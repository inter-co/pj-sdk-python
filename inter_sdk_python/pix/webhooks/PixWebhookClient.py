import json
import logging
from typing import List

from inter_sdk_python.commons.exceptions.SdkException import SdkException
from inter_sdk_python.commons.models.Config import Config
from inter_sdk_python.commons.models.Error import Error
from inter_sdk_python.commons.models.IncludeWebhookRequest import IncludeWebhookRequest
from inter_sdk_python.commons.models.Webhook import Webhook
from inter_sdk_python.commons.structures.Constants import Constants
from inter_sdk_python.commons.utils.HttpUtils import HttpUtils
from inter_sdk_python.commons.utils.UrlUtils import UrlUtils
from inter_sdk_python.commons.utils.WebhookUtil import WebhookUtil
from inter_sdk_python.pix.models.CallbackRetrieveFilter import CallbackRetrieveFilter
from inter_sdk_python.pix.models.PixCallbackPage import PixCallbackPage
from inter_sdk_python.pix.models.RetrieveCallbackResponse import RetrieveCallbackResponse


class PixWebhookClient:
    def delete_webhook(self, config: Config, key: str) -> None:
        """
        Deletes a webhook identified by the provided key.

        Args:
            config (Config): The configuration object containing client information.
            key (str): The unique key of the webhook to be deleted.

        Raises:
            SdkException: If there is an error during the deletion process, such as network issues
                           or API response errors.
        """
        logging.info("DeleteWebhook pix {} {}".format(config.client_id, key))
        
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_WEBHOOK)}/{key}"
        
        HttpUtils.call_delete(config, url, Constants.PIX_WEBHOOK_WRITE_SCOPE, "Error deleting webhook")

    def include_webhook(self, config: Config, key: str, webhook_url: str) -> None:
        """
        Includes a webhook for the specified key and webhook URL.

        Args:
            config (Config): The configuration object containing client information.
            key (str): The unique key for which the webhook is being included.
            webhook_url (str): The URL of the webhook to be included.

        Raises:
            SdkException: If there is an error during the inclusion process, such as network issues
                           or API response errors.
        """
        logging.info("IncludeWebhook pix {} {} {}".format(config.client_id, key, webhook_url))
        
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_WEBHOOK)}/{key}"
        request = IncludeWebhookRequest(webhook_url=webhook_url)

        WebhookUtil.include_webhook(config, url, request, Constants.PIX_WEBHOOK_WRITE_SCOPE)

    def retrieve_callbacks_page(
        self, 
        config: Config, 
        initial_date_hour: str, 
        final_date_hour: str, 
        page: int, 
        page_size: int, 
        filter: CallbackRetrieveFilter
    ) -> PixCallbackPage:
        """
        Retrieves a paginated list of callback notifications based on specified date range and filters.

        Args:
            config (Config): The configuration object containing client information.
            initial_date_hour (str): The start date and time for the retrieval range (inclusive).
            final_date_hour (str): The end date and time for the retrieval range (inclusive).
            page (int): The page number to retrieve.
            page_size (int): The number of items per page.
            filter (CallbackRetrieveFilter): An object containing filter criteria.

        Returns:
            PixCallbackPage: An object containing the requested page of callback notifications.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveCallbacks pix {} {}-{}".format(config.client_id, initial_date_hour, final_date_hour))
        
        return self.get_page(config, initial_date_hour, final_date_hour, page, page_size, filter)
    
    def retrieve_callbacks_in_range(
        self, 
        config: Config, 
        initial_date_hour: str, 
        final_date_hour: str, 
        filter: CallbackRetrieveFilter
    ) -> List[RetrieveCallbackResponse]:
        """
        Retrieves all callback notifications within the specified date range and filters.

        Args:
            config (Config): The configuration object containing client information.
            initial_date_hour (str): The start date and time for the retrieval range (inclusive).
            final_date_hour (str): The end date and time for the retrieval range (inclusive).
            filter (CallbackRetrieveFilter): An object containing filter criteria.

        Returns:
            List[RetrieveCallbackResponse]: A list of objects containing all retrieved callbacks.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveCallbacks pix {} {}-{}".format(config.client_id, initial_date_hour, final_date_hour))
        
        page = 0
        callbacks = []

        while True:
            callback_page = self.get_page(config, initial_date_hour, final_date_hour, page, None, filter)
            callbacks.extend(callback_page.data)
            page += 1
            if page >= callback_page.total_pages:
                break
        
        return callbacks
    
    def retrieve_webhook(self, config: Config, key: str) -> Webhook:
        """
        Retrieves a webhook identified by the provided key.

        Args:
            config (Config): The configuration object containing client information.
            key (str): The unique key of the webhook to be retrieved.

        Returns:
            Webhook: An object containing the details of the retrieved webhook.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveWebhook pix {} {}".format(config.client_id, key))
        
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_WEBHOOK)}/{key}"
        
        return WebhookUtil.retrieve_webhook(config, url, Constants.PIX_WEBHOOK_READ_SCOPE)
    
    def get_page(
        self, 
        config: Config, 
        initial_date_hour: str, 
        final_date_hour: str, 
        page: int, 
        page_size: int, 
        filter: CallbackRetrieveFilter
    ) -> PixCallbackPage:
        """
        Retrieves a specific page of callback notifications based on the provided date range and filters.

        Args:
            config (Config): The configuration object containing client information.
            initial_date_hour (str): The start date and time for the retrieval range (inclusive).
            final_date_hour (str): The end date and time for the retrieval range (inclusive).
            page (int): The page number to retrieve.
            page_size (int): The number of items per page.
            filter (CallbackRetrieveFilter): An object containing filter criteria.

        Returns:
            PixCallbackPage: An object containing the requested page of callback notifications.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_WEBHOOK_CALLBACKS)}?dataHoraInicio={initial_date_hour}&dataHoraFim={final_date_hour}&pagina={page}"
        
        if page_size is not None:
            url += f"&tamanhoPagina={page_size}"
        
        if filter is not None:
            url += self.add_filters(filter)
        
        json_response = HttpUtils.call_get(config, url, Constants.PIX_WEBHOOK_READ_SCOPE, "Error retrieving callbacks")
        
        try:
            return PixCallbackPage.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise SdkException(
                str(io_exception),
                Error(title=Constants.CERTIFICATE_EXCEPTION_MESSAGE, detail=str(io_exception))
            )
        
    def add_filters(self, filter: CallbackRetrieveFilter) -> str:
        """
        Adds filter parameters to the URL based on the provided filter criteria.

        Args:
            filter (CallbackRetrieveFilter): An object containing filter criteria.

        Returns:
            str: A string containing the appended filter parameters for the URL.
        """
        if filter is None:
            return ""
        
        string_filter = []

        if filter.txid is not None:
            string_filter.append(f"&txid={filter.txid}")

        return ''.join(string_filter)