import json
import logging
from typing import List

from inter_sdk_python.billing.models.BillingCallbackPage import BillingCallbackPage
from inter_sdk_python.billing.models.BillingRetrieveCallbackResponse import BillingRetrieveCallbackResponse
from inter_sdk_python.billing.models.BillingRetrieveCallbacksFilter import BillingRetrieveCallbacksFilter
from inter_sdk_python.commons.models.Config import Config
from inter_sdk_python.commons.models.IncludeWebhookRequest import IncludeWebhookRequest
from inter_sdk_python.commons.models.Webhook import Webhook
from inter_sdk_python.commons.structures.Constants import Constants
from inter_sdk_python.commons.utils.HttpUtils import HttpUtils
from inter_sdk_python.commons.utils.UrlUtils import UrlUtils
from inter_sdk_python.commons.utils.WebhookUtil import WebhookUtil


class BillingWebhookClient:

    def delete_webhook(self, config: Config) -> None:
        """
        Deletes the billing webhook associated with the specified configuration.

        Args:
            config (Config): The configuration object containing client information.

        Raises:
            SdkException: If there is an error during the deletion process, such as network issues
                           or API response errors.
        """
        logging.info("DeleteWebhook billing {}".format(config.client_id))
        url = UrlUtils.build_url(config, Constants.URL_BILLING_WEBHOOK)

        try:
            HttpUtils.call_delete(config, url, Constants.BILLET_BILLING_WRITE_SCOPE, "Error deleting webhook")
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def include_webhook(self, config: Config, webhook_url: str) -> None:
        """
        Includes a new webhook URL for billing notifications.

        Args:
            config (Config): The configuration object containing client information.
            webhook_url (str): The URL to be included as a webhook for billing notifications.

        Raises:
            SdkException: If there is an error during the inclusion process, such as network issues
                           or API response errors.
        """
        logging.info("IncludeWebhook billing {} {}".format(config.client_id, webhook_url))
        url = UrlUtils.build_url(config, Constants.URL_BILLING_WEBHOOK)
        request = IncludeWebhookRequest(webhook_url=webhook_url)

        try:
            WebhookUtil.include_webhook(config, url, request, Constants.BILLET_BILLING_WRITE_SCOPE)
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def retrieve_callback_page(
        self, 
        config: Config, 
        initial_date_hour: str, 
        final_date_hour: str, 
        page: int, 
        page_size: int, 
        filter: BillingRetrieveCallbacksFilter
    ) -> BillingCallbackPage:
        """
        Retrieves a page of callback responses based on the specified date range and optional filters.

        Args:
            config (Config): The configuration object containing client information.
            initial_date_hour (str): The start date and hour for the retrieval range (inclusive).
            final_date_hour (str): The end date and hour for the retrieval range (inclusive).
            page (int): The page number to retrieve.
            page_size (Optional[int]): The number of items per page (optional).
            filter (Optional[BillingRetrieveCallbacksFilter]): Optional filters to be applied to the callback retrieval.

        Returns:
            BillingCallbackPage: An object containing the requested page of callback responses.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveCallback {} {}-{}".format(config.client_id, initial_date_hour, final_date_hour))
        return self.get_page(config, initial_date_hour, final_date_hour, page, page_size, filter)

    def retrieve_callbacks_in_range(
        self, 
        config: Config, 
        initial_date_hour: str, 
        final_date_hour: str, 
        filter: BillingRetrieveCallbacksFilter,
        page_size: int
    ) -> List[BillingRetrieveCallbackResponse]:
        """
        Retrieves all callback responses within the specified date range, applying the given filters.

        Args:
            config (Config): The configuration object containing client information.
            initial_date_hour (str): The start date and hour for the retrieval range (inclusive).
            final_date_hour (str): The end date and hour for the retrieval range (inclusive).
            filter (Optional[BillingRetrieveCallbacksFilter]): Optional filters to be applied to the callback retrieval.

        Returns:
            List[BillingRetrieveCallbackResponse]: A list containing all callback responses
                                                   within the specified date range.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveCallback {} {}-{}".format(config.client_id, initial_date_hour, final_date_hour))
        page = 0
        callbacks = []

        while True:
            callback_page = self.get_page(config, initial_date_hour, final_date_hour, page, page_size, filter)
            callbacks.extend(callback_page.callbacks)
            page += 1
            if page >= callback_page.total_pages:
                break

        return callbacks

    def retrieve_webhook(self, config: Config) -> Webhook:
        """
        Retrieves the webhook configuration associated with the specified client configuration.

        Args:
            config (Config): The configuration object containing client information.

        Returns:
            Webhook: An object containing the current webhook settings.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveWebhook billing {}".format(config.client_id))
        url = UrlUtils.build_url(config, Constants.URL_BILLING_WEBHOOK)

        try:
            return WebhookUtil.retrieve_webhook(config, url, Constants.BILLET_BILLING_READ_SCOPE)
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def get_page(
        self, 
        config: Config, 
        initial_date_hour: str, 
        final_date_hour: str, 
        page: int, 
        page_size: int, 
        filter: BillingRetrieveCallbacksFilter
    ) -> BillingCallbackPage:
        """
        Retrieves a specific page of callbacks from the webhook.

        Args:
            config (Config): The configuration object containing client information.
            initial_date_hour (str): The start date and hour for the retrieval range (inclusive).
            final_date_hour (str): The end date and hour for the retrieval range (inclusive).
            page (int): The page number to retrieve.
            page_size (Optional[int]): The number of items per page (optional).
            filter (Optional[BillingRetrieveCallbacksFilter]): Optional filters to be applied to the callback retrieval.

        Returns:
            BillingCallbackPage: An object containing the requested page of callback responses.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        url = f"{UrlUtils.build_url(config, Constants.URL_BILLING_WEBHOOK_CALLBACKS)}" \
              f"?dataHoraInicio={initial_date_hour}&dataHoraFim={final_date_hour}" \
              f"&pagina={page}" \
              + (f"&itensPorPagina={page_size}" if page_size is not None else "") \
              + self.add_filters(filter)

        json_response = HttpUtils.call_get(config, url, Constants.BILLET_BILLING_READ_SCOPE, "Error retrieving callbacks")
        
        try:
            return BillingCallbackPage.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def add_filters(self, filter: BillingRetrieveCallbacksFilter) -> str:
        """
        Constructs the query string for filters to be applied when retrieving callbacks.

        Args:
            filter (Optional[BillingRetrieveCallbacksFilter]): The filter object containing filtering criteria.

        Returns:
            str: A query string that can be appended to the URL for filtering.
        """
        if filter is None:
            return ""

        string_filter = []

        if filter.request_code is not None:
            string_filter.append(f"&codigoSolicitacao={filter.request_code}")

        return ''.join(string_filter)