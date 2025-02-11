import json
import logging
from typing import List

from inter_sdk_python.commons.models.Config import Config
from inter_sdk_python.commons.structures.Constants import Constants
from inter_sdk_python.commons.utils.HttpUtils import HttpUtils
from inter_sdk_python.commons.utils.UrlUtils import UrlUtils
from inter_sdk_python.pix.models.BillingPage import BillingPage
from inter_sdk_python.pix.models.DetailedImmediatePixBilling import DetailedImmediatePixBilling
from inter_sdk_python.pix.models.GeneratedImmediateBilling import GeneratedImmediateBilling
from inter_sdk_python.pix.models.PixBilling import PixBilling
from inter_sdk_python.pix.models.RetrieveImmediateBillingsFilter import RetrieveImmediateBillingsFilter


class ImmediateBillingClient:
    def include_immediate_billing(self, config: Config, billing: PixBilling) -> GeneratedImmediateBilling:
        """
        Includes a new immediate billing or updates an existing one based on the provided configuration and billing details.

        Args:
            config (Config): The configuration object containing client information.
            billing (PixBilling): The object containing the details of the billing to be included.

        Returns:
            GeneratedImmediateBilling: An object containing the details of the generated immediate billing.

        Raises:
            SdkException: If there is an error during the inclusion process, such as network issues
                           or API response errors.
        """
        logging.info("IncludeImmediateBilling {} {}".format(config.client_id, billing.txid))
        url = UrlUtils.build_url(config, Constants.URL_PIX_IMMEDIATE_BILLINGS)
        
        try:
            json_data = billing.to_json()
            if billing.txid is None:
                json_response = HttpUtils.call_post(config, url, Constants.PIX_IMMEDIATE_BILLING_WRITE_SCOPE, "Error including immediate billing", json_data)
            else:
                url += f"/{billing.txid}"
                json_response = HttpUtils.call_put(config, url, Constants.PIX_IMMEDIATE_BILLING_WRITE_SCOPE, "Error including immediate billing", json_data)

            return GeneratedImmediateBilling.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def retrieve_immediate_billing(self, config: Config, tx_id: str) -> DetailedImmediatePixBilling:
        """
        Retrieves the details of an immediate billing based on the provided configuration and transaction ID.

        Args:
            config (Config): The configuration object containing client information.
            tx_id (str): The unique transaction ID for the immediate billing to be retrieved.

        Returns:
            DetailedImmediatePixBilling: An object containing the details of the retrieved immediate billing.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveImmediateBilling {} txId={}".format(config.client_id, tx_id))
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_IMMEDIATE_BILLINGS)}/{tx_id}"
        
        json_response = HttpUtils.call_get(config, url, Constants.PIX_IMMEDIATE_BILLING_READ_SCOPE, "Error retrieving immediate billing")
        
        try:
            return DetailedImmediatePixBilling.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def retrieve_immediate_billing_page(
        self, 
        config: Config, 
        initial_date: str, 
        final_date: str, 
        page: int, 
        page_size: int, 
        filter: RetrieveImmediateBillingsFilter
    ) -> BillingPage:
        """
        Retrieves a paginated list of immediate billings based on the specified date range, page number, and filters.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date for the retrieval range (inclusive).
            final_date (str): The end date for the retrieval range (inclusive).
            page (int): The page number to retrieve.
            page_size (Optional[int]): The number of items per page (optional).
            filter (RetrieveImmediateBillingsFilter): An object containing filter criteria.

        Returns:
            BillingPage: An object containing the requested page of immediate billings.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveImmediateBillingList {} {}-{} page={}".format(config.client_id, initial_date, final_date, page))
        return self.get_page(config, initial_date, final_date, page, page_size, filter)

    def retrieve_immediate_billings_in_range(
        self, 
        config: Config, 
        initial_date: str, 
        final_date: str, 
        filter: RetrieveImmediateBillingsFilter
    ) -> List[DetailedImmediatePixBilling]:
        """
        Retrieves all immediate billings within the specified date range and filters.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date for the retrieval range (inclusive).
            final_date (str): The end date for the retrieval range (inclusive).
            filter (RetrieveImmediateBillingsFilter): An object containing filter criteria.

        Returns:
            List[DetailedImmediatePixBilling]: A list of objects containing all retrieved immediate billings.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveImmediateBillingList {} {}-{}".format(config.client_id, initial_date, final_date))
        page = 0
        cobrancas = []

        while True:
            billing_page = self.get_page(config, initial_date, final_date, page, None, filter)
            cobrancas.extend(billing_page.billings)
            page += 1
            if page >= billing_page.total_pages:
                break

        return cobrancas

    def review_immediate_billing(self, config: Config, cobranca: PixBilling) -> GeneratedImmediateBilling:
        """
        Reviews an immediate billing based on the provided configuration and billing details.

        Args:
            config (Config): The configuration object containing client information.
            cobranca (PixBilling): The object containing the details of the billing to be reviewed.

        Returns:
            GeneratedImmediateBilling: An object containing the details of the reviewed immediate billing.

        Raises:
            SdkException: If there is an error during the review process, such as network issues
                           or API response errors.
        """
        logging.info("ReviewImmediateBilling {} {}".format(config.client_id, cobranca.txid))
        
        try:
            url = f"{UrlUtils.build_url(config, Constants.URL_PIX_IMMEDIATE_BILLINGS)}/{cobranca.txid}"
            json_data = cobranca.to_json()
            
            json_response = HttpUtils.call_patch(config, url, Constants.PIX_IMMEDIATE_BILLING_WRITE_SCOPE, "Error reviewing immediate billing", json_data)
            return GeneratedImmediateBilling.from_dict(json_response)

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
        filter: RetrieveImmediateBillingsFilter
    ) -> BillingPage:
        """
        Retrieves a specific page of immediate billings based on the provided criteria.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date for the retrieval range (inclusive).
            final_date (str): The end date for the retrieval range (inclusive).
            page (int): The page number to retrieve.
            page_size (Optional[int]): The number of items per page (optional).
            filter (RetrieveImmediateBillingsFilter): An object containing filter criteria.

        Returns:
            BillingPage: An object containing the requested page of immediate billings.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_IMMEDIATE_BILLINGS)}?inicio={initial_date}&fim={final_date}&paginacao.paginaAtual={page}"
        
        if page_size is not None:
            url += f"&paginacao.itensPorPagina={page_size}"
        
        if filter is not None:
            url += self.add_filters(filter)
        
        json_response = HttpUtils.call_get(config, url, Constants.PIX_IMMEDIATE_BILLING_READ_SCOPE, "Error retrieving list of immediate billings")
        
        try:
            return BillingPage.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def add_filters(self, filter: RetrieveImmediateBillingsFilter) -> str:
        """
        Adds filter parameters to the URL based on the provided filter criteria.

        Args:
            filter (RetrieveImmediateBillingsFilter): An object containing filter criteria.

        Returns:
            str: A string containing the appended filter parameters for the URL.
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