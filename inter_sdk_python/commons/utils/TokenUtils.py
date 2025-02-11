import time
from datetime import datetime, timedelta

import requests

from ..exceptions.CertificateException import CertificateException
from ..models.Config import Config
from ..models.Error import Error
from ..models.GetTokenResponse import GetTokenResponse
from ..structures.Constants import Constants
from ..utils.UrlUtils import UrlUtils

class TokenUtils:
    ADDITIONAL_TIME = 60
    TOKEN_MAP: dict[str, GetTokenResponse] = {}

    @staticmethod
    def get(config: Config, scope: str) -> str:
        get_token_response = TokenUtils.get_from_map(config.client_id, config.client_secret, scope)

        if get_token_response is None or not TokenUtils.validate(get_token_response):
            get_token_response = TokenUtils.generate_token(config, scope)
            TokenUtils.add_to_map(config.client_id, config.client_secret, scope, get_token_response)

        return get_token_response.get("access_token")

    @staticmethod
    def validate(get_token_response: GetTokenResponse) -> bool:
        if not get_token_response:
            return False

        created_at = get_token_response['created_at']
        expires_in = get_token_response['expires_in']
        expiration_date = created_at + timedelta(seconds=expires_in)
        now = int(time.time())
        return (now + TokenUtils.ADDITIONAL_TIME) <= int(expiration_date.timestamp())

    @staticmethod
    def get_from_map(client_id: str, client_secret: str, scope: str):
        key = f"{client_id}:{client_secret}:{scope}"
        return TokenUtils.TOKEN_MAP.get(key)

    @staticmethod
    def add_to_map(client_id: str, client_secret: str, scope: str, get_token_response: GetTokenResponse):
        key = f"{client_id}:{client_secret}:{scope}"
        TokenUtils.TOKEN_MAP[key] = get_token_response

    @staticmethod
    def generate_token(config, scope):
        try:
            data = {
                "client_id": config.client_id,
                "client_secret": config.client_secret,
                "grant_type": "client_credentials",
                "scope": scope
            }

            response = requests.post(
                UrlUtils.build_url(config=config, url=Constants.URL_TOKEN),
                data=data,
                cert=(config.crt, config.key)
            )

            if response is None:
                return None

            response.raise_for_status()

            data = response.json()

            if data.get('created_at') is None:
                data['created_at'] = datetime.now()
    
            return data

        except Exception as exception:
            raise CertificateException(
                "Erro ao obter Token",
                Error(title="Erro ao obter Token", detail="Não foi possível obter token utilizando os dados fornecidos")
            )