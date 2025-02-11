import json
import logging
from typing import List

from inter_sdk_python.commons.models.Config import Config
from inter_sdk_python.commons.structures.Constants import Constants
from inter_sdk_python.commons.utils.HttpUtils import HttpUtils
from inter_sdk_python.commons.utils.UrlUtils import UrlUtils
from inter_sdk_python.pix.models.DetailedDevolution import DetailedDevolution
from inter_sdk_python.pix.models.DevolutionRequestBody import DevolutionRequestBody
from inter_sdk_python.pix.models.Pix import Pix
from inter_sdk_python.pix.models.PixPage import PixPage
from inter_sdk_python.pix.models.RetrievedPixFilter import RetrievedPixFilter


class PixClient:
    def request_devolution(
        self, 
        config: Config, 
        e2e_id: str, 
        id: str, 
        devolution_request_body: DevolutionRequestBody
    ) -> DetailedDevolution:
        """
        Requests a devolution for a transaction identified by its end-to-end ID and the specific ID.

        Args:
            config (Config): The configuration object containing client information.
            e2e_id (str): The end-to-end ID of the transaction for which the devolution is being requested.
            id (str): The unique identifier for the devolution request.
            devolution_request_body (DevolutionRequestBody): An object containing details for the devolution request.

        Returns:
            DetailedDevolution: An object containing details about the requested devolution.

        Raises:
            SdkException: If there is an error during the request process, such as network issues
                           or API response errors.
        """
        logging.info("RequestDevolution {} e2eId={} id={}".format(config.client_id, e2e_id, id))
        
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_PIX)}/{e2e_id}/devolucao/{id}"
        
        try:
            json_data = json.dumps(devolution_request_body.to_dict(), indent=4)
            json_response = HttpUtils.call_put(config, url, Constants.PIX_WRITE_SCOPE, "Error requesting devolution", json_data)
            return DetailedDevolution.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise
        
    def retrieve_devolution(self, config: Config, e2e_id: str, id: str) -> DetailedDevolution:
        """
        Retrieves the details of a devolution based on the provided end-to-end ID and specific ID.

        Args:
            config (Config): The configuration object containing client information.
            e2e_id (str): The end-to-end ID of the transaction for which the devolution details are requested.
            id (str): The unique identifier for the devolution to be retrieved.

        Returns:
            DetailedDevolution: An object containing the details of the retrieved devolution.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveDevolution {} e2eId={} id={}".format(config.client_id, e2e_id, id))
        
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_PIX)}/{e2e_id}/devolucao/{id}"
        json_response = HttpUtils.call_get(config, url, Constants.PIX_READ_SCOPE, "Error retrieving devolution")
        
        try:
            return DetailedDevolution.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise
        
    def retrieve_pix_transaction(self, config: Config, e2e_id: str) -> Pix:
        """
        Retrieves the details of a Pix transaction based on the provided end-to-end ID.

        Args:
            config (Config): The configuration object containing client information.
            e2e_id (str): The end-to-end ID of the Pix transaction to be retrieved.

        Returns:
            Pix: An object containing the details of the retrieved Pix transaction.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrievePix {} e2eId={}".format(config.client_id, e2e_id))
        
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_PIX)}/{e2e_id}"
        json_response = HttpUtils.call_get(config, url, Constants.PIX_READ_SCOPE, "Error retrieving pix")
        
        try:
            return Pix.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise
        
    def retrieve_pix_page(
        self, 
        config: Config, 
        initial_date: str, 
        final_date: str, 
        page: int, 
        page_size: int, 
        filter: RetrievedPixFilter
    ) -> PixPage:
        """
        Retrieves a paginated list of Pix transactions based on the specified date range, page number, and filters.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date for the retrieval range (inclusive).
            final_date (str): The end date for the retrieval range (inclusive).
            page (int): The page number to retrieve.
            page_size (int): The number of items per page.
            filter (RetrievedPixFilter): An object containing filter criteria.

        Returns:
            PixPage: An object containing the requested page of Pix transactions.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrievePixList {} {}-{} page={}".format(config.client_id, initial_date, final_date, page))
        
        return self.get_page(config, initial_date, final_date, page, page_size, filter)
    
    def retrieve_pix_list_in_range(
        self, 
        config: Config, 
        initial_date: str, 
        final_date: str, 
        filter: RetrievedPixFilter
    ) -> List[Pix]:
        """
        Retrieves all Pix transactions within the specified date range and filters.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date for the retrieval range (inclusive).
            final_date (str): The end date for the retrieval range (inclusive).
            filter (RetrievedPixFilter): An object containing filter criteria.

        Returns:
            List[Pix]: A list of objects containing all retrieved Pix transactions.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrievePixList {} {}-{}".format(config.client_id, initial_date, final_date))
        
        page = 0
        pix_list = []

        while True:
            pix_page = self.get_page(config, initial_date, final_date, page, None, filter)
            pix_list.extend(pix_page.pix_list)
            page += 1
            if page >= pix_page.total_pages:
                break
        
        return pix_list
    
    def get_page(
        self, 
        config: Config, 
        initial_date: str, 
        final_date: str, 
        page: int, 
        page_size: int, 
        filter: RetrievedPixFilter = None
    ) -> PixPage:
        """
        Retrieves a specific page of Pix transactions based on the provided criteria.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date for the retrieval range (inclusive).
            final_date (str): The end date for the retrieval range (inclusive).
            page (int): The page number to retrieve.
            page_size (int): The number of items per page.
            filter (RetrievedPixFilter): An object containing filter criteria.

        Returns:
            PixPage: An object containing the requested page of Pix transactions.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_PIX)}?inicio={initial_date}&fim={final_date}&paginacao.paginaAtual={page}"
        
        if page_size is not None:
            url += f"&paginacao.itensPorPagina={page_size}"
        
        if filter is not None:
            url += self.add_filters(filter)
        
        json_response = HttpUtils.call_get(config, url, Constants.PIX_READ_SCOPE, "Error retrieving pix")
        
        try:
            return PixPage.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise
        
    def add_filters(self, filter: RetrievedPixFilter) -> str:
        """
        Adds filter parameters to the URL based on the provided filter criteria.

        Args:
            filter (RetrievedPixFilter): An object containing filter criteria.

        Returns:
            str: A string containing the appended filter parameters for the URL.
        """
        if filter is None:
            return ""
        
        string_filter = []

        if filter.tx_id is not None:
            string_filter.append(f"&txId={filter.tx_id}")
        if filter.tx_id_present is not None:
            string_filter.append(f"&txIdPresente={filter.tx_id_present}")
        if filter.devolution_present is not None:
            string_filter.append(f"&devolucaoPresente={filter.devolution_present}")
        if filter.cpf is not None:
            string_filter.append(f"&cpf={filter.cpf}")
        if filter.cnpj is not None:
            string_filter.append(f"&cnpj={filter.cnpj}")

        return ''.join(string_filter)