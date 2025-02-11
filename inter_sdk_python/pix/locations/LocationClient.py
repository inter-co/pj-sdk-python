import json
import logging
from typing import List

from inter_sdk_python.commons.models.Config import Config
from inter_sdk_python.commons.structures.Constants import Constants
from inter_sdk_python.commons.utils.HttpUtils import HttpUtils
from inter_sdk_python.commons.utils.UrlUtils import UrlUtils
from inter_sdk_python.pix.enums.ImmediateBillingType import ImmediateBillingType
from inter_sdk_python.pix.models.Location import Location
from inter_sdk_python.pix.models.LocationPage import LocationPage
from inter_sdk_python.pix.models.RetrieveLocationFilter import RetrieveLocationFilter


class LocationClient:
    def include_location(self, config: Config, immediate_billing_type: ImmediateBillingType) -> Location:
        """
        Includes a new location based on the provided configuration and immediate billing type.

        Args:
            config (Config): The configuration object containing client information.
            immediate_billing_type (ImmediateBillingType): The type of immediate billing.

        Returns:
            Location: An object containing the details of the included location.

        Raises:
            SdkException: If there is an error during the inclusion process, such as network issues
                           or API response errors.
        """
        logging.info("IncludeLocation pix {} {}".format(config.client_id, immediate_billing_type))
        
        url = UrlUtils.build_url(config, Constants.URL_PIX_LOCATIONS)
        request = {"tipoCob": immediate_billing_type.name}

        try:
            json_data = json.dumps(request, indent=4)
            json_response = HttpUtils.call_post(config, url, Constants.PIX_LOCATION_WRITE_SCOPE, "Error including location", json_data)
            return Location.from_dict(json_response)

        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise
        
    def retrieve_location(self, config: Config, id: str) -> Location:
        """
        Retrieves the details of a location based on the provided configuration and location ID.

        Args:
            config (Config): The configuration object containing client information.
            id (str): The unique identifier for the location to be retrieved.

        Returns:
            Location: An object containing the details of the retrieved location.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveLocation {} id={}".format(config.client_id, id))
        
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_LOCATIONS)}/{id}"
        json_response = HttpUtils.call_get(config, url, Constants.PIX_LOCATION_READ_SCOPE, "Error retrieving location")
        
        try:
            return Location.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise
        
    def retrieve_location_page(
        self, 
        config: Config, 
        initial_date: str, 
        final_date: str, 
        page: int, 
        page_size: int, 
        filter: RetrieveLocationFilter
    ) -> LocationPage:
        """
        Retrieves a paginated list of locations based on the specified date range, page number, and filters.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date for the retrieval range (inclusive).
            final_date (str): The end date for the retrieval range (inclusive).
            page (int): The page number to retrieve.
            page_size (Optional[int]): The number of items per page (optional).
            filter (RetrieveLocationFilter): An object containing filter criteria.

        Returns:
            LocationPage: An object containing the requested page of locations.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveLocationsList {} {}-{} pagina={}".format(config.client_id, initial_date, final_date, page))
        
        return self.get_page(config, initial_date, final_date, page, page_size, filter)
    
    def retrieve_location_in_range(
        self, 
        config: Config, 
        initial_date: str, 
        final_date: str, 
        filter: RetrieveLocationFilter
    ) -> List[Location]:
        """
        Retrieves all locations within the specified date range and filters.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date for the retrieval range (inclusive).
            final_date (str): The end date for the retrieval range (inclusive).
            filter (RetrieveLocationFilter): An object containing filter criteria.

        Returns:
            List[Location]: A list of objects containing all retrieved locations.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveLocationsList {} {}-{}".format(config.client_id, initial_date, final_date))
        
        page = 0
        locs = []
        location_page = None

        while True:
            location_page = self.get_page(config, initial_date, final_date, page, None, filter)
            locs.extend(location_page.locations)
            page += 1
            if page >= location_page.total_pages:
                break
        
        return locs
    
    def unlink_location(self, config: Config, id: str) -> Location:
        """
        Unlinks a location based on the provided configuration and location ID.

        Args:
            config (Config): The configuration object containing client information.
            id (str): The unique identifier for the location to be unlinked.

        Returns:
            Location: An object confirming the unlinking of the location.

        Raises:
            SdkException: If there is an error during the unlinking process, such as network issues
                           or API response errors.
        """
        logging.info("UnlinkLocation {} id={}".format(config.client_id, id))
        
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_LOCATIONS)}/{id}/txid"
        json_response = HttpUtils.call_delete(config, url, Constants.PIX_LOCATION_WRITE_SCOPE, "Error unlinking location")
        
        try:
            return Location.from_dict(json_response)
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
        filter: RetrieveLocationFilter
    ) -> LocationPage:
        """
        Retrieves a specific page of locations based on the provided criteria.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date for the retrieval range (inclusive).
            final_date (str): The end date for the retrieval range (inclusive).
            page (int): The page number to retrieve.
            page_size (Optional[int]): The number of items per page (optional).
            filter (RetrieveLocationFilter): An object containing filter criteria.

        Returns:
            LocationPage: An object containing the requested page of locations.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_LOCATIONS)}?inicio={initial_date}&fim={final_date}&paginacao.paginaAtual={page}"
        
        if page_size is not None:
            url += f"&paginacao.itensPorPagina={page_size}"
        
        if filter is not None:
            url += self.add_filters(filter)
        
        json_response = HttpUtils.call_get(config, url, Constants.PIX_LOCATION_READ_SCOPE, "Error retrieving locations")
        
        try:
            return LocationPage.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise
        
    def add_filters(self, filter: RetrieveLocationFilter) -> str:
        """
        Adds filter parameters to the URL based on the provided filter criteria.

        Args:
            filter (RetrieveLocationFilter): An object containing filter criteria.

        Returns:
            str: A string containing the appended filter parameters for the URL.
        """
        if filter is None:
            return ""
        
        string_filter = []

        if filter.tx_id_present is not None:
            string_filter.append(f"&txIdPresente={filter.tx_id_present}")
        if filter.billing_type is not None:
            string_filter.append(f"&tipoCob={filter.billing_type}")

        return ''.join(string_filter)
