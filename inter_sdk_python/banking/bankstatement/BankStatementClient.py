import base64
import json
import logging
from typing import List

from inter_sdk_python.banking.models.BankStatement import BankStatement
from inter_sdk_python.banking.models.EnrichedBankStatementPage import EnrichedBankStatementPage
from inter_sdk_python.banking.models.EnrichedTransaction import EnrichedTransaction
from inter_sdk_python.banking.models.FilterRetrieveEnrichedStatement import FilterRetrieveEnrichedStatement
from inter_sdk_python.commons.models.Config import Config
from inter_sdk_python.commons.models.PdfReturn import PdfReturn
from inter_sdk_python.commons.structures.Constants import Constants
from inter_sdk_python.commons.utils.HttpUtils import HttpUtils
from inter_sdk_python.commons.utils.UrlUtils import UrlUtils

class BankStatementClient:
    def retrieve_statement(self, config: Config, initial_date: str, final_date: str) -> BankStatement:
        """
        Retrieves the bank statement for a specified date range.

        Args:
            config (Config): The configuration object containing necessary parameters, such as client ID.
            initial_date (str): The start date for retrieving the bank statement in the appropriate format.
            final_date (str): The end date for retrieving the bank statement in the appropriate format.

        Returns:
            BankStatement: An instance of BankStatement containing the retrieved statement information.

        Raises:
            SdkException: If there is an error during the retrieval process or if the response format is incorrect.
        """
        logging.info("RetrieveBankStatement {} {}-{}".format(config.client_id, initial_date, final_date))
        url = UrlUtils.build_url(config, Constants.URL_BANKING_STATEMENT) + f"?dataInicio={initial_date}&dataFim={final_date}"

        json_response = HttpUtils.call_get(config, url, Constants.READ_BALANCE_SCOPE, "Error retrieving statement")
        
        try:
            return BankStatement.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def retrieve_statement_in_pdf(self, config: Config, initial_date: str, final_date: str, file: str) -> None:
        """
        Retrieves the bank statement in PDF format for a specified date range and saves it to a file.

        Args:
            config (Config): The configuration object containing necessary parameters such as client ID.
            initial_date (str): The start date for the bank statement period.
            final_date (str): The end date for the bank statement period.
            file (str): The path where the PDF file will be saved.

        Raises:
            SdkException: If an error occurs during the retrieval of the statement or if an error
                        occurs during the PDF decoding or file writing process.
        """
        logging.info("RetrieveBankStatementInPdf {} {}-{}".format(config.client_id, initial_date, final_date))
        
        url = UrlUtils.build_url(config, Constants.URL_BANKING_STATEMENT_PDF)
        url += f"?dataInicio={initial_date}&dataFim={final_date}"
        
        json_response = HttpUtils.call_get(config, url, Constants.READ_BALANCE_SCOPE, "Error retrieving statement in pdf")
        
        try:
            pdf_return = PdfReturn.from_dict(json_response)
            decoded_bytes = base64.b64decode(pdf_return.pdf)
            with open(file, 'wb') as stream:
                stream.write(decoded_bytes)
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def retrieve_statement_page(self, config: Config, initial_date: str, final_date: str, page: int, page_size: int, filter_retrieve: FilterRetrieveEnrichedStatement) -> \
            EnrichedBankStatementPage:
        """
        Retrieves a specific page of enriched bank statements within a given date range.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date of the statement range (inclusive).
            final_date (str): The end date of the statement range (inclusive).
            page (int): The page number to retrieve.
            page_size (Optional[int]): The number of items per page (optional).
            filter_retrieve (Optional[FilterRetrieveEnrichedStatement]): Optional filters for retrieving enriched bank statements.

        Returns:
            EnrichedBankStatementPage: An instance containing the requested page of enriched statements.

        Raises:
            SdkException: If there is an error during the retrieval process.
        """
        logging.info("RetrieveEnrichedBankStatement {} {}-{}".format(config.client_id, initial_date, final_date))
        statement_page = self.get_page(config, initial_date, final_date, page, page_size, filter_retrieve)
        return statement_page

    def retrieve_statement_with_range(self, config: Config, initial_date: str, final_date: str, filter_retrieve: FilterRetrieveEnrichedStatement) -> \
            list[EnrichedBankStatementPage]:
        """
        Retrieves a list of enriched transactions within a given date range.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date of the statement range (inclusive).
            final_date (str): The end date of the statement range (inclusive).
            filter_retrieve (Optional[FilterRetrieveEnrichedStatement]): Optional filters for retrieving enriched bank statements.

        Returns:
            List[EnrichedTransaction]: A list of all transactions within the date range.

        Raises:
            SdkException: If there is an error during the retrieval process.
        """
        logging.info("RetrieveEnrichedBankStatement {} {}-{}".format(config.client_id, initial_date, final_date))
        page = 0
        transactions = []
        
        while True:
            transaction_page = self.get_page(config, initial_date, final_date, page, None, filter_retrieve)
            transactions.extend(transaction_page.transactions)
            
            if page >= transaction_page.total_pages:
                break
            page += 1

        return transactions

    def get_page(self, config: Config, initial_date: str, final_date: str, page: int, page_size: int, filter_retrieve: FilterRetrieveEnrichedStatement) -> EnrichedBankStatementPage:
        """
        Retrieves a page of enriched bank statements based on the provided parameters.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date of the statement range (inclusive).
            final_date (str): The end date of the statement range (inclusive).
            page (int): The page number to retrieve.
            page_size (Optional[int]): The number of items per page (optional).
            filter_retrieve (Optional[FilterRetrieveEnrichedStatement]): Optional filters for retrieving enriched bank statements.

        Returns:
            EnrichedBankStatementPage: An instance containing the requested page of enriched statements.

        Raises:
            SdkException: If there is an error during the retrieval process.
        """
        url = UrlUtils.build_url(config, Constants.URL_BANKING_ENRICHED_STATEMENT)
        url += f"?dataInicio={initial_date}&dataFim={final_date}&pagina={page}"
        
        if page_size is not None:
            url += f"&tamanhoPagina={page_size}"
        
        url += self.add_filters(filter_retrieve)

        json_response = HttpUtils.call_get(config, url, Constants.READ_BALANCE_SCOPE, "Error retrieving enriched statement")
        
        try:
            return EnrichedBankStatementPage.from_dict(json_response)
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    @staticmethod
    def add_filters(filter_retrieve: FilterRetrieveEnrichedStatement) -> str:
        """
        Constructs the query string for filters to be applied when retrieving enriched bank statements.

        Args:
            filter_retrieve (FilterRetrieveEnrichedStatement): The filter object containing filtering criteria.

        Returns:
            str: A query string that can be appended to the URL for filtering.
        """
        if filter_retrieve is None:
            return ""
        
        string_filter = []
        
        if filter_retrieve.operation_type is not None:
            string_filter.append(f"&tipoOperacao={filter_retrieve.operation_type}")
        
        if filter_retrieve.transaction_type is not None:
            string_filter.append(f"&tipoTransacao={filter_retrieve.transaction_type}")
        
        return ''.join(string_filter)

