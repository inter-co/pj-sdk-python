import json
import logging

from inter_sdk_python.commons.models.Config import Config
from inter_sdk_python.commons.models.IncludeWebhookRequest import IncludeWebhookRequest
from inter_sdk_python.commons.models.Webhook import Webhook
from inter_sdk_python.commons.utils.HttpUtils import HttpUtils

class WebhookUtil:
    @staticmethod
    def include_webhook(config: Config, url: str, request: IncludeWebhookRequest, scope: str):
        try:
            json_data = json.dumps(request.to_dict(), indent=4)
            HttpUtils.call_put(config, url, scope, "Error including webhook", json_data)
        except Exception as io_exception:
            logging.error("An error occurred: %s", io_exception)
            raise

    @staticmethod
    def retrieve_webhook(config: Config, url: str, scope: str) -> Webhook:
        json_data = HttpUtils.call_get(config, url, scope, "Error retrieving webhook")
        try:
            return Webhook.from_dict(json_data)
        except Exception as io_exception:
            logging.error("An error occurred: %s", io_exception)
            raise