import json
import logging
import time
from typing import Optional

import requests

from inter_sdk_python.commons.models.Config import Config
from inter_sdk_python.commons.structures.Constants import Constants
from ..exceptions.ClientException import ClientException
from ..exceptions.SdkException import SdkException
from ..exceptions.ServerException import ServerException
from ..models.Error import Error
from ..utils.TokenUtils import TokenUtils

class HttpUtils:
    SLEEP = 60
    CLIENT_ERROR_BASE = 400
    SERVER_ERROR_BASE = 500
    TOO_MANY_REQUESTS = 429
    SUCCESSFUL = 200
    REDIRECTION = 300
    APPLICATION_JSON = "application/json"
    NO_CONTENT = [204, 202]

    last_url: Optional[str] = None
    last_request: Optional[str] = None

    @staticmethod
    def call_get(config: Config, url: str, scope: str, message: str) -> str:
        logging.info("http GET %s", url)
        return HttpUtils.call(config, "GET", url, scope, message, "")

    @staticmethod
    def call_put(config: Config, url: str, scope: str, message: str, json_data: str) -> str:
        return HttpUtils.call(config, "PUT", url, scope, message, json_data)

    @staticmethod
    def call_patch(config: Config, url: str, scope: str, message: str, json_data: str) -> str:
        return HttpUtils.call(config, "PATCH", url, scope, message, json_data)

    @staticmethod
    def call_post(config: Config, url: str, scope: str, message: str, json_data: str) -> str:
        return HttpUtils.call(config, "POST", url, scope, message, json_data)

    @staticmethod
    def call_delete(config: Config, url: str, scope: str, message: str) -> str:
        logging.info("http DELETE %s", url)
        return HttpUtils.call(config, "DELETE", url, scope, message, {})
    
    @staticmethod
    def call(config: Config, method: str, url: str, scope: str, message: str, json_data: str) -> str:
        try:
            access_token = TokenUtils.get(config, scope)
            
            headers = {
                'Authorization': f'Bearer {access_token}',
                'x-inter-sdk': 'python',
                'x-inter-sdk-version': '1.0.2',
                'Content-Type': 'application/json'
            }

            if config.account is not None:
                headers["x-conta-corrente"] = config.account

            response = None
            if method == "GET":
                response = requests.get(url, headers=headers, cert=(config.crt, config.key))
            elif method == "PUT":
                response = requests.put(
                    url,
                    data=json_data,
                    headers=headers,
                    cert=(config.crt, config.key)
                )
            elif method == "POST":
                response = requests.post(
                    url,
                    data=json_data,
                    headers=headers,
                    cert=(config.crt, config.key)
                )
            elif method == "PATCH":
                response = requests.patch(
                    url,
                    data=json_data,
                    headers=headers,
                    cert=(config.crt, config.key)
                )
            elif method == "DELETE":
                response = requests.delete(url, headers=headers, cert=(config.crt, config.key))

            if response is not None:
                retry = HttpUtils.handle_response(url, response, message, config.rate_limit_control)
            else:
                raise SdkException(
                    "No response received",
                    Error(title="No response", detail="The response object is None", timestamp=None)
                )
            
            if retry:
                time.sleep(60)
                return HttpUtils.call(config, method, url, scope, message, json_data)
            
            if config.debug and response.json():
                logging.info(response.json())

            if response.status_code in HttpUtils.NO_CONTENT:
                return ""

            return response.json()

        except Exception as exception:
            logging.error(Constants, exc_info=True)
            error = getattr(exception, 'error', None)

            title_detail = None
            message_detail = None
            violations = None
            if error is not None:
                if hasattr(error, 'title'):
                    title_detail = error.title
                if hasattr(error, 'detail'):
                    message_detail = error.detail
                if hasattr(error, 'violations'):
                    violations = error.violations

            raise SdkException(
                message,
                Error(title=title_detail, detail=message_detail, timestamp=None, violations=violations)
            )

    @staticmethod
    def handle_response(url: str, response: requests.Response, message: str, rate_limit_control: bool) -> bool:
        logging.info("http status=%s %s", response.status_code, url)
        if HttpUtils.SUCCESSFUL <= response.status_code <= HttpUtils.REDIRECTION:
            return False

        if response.status_code >= HttpUtils.SERVER_ERROR_BASE:
            error = HttpUtils.convert_json_to_error(response.text)
            e = ServerException(message, error)
            raise e

        if response.status_code >= HttpUtils.CLIENT_ERROR_BASE:
            if response.status_code == HttpUtils.TOO_MANY_REQUESTS and rate_limit_control:
                return True
            json_body = response.content.decode('utf-8')
            if not json_body:
                detail = response.reason if response.reason else ""
                error = Error(title=str(response.status_code), detail= detail, timestamp="")
            else:
                error = HttpUtils.convert_json_to_error(json_body)
            e = ClientException(message, error)
            raise e

        return False

    @staticmethod
    def convert_json_to_error(string_json: str) -> Error:
        return Error.from_dict(json.loads(string_json))