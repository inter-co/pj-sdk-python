import base64
import json
import logging
from typing import List

from inter_sdk_python.billing.models.BillingIssueRequest import BillingIssueRequest
from inter_sdk_python.billing.models.BillingIssueResponse import BillingIssueResponse
from inter_sdk_python.billing.models.BillingPage import BillingPage
from inter_sdk_python.billing.models.BillingRetrievalFilter import BillingRetrievalFilter
from inter_sdk_python.billing.models.CancelBillingRequest import CancelBillingRequest
from inter_sdk_python.billing.models.RetrievedBilling import RetrievedBilling
from inter_sdk_python.billing.models.Sorting import Sorting
from inter_sdk_python.billing.models.Summary import Summary
from inter_sdk_python.billing.models.SummaryItem import SummaryItem
from inter_sdk_python.commons.models.Config import Config
from inter_sdk_python.commons.models.PdfReturn import PdfReturn
from inter_sdk_python.commons.structures.Constants import Constants
from inter_sdk_python.commons.utils.HttpUtils import HttpUtils
from inter_sdk_python.commons.utils.UrlUtils import UrlUtils


class BillingClient:

    def cancel_billing(self, config: Config, request_code: str, cancellation_reason: str) -> None:
        """
        Cancels a billing request identified by its request code.

        Args:
            config (Config): The configuration object containing client information.
            request_code (str): The unique identifier for the billing request to be canceled.
            cancellation_reason (str): The reason for canceling the billing request.

        Raises:
            SdkException: If there is an error during the cancellation process, such as
                          network issues or API response errors.
        """
        logging.info("CancelBilling {} {} {}".format(config.client_id, request_code, cancellation_reason))
        
        url = UrlUtils.build_url(config, Constants.URL_BILLING) + f"/{request_code}/cancelar"
        
        request = CancelBillingRequest(cancellation_reason)
        
        try:
            json_request = request.to_json()
            HttpUtils.call_post(config, url, Constants.BILLET_BILLING_WRITE_SCOPE, "Error canceling billing", json_request)
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def issue_billing(self, config: Config, billing_issue_request: BillingIssueRequest) -> BillingIssueResponse:
        """
        Issues a new billing request based on the provided billing issue details.

        Args:
            config (Config): The configuration object containing client information.
            billing_issue_request (BillingIssueRequest): The request object containing details for the billing to be issued.

        Returns:
            BillingIssueResponse: An object containing the response details from the billing issue process.

        Raises:
            SdkException: If there is an error during the billing issuance process, such as network issues
                            or API response errors.
        """
        logging.info("IssueBilling {} {}".format(config.client_id, billing_issue_request.your_number))
        
        url = UrlUtils.build_url(config, Constants.URL_BILLING)
        
        try:
            json_request = billing_issue_request.to_json()
            json_response = HttpUtils.call_post(config, url, Constants.BILLET_BILLING_WRITE_SCOPE, "Error issuing billing", json_request)
            return BillingIssueResponse.from_dict(json_response)
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def retrieve_billing(self, config: Config, request_code: str) -> RetrievedBilling:
        """
        Retrieves billing details based on the provided request code.

        Args:
            config (Config): The configuration object containing client information.
            request_code (str): The unique identifier for the billing request to be retrieved.

        Returns:
            RetrievedBilling: An object containing the details of the requested billing.

        Raises:
            SdkException: If there is an error during the retrieval process, such as
                          network issues or API response errors.
        """
        logging.info("RetrieveIssue {} requestCode={}".format(config.client_id, request_code))
        
        url = UrlUtils.build_url(config, Constants.URL_BILLING) + f"/{request_code}"
        
        json_response = HttpUtils.call_get(config, url, Constants.BILLET_BILLING_READ_SCOPE, "Error retrieving billing")
        try:
            return RetrievedBilling.from_dict(json_response)
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise
    def retrieve_billing_page(self, config: Config, initial_date: str, final_date: str, page: int, page_size: int, filter: BillingRetrievalFilter, sort: Sorting) -> BillingPage:
        """
        Retrieves a page of billing records based on the specified parameters.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date for the retrieval range (inclusive).
            final_date (str): The end date for the retrieval range (inclusive).
            page (int): The page number to retrieve.
            page_size (Optional[int]): The number of items per page (optional).
            filter (Optional[BillingRetrievalFilter]): Optional filters to be applied to the billing retrieval.
            sort (Optional[Sorting]): Optional sorting criteria for the billing retrieval.

        Returns:
            BillingPage: An object containing the requested page of billing records.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                          or API response errors.
        """
        logging.info("RetrieveBillingCollection {} {}-{}".format(config.client_id, initial_date, final_date))
        
        return self.get_page(config, initial_date, final_date, page, page_size, filter, sort)

    def retrieve_billing_in_range(self, config: Config, initial_date: str, final_date: str, filter: BillingRetrievalFilter, sort: Sorting) -> List[RetrievedBilling]:
        """
        Retrieves all billing records within the specified date range, applying the given filters and sorting.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date for the retrieval range (inclusive).
            final_date (str): The end date for the retrieval range (inclusive).
            filter (Optional[BillingRetrievalFilter]): Optional filters to be applied to the billing retrieval.
            sort (Optional[Sorting]): Optional sorting criteria for the billing retrieval.

        Returns:
            List[RetrievedBilling]: A list of objects containing all billing records within the specified date range.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                          or API response errors.
        """
        logging.info("RetrieveBillingCollection {} {}-{}".format(config.client_id, initial_date, final_date))
        page = 0
        billing_records = []
        
        while True:
            billing_page = self.get_page(config, initial_date, final_date, page, None, filter, sort)
            billing_records.extend(billing_page.billings)
            if page >= billing_page.total_pages:
                break
            page += 1
            
        return billing_records

    def retrieve_billing_in_pdf(self, config: Config, request_code: str, file_path: str) -> None:
        """
        Retrieves the billing PDF identified by the provided request code and saves it to a specified file.

        Args:
            config (Config): The configuration object containing client information.
            request_code (str): The unique identifier for the billing request whose PDF is to be retrieved.
            file_path (str): The file path where the PDF document will be saved.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                          or API response errors.
        """
        logging.info("RetrieveBillingPdf {} requestCode={}".format(config.client_id, request_code))
        
        url = UrlUtils.build_url(config, Constants.URL_BILLING) + f"/{request_code}/pdf"
        
        json_response = HttpUtils.call_get(config, url, Constants.BILLET_BILLING_READ_SCOPE, "Error retrieving billing pdf")
        try:
            pdf_return = PdfReturn.from_dict(json_response)
            decoded_bytes = base64.b64decode(pdf_return.pdf)
            
            with open(file_path, 'wb') as stream:
                stream.write(decoded_bytes)
                
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def retrieve_billing_summary(self, config: Config, initial_date: str, final_date: str, filter: BillingRetrievalFilter) -> List[SummaryItem]:
        """
        Retrieves a summary of billing records within a specified date range and optional filters.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date for the retrieval range (inclusive).
            final_date (str): The end date for the retrieval range (inclusive).
            filter (Optional[BillingRetrievalFilter]): Optional filters to be applied to the billing summary retrieval.

        Returns:
            Summary: An object containing the billing summary details.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                          or API response errors.
        """
        logging.info("RetrieveBillingSummary {} {}-{}".format(config.client_id, initial_date, final_date))
        
        url = f"{UrlUtils.build_url(config, Constants.URL_BILLING_SUMMARY)}?dataInicial={initial_date}&dataFinal={final_date}{self.add_filters(filter)}"
        
        json_response = HttpUtils.call_get(config, url, Constants.BILLET_BILLING_READ_SCOPE, "Error retrieving billing summary")
        try:
            return [SummaryItem.from_dict(item) for item in json_response]
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def get_page(self, config: Config, initial_date: str, final_date: str, page: int, page_size: int, filter: BillingRetrievalFilter, sort: Sorting) -> BillingPage:
        """
        Retrieves a specific page of billing records based on the specified parameters.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date for the retrieval range (inclusive).
            final_date (str): The end date for the retrieval range (inclusive).
            page (int): The page number to retrieve.
            page_size (Optional[int]): The number of items per page (optional).
            filter (Optional[BillingRetrievalFilter]): Optional filters to be applied to the billing retrieval.
            sort (Optional[Sorting]): Optional sorting criteria for the billing retrieval.

        Returns:
            BillingPage: An object containing the requested page of billing records.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                          or API response errors.
        """
        url = f"{UrlUtils.build_url(config, Constants.URL_BILLING)}?dataInicial={initial_date}&dataFinal={final_date}&paginacao.paginaAtual={page}"
        if page_size is not None:
            url += f"&paginacao.itensPorPagina={page_size}"
        url += self.add_filters(filter) + self.add_sort(sort)

        json_response = HttpUtils.call_get(config, url, Constants.BILLET_BILLING_READ_SCOPE, "Error retrieving billing collection")
        try:
            return BillingPage.from_dict(json_response)
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def add_filters(self, filter: BillingRetrievalFilter) -> str:
        """
        Constructs the query string for filters to be applied when retrieving billing records.

        Args:
            filter (Optional[BillingRetrievalFilter]): The filter object containing filtering criteria.

        Returns:
            str: A query string that can be appended to the URL for filtering.
        """
        if filter is None:
            return ""

        string_filter = []
        if filter.filter_date_by is not None:
            string_filter.append(f"&filtrarDataPor={filter.filter_date_by}")
        if filter.situation is not None:
            string_filter.append(f"&situacao={filter.situation}")
        if filter.payer is not None:
            string_filter.append(f"&pessoaPagadora={filter.payer}")
        if filter.payer_cpf_cnpj is not None:
            string_filter.append(f"&cpfCnpjPessoaPagadora={filter.payer_cpf_cnpj}")
        if filter.your_number is not None:
            string_filter.append(f"&seuNumero={filter.your_number}")
        if filter.billing_type is not None:
            string_filter.append(f"&tipoCobranca={filter.billing_type}")

        return ''.join(string_filter)

    def add_sort(self, sort: Sorting) -> str:
        """
        Constructs the query string for sorting to be applied when retrieving billing records.

        Args:
            sort (Optional[Sorting]): The sorting object containing sorting criteria.

        Returns:
            str: A query string that can be appended to the URL for sorting.
        """
        if sort is None:
            return ""

        order = []
        if sort.order_by is not None:
            order.append(f"&ordenarPor={sort.order_by}")
        if sort.sort_type is not None:
            order.append(f"&tipoOrdenacao={sort.sort_type}")

        return ''.join(order)