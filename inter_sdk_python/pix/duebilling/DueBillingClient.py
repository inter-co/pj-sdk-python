import json
import logging
from typing import List

from inter_sdk_python.commons.models.Config import Config
from inter_sdk_python.commons.structures.Constants import Constants
from inter_sdk_python.commons.utils.HttpUtils import HttpUtils
from inter_sdk_python.commons.utils.UrlUtils import UrlUtils
from inter_sdk_python.pix.models.DetailedDuePixBilling import DetailedDuePixBilling
from inter_sdk_python.pix.models.DueBilling import DueBilling
from inter_sdk_python.pix.models.DueBillingPage import DueBillingPage
from inter_sdk_python.pix.models.GeneratedDueBilling import GeneratedDueBilling
from inter_sdk_python.pix.models.RetrieveDueBillingFilter import RetrieveDueBillingFilter


class DueBillingClient:
    def include_due_billing(self, config: Config, txid: str, billing: DueBilling) -> GeneratedDueBilling:
        """
        Includes a due billing entry into the system for a specified transaction ID.

        Args:
            config (Config): The configuration object containing client information.
            txid (str): The transaction ID associated with the due billing.
            billing (DueBilling): The object containing the billing details to be included.

        Returns:
            GeneratedDueBilling: An object containing the details of the generated billing.

        Raises:
            SdkException: If there is an error during the inclusion process, such as network issues
                           or API response errors.
        """
        logging.info("IncludeDueBilling {} {}".format(config.client_id, txid))
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_SCHEDULED_BILLINGS)}/{txid}"
        
        try:
            json_data = billing.to_json()
            json_response = HttpUtils.call_put(config, url, Constants.PIX_SCHEDULED_BILLING_WRITE_SCOPE, "Error including due billing", json_data)
            return GeneratedDueBilling.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def retrieve_due_billing(self, config: Config, txid: str) -> DetailedDuePixBilling:
        """
        Retrieves detailed information about a scheduled Pix billing using the provided transaction ID.

        Args:
            config (Config): The configuration object containing client information.
            txid (str): The transaction ID associated with the scheduled Pix billing.

        Returns:
            DetailedDuePixBilling: An object containing the details of the scheduled billing.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveDueBilling {} txId={}".format(config.client_id, txid))
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_SCHEDULED_BILLINGS)}/{txid}"
        
        json_response = HttpUtils.call_get(config, url, Constants.PIX_SCHEDULED_BILLING_READ_SCOPE, "Error retrieving due billing")
        
        try:
            return DetailedDuePixBilling.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def retrieve_due_billing_page(
        self, 
        config: Config, 
        initial_date: str, 
        final_date: str, 
        page: int, 
        page_size: int, 
        filter: RetrieveDueBillingFilter
    ) -> DueBillingPage:
        """
        Retrieves a page of scheduled Pix billings within a specified date range and optional filters.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date for the retrieval range (inclusive).
            final_date (str): The end date for the retrieval range (inclusive).
            page (int): The page number to retrieve.
            page_size (Optional[int]): The number of items per page (optional).
            filter (Optional[RetrieveDueBillingFilter]): Optional filters to be applied during retrieval.

        Returns:
            DueBillingPage: An object containing the requested page of due billings.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveDueBillingList {} {}-{} page={}".format(config.client_id, initial_date, final_date, page))
        return self.get_page(config, initial_date, final_date, page, page_size, filter)

    def retrieve_due_billings_in_range(
        self, 
        config: Config, 
        initial_date: str, 
        final_date: str, 
        filter: RetrieveDueBillingFilter
    ) -> List[DetailedDuePixBilling]:
        """
        Retrieves all scheduled Pix billings within a specified date range and applies the given filters.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date for the retrieval range (inclusive).
            final_date (str): The end date for the retrieval range (inclusive).
            filter (Optional[RetrieveDueBillingFilter]): Optional filters to be applied during retrieval.

        Returns:
            List[DetailedDuePixBilling]: A list of objects containing all retrieved billings.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveDueBillingList {} {}-{}".format(config.client_id, initial_date, final_date))
        page = 0
        billings = []

        while True:
            due_billing_page = self.get_page(config, initial_date, final_date, page, None, filter)
            billings.extend(due_billing_page.due_billings)
            page += 1
            if page >= due_billing_page.total_pages:
                break

        return billings

    def review_due_billing(self, config: Config, txid: str, billing: DueBilling) -> GeneratedDueBilling:
        """
        Reviews a scheduled Pix billing entry based on the specified transaction ID.

        Args:
            config (Config): The configuration object containing client information.
            txid (str): The transaction ID associated with the due billing to be reviewed.
            billing (DueBilling): The object containing the updated billing details.

        Returns:
            GeneratedDueBilling: An object containing the details of the reviewed billing.

        Raises:
            SdkException: If there is an error during the review process, such as network issues
                           or API response errors.
        """
        logging.info("ReviewDueBilling {} {}".format(config.client_id, txid))
        
        try:
            url = f"{UrlUtils.build_url(config, Constants.URL_PIX_SCHEDULED_BILLINGS)}/{txid}"
            json_data = billing.to_json()
            json_response = HttpUtils.call_patch(config, url, Constants.PIX_SCHEDULED_BILLING_WRITE_SCOPE, "Error retrieving due billing", json_data)
            return GeneratedDueBilling.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def get_page(
        self, 
        config: Config, 
        initial_date: str, 
        final_date: str, 
        page: int, 
        page_size: int,
        filter: RetrieveDueBillingFilter
    ) -> DueBillingPage:
        """
        Retrieves a specific page of scheduled Pix billings based on the provided criteria.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date for the retrieval range (inclusive).
            final_date (str): The end date for the retrieval range (inclusive).
            page (int): The page number to retrieve.
            page_size (Optional[int]): The number of items per page (optional).
            filter (Optional[RetrieveDueBillingFilter]): Optional filters to be applied during retrieval.

        Returns:
            DueBillingPage: An object containing the requested page of due billings.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_SCHEDULED_BILLINGS)}" \
              f"?inicio={initial_date}&fim={final_date}" \
              f"&paginacao.paginaAtual={page}" \
              + (f"&paginacao.itensPorPagina={page_size}" if page_size is not None else "") \
              + self.add_filters(filter)

        json_response = HttpUtils.call_get(config, url, Constants.PIX_SCHEDULED_BILLING_READ_SCOPE, "Error retrieving due billing")
        
        try:
            return DueBillingPage.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def add_filters(self, filter: RetrieveDueBillingFilter) -> str:
        """
        Constructs the query string for filters to be applied when retrieving due billings.

        Args:
            filter (Optional[RetrieveDueBillingFilter]): The filter object containing filtering criteria.

        Returns:
            str: A query string that can be appended to the URL for filtering.
        """
        if filter is None:
            return ""

        string_filter = []

        if filter.cpf is not None:
            string_filter.append(f"&cpf={filter.cpf}")
        if filter.cnpj is not None:
            string_filter.append(f"&cnpj={filter.cnpj}")
        if filter.location_present is not None:
            string_filter.append(f"&locationPresente={filter.location_present}")
        if filter.status is not None:
            string_filter.append(f"&status={filter.status}")

        return ''.join(string_filter)