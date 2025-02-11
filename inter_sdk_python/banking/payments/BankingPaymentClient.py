import logging
from typing import Optional, List

from inter_sdk_python.banking.models.Batch import Batch, BilletBatch, DarfPaymentBatch
from inter_sdk_python.banking.models.BatchItem import BatchItem
from inter_sdk_python.banking.models.BatchProcessing import BatchProcessing
from inter_sdk_python.banking.models.BilletPayment import BilletPayment
from inter_sdk_python.banking.models.DarfPayment import DarfPayment
from inter_sdk_python.banking.models.DarfPaymentResponse import DarfPaymentResponse
from inter_sdk_python.banking.models.DarfPaymentSearchFilter import DarfPaymentSearchFilter
from inter_sdk_python.banking.models.IncludeBatchPaymentResponse import IncludeBatchPaymentResponse
from inter_sdk_python.banking.models.IncludeDarfPaymentResponse import IncludeDarfPaymentResponse
from inter_sdk_python.banking.models.IncludePaymentResponse import IncludePaymentResponse
from inter_sdk_python.banking.models.Payment import Payment
from inter_sdk_python.banking.models.PaymentSearchFilter import PaymentSearchFilter
from inter_sdk_python.commons.models.Config import Config
from inter_sdk_python.commons.structures.Constants import Constants
from inter_sdk_python.commons.utils.HttpUtils import HttpUtils
from inter_sdk_python.commons.utils.UrlUtils import UrlUtils


class BankingPaymentClient:
    def cancel(self, config: Config, transaction_code: str) -> None:
        """
        Cancels a scheduled payment based on the provided transaction code.

        This method constructs the URL to cancel the payment scheduling
        using the client's configuration and the transaction code. It logs 
        the cancellation request and handles any exceptions that may arise 
        during the HTTP call to the banking API.

        Args:
            config (Config): The configuration object containing the client's details and environment settings.
            transaction_code (str): The unique code associated with the transaction that is to be canceled.

        Raises:
            SdkException: If an error occurs during the cancellation process,
                          such as issues with the HTTP request or response.
        """
        logging.info("CancelPaymentScheduling banking {} {}".format(config.client_id, transaction_code))
        url = f"{UrlUtils.build_url(config, Constants.URL_BANKING_PAYMENT)}/{transaction_code}"
        
        HttpUtils.call_delete(config, url, Constants.BILLET_PAYMENT_WRITE_SCOPE, "Error canceling payment scheduling")

    def include_batch_payment(self, config: Config, my_identifier: str, payments: List[BatchItem]) -> IncludeBatchPaymentResponse:
        """
        Includes a list of payments in a batch using the provided configuration and identifier.

        This method logs the inclusion operation and constructs a JSON representation
        of the batch payment request. It sends this request to the banking API and
        returns the response as an IncludeBatchPaymentResponse object.
        In case of errors during processing, an SdkException is thrown.

        Args:
            config (Config): The configuration object containing the client's details and environment settings.
            my_identifier (str): A unique identifier for the batch payment.
            payments (List[BatchItem]): A list of BatchItem objects representing the payments to be included in the batch.

        Returns:
            IncludeBatchPaymentResponse: An object that contains the response from the banking API regarding the batch inclusion.

        Raises:
            SdkException: If an error occurs while including the payments, such as issues with the HTTP request or response.
        """
        logging.info("IncludeBatchPayment banking {} {} {}".format(config.client_id, my_identifier, len(payments)))
        url = UrlUtils.build_url(config, Constants.URL_BANKING_PAYMENT_BATCH)
        
        request = Batch(my_identifier=my_identifier, payments=payments)
        
        try:
            json_request = request.to_json()
            json_response = HttpUtils.call_post(config, url, Constants.BATCH_PAYMENT_WRITE_SCOPE, "Error including payment in batch", json_request)
            return IncludeBatchPaymentResponse.from_dict(json_response)
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def include_darf_payment(self, config: Config, pagamento: DarfPayment) -> IncludeDarfPaymentResponse:
        """
        Includes a DARF payment request using the provided configuration and payment data.

        This method logs the inclusion operation and converts the DARF payment object
        into a JSON string. It sends the request to the banking API and returns the
        response as an IncludeDarfPaymentResponse object. In the event of an
        error during processing, an SdkException is thrown.

        Args:
            config (Config): The configuration object containing the client's details and environment settings.
            pagamento (DarfPayment): The DarfPayment object containing the payment details to be included in the request.

        Returns:
            IncludeDarfPaymentResponse: An object that contains the response from the banking API regarding the DARF payment inclusion.

        Raises:
            SdkException: If an error occurs while including the DARF payment, such as issues with the HTTP request or response.
        """
        logging.info("IncludeDarfPayment banking {} {}".format(config.client_id, pagamento.revenue_code))
        url = UrlUtils.build_url(config, Constants.URL_BANKING_PAYMENT_DARF)
        
        try:
            json_request = pagamento.to_json()
            json_response = HttpUtils.call_post(config, url, Constants.DARF_PAYMENT_WRITE_SCOPE, "Error including DARF payment", json_request)
            return IncludeDarfPaymentResponse.from_dict(json_response)
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def include_billet_payment(self, config: Config, payment: BilletPayment) -> IncludePaymentResponse:
        """
        Includes a billet payment request using the provided configuration and payment data.

        This method logs the inclusion operation and converts the billet payment object
        into a JSON string. It sends the request to the banking API and returns the
        response as an IncludePaymentResponse object. In case of errors during
        processing, an SdkException is thrown.

        Args:
            config (Config): The configuration object containing the client's details and environment settings.
            payment (BilletPayment): The BilletPayment object containing the payment details to be included in the request.

        Returns:
            IncludePaymentResponse: An object that contains the response from the banking API regarding the billet payment inclusion.

        Raises:
            SdkException: If an error occurs while including the billet payment, such as issues with the HTTP request or response.
        """
        logging.info("IncludePayment {} {}".format(config.client_id, payment.barcode))
        url = UrlUtils.build_url(config, Constants.URL_BANKING_PAYMENT)
        
        try:
            json_request = payment.to_json()
            json_response = HttpUtils.call_post(config, url, Constants.BILLET_PAYMENT_WRITE_SCOPE, "Error including payment", json_request)
            return IncludePaymentResponse.from_dict(json_response)
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def retrieve_darf_list(self, config: Config, initial_date: str, final_date: str, filtro: DarfPaymentSearchFilter) -> List[DarfPaymentResponse]:
        """
        Retrieves a list of DARF payments based on the specified date range and filters.

        This method constructs the request URL using the client configuration, initial
        and final dates, and any additional filters provided. It sends the request to
        the banking API and returns the list of DARF payment responses.
        In the event of an error during processing, an SdkException is thrown.

        Args:
            config (Config): The configuration object containing the client's details and environment settings.
            initial_date (str): The starting date for the payment retrieval in the format accepted by the API (e.g. "YYYY-MM-DD").
            final_date (str): The ending date for the payment retrieval in the same format as above.
            filtro (Optional[DarfPaymentSearchFilter]): An optional object that contains additional search criteria.

        Returns:
            List[DarfPaymentResponse]: A list of objects representing the retrieved DARF payments.

        Raises:
            SdkException: If an error occurs while retrieving the DARF payments,
                          such as issues with the HTTP request or response.
        """
        logging.info("RetrieveDarfPayments banking {} {}-{}".format(config.client_id, initial_date, final_date))
        url = f"{UrlUtils.build_url(config, Constants.URL_BANKING_PAYMENT_DARF)}?dataInicio={initial_date}&dataFim={final_date}{self.add_darf_filters(filtro)}"
        
        json_response = HttpUtils.call_get(config, url, Constants.BILLET_PAYMENT_READ_SCOPE, "Error retrieving DARF payment")
        try:
            return [DarfPaymentResponse.from_dict(item) for item in json_response]
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def retrieve_payment_batch(self, config: Config, batch_id: str) -> BatchProcessing:
        """
        Retrieves payment batch details for a given batch ID.

        This method logs the retrieval operation and constructs the request URL using
        the provided configuration and batch ID. It processes the JSON response,
        extracting relevant payment information and returning it as a BatchProcessing object.
        In case of errors during processing, an SdkException is thrown.

        Args:
            config (Config): The configuration object containing the client's details and environment settings.
            batch_id (str): The unique identifier for the batch of payments to be retrieved.

        Returns:
            BatchProcessing: An object that contains the details of the payment batch along with the individual payments.

        Raises:
            SdkException: If an error occurs while retrieving the payment batch, such as issues with the HTTP request or response.
        """
        logging.info("RetrievePaymentBatch {} {}".format(config.client_id, batch_id))
        url = f"{UrlUtils.build_url(config, Constants.URL_BANKING_PAYMENT_BATCH)}/{batch_id}"
        json_response = HttpUtils.call_get(config, url, Constants.BATCH_PAYMENT_READ_SCOPE, "Error to retrieve batch")

        try:
            payments = []

            if "pagamentos" in json_response and json_response["pagamentos"]:
                for item in json_response["pagamentos"]:
                    payment_type = item.get("tipoPagamento")
                    if payment_type == "BILLET":
                        billet_batch = BilletBatch.from_dict(item)
                        payments.append(billet_batch)
                    else:
                        darf_batch = DarfPaymentBatch.from_dict(item)
                        payments.append(darf_batch)
                
                json_response["pagamentos"] = None

            batch_processing = BatchProcessing.from_dict(json_response)
            batch_processing.payments = payments
            return batch_processing
        except Exception as e:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=e)
            raise

    def retrieve_payment_list_in_range(self, config: Config, initial_date: str, final_date: str, filtro: PaymentSearchFilter) -> list[Payment]:
        """
        Retrieves a list of payments based on the specified date range and filters.

        This method constructs the request URL using the client configuration,
        initial and final dates, and any additional filters provided.
        It sends the request to the banking API and returns a list of
        Payment objects. In case of errors during processing,
        an SdkException is thrown.

        Args:
            config (Config): The configuration object containing the client's details and environment settings.
            initial_date (str): The starting date for the payment retrieval in the format accepted by the API (e.g. "YYYY-MM-DD").
            final_date (str): The ending date for the payment retrieval in the same format as above.
            filtro (Optional[PaymentSearchFilter]): An optional object that contains additional search criteria.

        Returns:
            List[Payment]: A list of objects representing the retrieved payments.

        Raises:
            SdkException: If an error occurs while retrieving the payments, such as issues with the HTTP request or response.
        """
        logging.info("RetrievePayments banking {} {}-{}".format(config.client_id, initial_date, final_date))
        url = f"{UrlUtils.build_url(config, Constants.URL_BANKING_PAYMENT)}?dataInicio={initial_date}&dataFim={final_date}{self.add_payment_filters(filtro)}"
        
        json_response = HttpUtils.call_get(config, url, Constants.BILLET_PAYMENT_READ_SCOPE, "Error retrieving payments")
        try:
            return [Payment.from_dict(item) for item in json_response]
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def add_darf_filters(self, filtro: DarfPaymentSearchFilter) -> str:
        """
        Adds filters to the request URL based on the provided DarfPaymentSearchFilter.

        This method builds query parameters from the filter object to be appended
        to the request URL. If no filters are provided, it returns an empty string.

        Args:
            filtro (Optional[DarfPaymentSearchFilter]): The filter object containing optional filter criteria.

        Returns:
            str: A string of query parameters representing the filters, or an empty string if no filters are set.
        """
        if filtro is None:
            return ""

        filter_params = []
        if filtro.request_code is not None:
            filter_params.append(f"&codigoTransacao={filtro.request_code}")
        if filtro.revenue_code is not None:
            filter_params.append(f"&codigoReceita={filtro.revenue_code}")
        if filtro.filter_date_by is not None:
            filter_params.append(f"&filtrarDataPor={filtro.filter_date_by}")

        return ''.join(filter_params)

    def add_payment_filters(self, filter: PaymentSearchFilter) -> str:
        """
        Adds filters to the request URL based on the provided PaymentSearchFilter.

        This method builds query parameters from the filter object to be appended
        to the request URL. If no filters are provided, it returns an empty string.

        Args:
            filter (Optional[PaymentSearchFilter]): The filter object containing optional filter criteria.

        Returns:
            str: A string of query parameters representing the filters, or an empty string if no filters are set.
        """
        if filter is None:
            return ""
        
        string_filter = []
        if filter.barcode is not None:
            string_filter.append(f"&codBarraLinhaDigitavel={filter.barcode}")
        if filter.transaction_code is not None:
            string_filter.append(f"&codigoTransacao={filter.transaction_code}")
        if filter.filter_date_by is not None:
            string_filter.append(f"&filtrarDataPor={filter.filter_date_by}")

        return ''.join(string_filter)
