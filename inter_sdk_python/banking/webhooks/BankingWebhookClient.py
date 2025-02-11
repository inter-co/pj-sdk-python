import json
import logging
from typing import List

from inter_sdk_python.banking.models.CallbackPage import CallbackPage
from inter_sdk_python.banking.models.CallbackRetrieveFilter import CallbackRetrieveFilter
from inter_sdk_python.banking.models.RetrieveCallbackResponse import RetrieveCallbackResponse
from inter_sdk_python.commons.models.Config import Config
from inter_sdk_python.commons.models.IncludeWebhookRequest import IncludeWebhookRequest
from inter_sdk_python.commons.models.Webhook import Webhook
from inter_sdk_python.commons.structures.Constants import Constants
from inter_sdk_python.commons.utils.HttpUtils import HttpUtils
from inter_sdk_python.commons.utils.UrlUtils import UrlUtils
from inter_sdk_python.commons.utils.WebhookUtil import WebhookUtil


class BankingWebhookClient:
    def delete_webhook(self, config: Config, webhook_type: str) -> None:
        """
        Deletes a specified webhook based on its type.

        Args:
            config (Config): The configuration object containing client information.
            webhook_type (str): The type of the webhook to be deleted.

        Raises:
            SdkException: If there is an error during the deletion process, such as
                           network issues or API response errors.
        """
        logging.info("DeleteWebhook banking {} {}".format(config.client_id, webhook_type))
        url = f"{UrlUtils.build_url(config, Constants.URL_BANKING_WEBHOOK)}/{webhook_type}"
        
        try:
            HttpUtils.call_delete(config, url, Constants.WEBHOOK_BANKING_WRITE_SCOPE, "Error deleting webhook")
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise
        
    def include_webhook(self, config: Config, webhook_type: str, webhook_url: str) -> None:
        """
        Includes a new webhook configuration for a specified type and URL.

        Args:
            config (Config): The configuration object containing client information.
            webhook_type (str): The type of the webhook to be included.
            webhook_url (str): The URL where the webhook will send notifications.

        Raises:
            SdkException: If there is an error during the inclusion process, such as
                           network issues or API response errors.
        """
        logging.info("IncludeWebhookBanking {} {} {}".format(config.client_id, webhook_type, webhook_url))
        url = f"{UrlUtils.build_url(config, Constants.URL_BANKING_WEBHOOK)}/{webhook_type}"
        request = IncludeWebhookRequest(webhook_url=webhook_url)

        try:
            WebhookUtil.include_webhook(config, url, request, Constants.WEBHOOK_BANKING_WRITE_SCOPE)
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def retrieve_callbacks_page(
        self, 
        config: Config, 
        webhook_type: str, 
        initial_date_hour: str, 
        final_date_hour: str, 
        page: int, 
        page_size: int, 
        filter: CallbackRetrieveFilter
    ) -> CallbackPage:
        """
        Retrieves a page of callback responses for a specified webhook type within a given date range.

        Args:
            config (Config): The configuration object containing client information.
            webhook_type (str): The type of the webhook to retrieve callbacks for.
            initial_date_hour (str): The start date and hour for the retrieval range (inclusive).
            final_date_hour (str): The end date and hour for the retrieval range (inclusive).
            page (int): The page number to retrieve.
            page_size (Optional[int]): The number of items per page (optional).
            filter (Optional[CallbackRetrieveFilter]): Optional filters to apply to the callback retrieval.

        Returns:
            CallbackPage: An object containing the requested page of callback responses.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveCallbacks {} {}-{}".format(config.client_id, initial_date_hour, final_date_hour))
        return self.get_page(config, webhook_type, initial_date_hour, final_date_hour, page, page_size, filter)

    def retrieve_callbacks_in_range(
        self, 
        config: Config, 
        webhook_type: str, 
        initial_date: str, 
        final_date: str, 
        filter: CallbackRetrieveFilter
    ) -> List[RetrieveCallbackResponse]:
        """
        Retrieves all callback responses for a specified webhook type within a given date range.

        Args:
            config (Config): The configuration object containing client information.
            webhook_type (str): The type of the webhook to retrieve callbacks for.
            initial_date (str): The start date for the retrieval range (inclusive).
            final_date (str): The end date for the retrieval range (inclusive).
            filter (Optional[CallbackRetrieveFilter]): Optional filters to apply to the callback retrieval.

        Returns:
            List[RetrieveCallbackResponse]: A list containing all callback responses
                                              within the specified date range.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveCallbacks {} {}-{}".format(config.client_id, initial_date, final_date))
        page = 0
        callbacks = []

        while True:
            callback_page = self.get_page(config, webhook_type, initial_date, final_date, page, None, filter)

            if callback_page.data is not None:
                callbacks.extend(callback_page.data)

            page += 1
            if page >= callback_page.total_pages:
                break

        return callbacks

    def retrieve_webhook(self, config: Config, webhook_type: str) -> Webhook:
        """
        Retrieves the configuration for a specified webhook type.

        Args:
            config (Config): The configuration object containing client information.
            webhook_type (str): The type of the webhook to be retrieved.

        Returns:
            Webhook: An object containing the configuration details of the requested webhook.

        Raises:
            SdkException: If there is an error during the retrieval process, such as
                           network issues or API response errors.
        """
        logging.info("RetrieveWebhook banking {} {}".format(config.client_id, webhook_type))
        url = f"{UrlUtils.build_url(config, Constants.URL_BANKING_WEBHOOK)}/{webhook_type}"

        try:
            return WebhookUtil.retrieve_webhook(config, url, Constants.WEBHOOK_BANKING_READ_SCOPE)
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def get_page(
        self, 
        config: Config, 
        webhook_type: str, 
        initial_date_hour: str, 
        final_date_hour: str, 
        page: int, 
        page_size: int, 
        filter: CallbackRetrieveFilter
    ) -> CallbackPage:
        """
        Retrieves a specific page of callback responses for a specified webhook type.

        Args:
            config (Config): The configuration object containing client information.
            webhook_type (str): The type of the webhook to retrieve callbacks for.
            initial_date_hour (str): The start date and hour for the retrieval range (inclusive).
            final_date_hour (str): The end date and hour for the retrieval range (inclusive).
            page (int): The page number to retrieve.
            page_size (Optional[int]): The number of items per page (optional).
            filter (Optional[CallbackRetrieveFilter]): Optional filters to apply to the callback retrieval.

        Returns:
            CallbackPage: An object containing the requested page of callback responses.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        url1 = f"{UrlUtils.build_url(config, Constants.URL_BANKING_WEBHOOK)}/{webhook_type}/callbacks"
        url = f"{url1}?dataHoraInicio={initial_date_hour}&dataHoraFim={final_date_hour}&pagina={page}"
        
        if page_size is not None:
            url += f"&tamanhoPagina={page_size}"
        
        url += self.add_filters(filter)

        json_response = HttpUtils.call_get(config, url, Constants.WEBHOOK_BANKING_READ_SCOPE, "Error retrieving callbacks")
        
        try:
            return CallbackPage.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def add_filters(self, filter: CallbackRetrieveFilter) -> str:
        """
        Constructs the query string for filters to be applied when retrieving callbacks.

        Args:
            filter (Optional[CallbackRetrieveFilter]): The filter object containing filtering criteria.

        Returns:
            str: A query string that can be appended to the URL for filtering.
        """
        if filter is None:
            return ""

        string_filter = []

        if filter.transaction_code is not None:
            string_filter.append(f"&codigoTransacao={filter.transaction_code}")

        if filter.end_to_end_id is not None:
            string_filter.append(f"&endToEnd={filter.end_to_end_id}")

        return ''.join(string_filter)