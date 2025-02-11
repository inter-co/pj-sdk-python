import json
import logging
from typing import List

from inter_sdk_python.commons.models.Config import Config
from inter_sdk_python.commons.structures.Constants import Constants
from inter_sdk_python.commons.utils.HttpUtils import HttpUtils
from inter_sdk_python.commons.utils.UrlUtils import UrlUtils
from inter_sdk_python.pix.models.DueBillingBatch import DueBillingBatch
from inter_sdk_python.pix.models.DueBillingBatchPage import DueBillingBatchPage
from inter_sdk_python.pix.models.DueBillingBatchSummary import DueBillingBatchSummary
from inter_sdk_python.pix.models.IncludeDueBillingBatchRequest import IncludeDueBillingBatchRequest


class DueBillingBatchClient:
    def include_due_billing_batch(self, config: Config, batch_id: str, request: IncludeDueBillingBatchRequest) -> None:
        """
        Includes a batch request for due billing based on the provided configuration,
        batch ID, and request details.

        Args:
            config (Config): The configuration object containing client information.
            batch_id (str): The unique identifier for the batch of due billings to be included.
            request (IncludeDueBillingBatchRequest): The object containing the details
                                                     of the due billing batch request to be included.

        Raises:
            SdkException: If there is an error during the inclusion process, such as network issues
                           or API response errors.
        """
        logging.info("IncludeDueBillingBatch {} {}".format(config.client_id, request))
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_SCHEDULED_BILLINGS_BATCH)}/{batch_id}"
        
        try:
            json_data = request.to_json()
            HttpUtils.call_put(config, url, Constants.PIX_SCHEDULED_BILLING_BATCH_WRITE_SCOPE, "Error including due billing in batch", json_data)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def retrieve_due_billing_batch(self, config: Config, batch_id: str) -> DueBillingBatch:
        """
        Retrieves a due billing batch based on the provided configuration and batch ID.

        Args:
            config (Config): The configuration object containing client information.
            batch_id (str): The unique identifier for the due billing batch to be retrieved.

        Returns:
            DueBillingBatch: An object containing the details of the retrieved due billing batch.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveDueBillingBatch {} id={}".format(config.client_id, batch_id))
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_SCHEDULED_BILLINGS_BATCH)}/{batch_id}"
        
        json_response = HttpUtils.call_get(config, url, Constants.PIX_SCHEDULED_BILLING_BATCH_READ_SCOPE, "Error retrieving due billing batch")
        
        try:
            return DueBillingBatch.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def retrieve_due_billing_batch_page(
        self, 
        config: Config, 
        initial_date: str, 
        final_date: str, 
        page: int, 
        page_size: int
    ) -> DueBillingBatchPage:
        """
        Retrieves a paginated list of due billing batches based on the specified date range and page number.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date for the retrieval range (inclusive).
            final_date (str): The end date for the retrieval range (inclusive).
            page (int): The page number to retrieve.
            page_size (Optional[int]): The number of items per page (optional).

        Returns:
            DueBillingBatchPage: An object containing the requested page of due billing batches.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveDueBillingBatchList {} {}-{} page={}".format(config.client_id, initial_date, final_date, page))
        return self.get_page(config, initial_date, final_date, page, page_size)

    def retrieve_due_billing_batches_in_range(
        self, 
        config: Config, 
        initial_date: str, 
        final_date: str
    ) -> List[DueBillingBatch]:
        """
        Retrieves all due billing batches within the specified date range.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date for the retrieval range (inclusive).
            final_date (str): The end date for the retrieval range (inclusive).

        Returns:
            List[DueBillingBatch]: A list of objects containing all retrieved billing batches.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveDueBillingBatchList {} {}-{}".format(config.client_id, initial_date, final_date))
        page = 0
        batches = []

        while True:
            due_billing_page = self.get_page(config, initial_date, final_date, page, None)
            batches.extend(due_billing_page.batches)
            page += 1
            if page >= due_billing_page.total_pages:
                break

        return batches

    def review_due_billing_batch(self, config: Config, batch_id: str, request: IncludeDueBillingBatchRequest) -> None:
        """
        Reviews a due billing batch based on the provided configuration, batch ID, and review request details.

        Args:
            config (Config): The configuration object containing client information.
            batch_id (str): The unique identifier for the due billing batch to be reviewed.
            request (IncludeDueBillingBatchRequest): The object containing the details to update the review.

        Raises:
            SdkException: If there is an error during the review process, such as network issues
                           or API response errors.
        """
        logging.info("IncludeDueBillingBatch {} {}".format(config.client_id, request))
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_SCHEDULED_BILLINGS_BATCH)}/{batch_id}"
        
        try:
            json_data = request.to_json()
            HttpUtils.call_patch(config, url, Constants.PIX_SCHEDULED_BILLING_BATCH_WRITE_SCOPE, "Error reviewing due billing in batch", json_data)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def retrieve_due_billing_batch_summary(self, config: Config, batch_id: str) -> DueBillingBatchSummary:
        """
        Retrieves the summary of a due billing batch based on the provided configuration and batch ID.

        Args:
            config (Config): The configuration object containing client information.
            batch_id (str): The unique identifier for the due billing batch to be retrieved.

        Returns:
            DueBillingBatchSummary: An object containing the summary details of the retrieved due billing batch.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        logging.info("RetrieveDueBillingBatch {} id={}".format(config.client_id, batch_id))
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_SCHEDULED_BILLINGS_BATCH)}/{batch_id}/sumario"
        
        json_response = HttpUtils.call_get(config, url, Constants.PIX_SCHEDULED_BILLING_BATCH_READ_SCOPE, "Error retrieving due billing batch summary")
        
        try:
            return DueBillingBatchSummary.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def retrieve_due_billing_batch_by_situation(
        self, 
        config: Config, 
        batch_id: str, 
        situation: str
    ) -> DueBillingBatch:
        """
        Retrieves a due billing batch identified by the specified ID and situation.
        This method constructs a URL using the provided configuration, ID, and situation,
        performs a GET request to retrieve the corresponding due billing batch,
        and maps the JSON response to a DueBillingBatch object.

        Args:
            config (Config): The configuration object containing client information for making the request.
            batch_id (str): The unique identifier of the due billing batch to retrieve.
            situation (str): The situation status to filter the due billing batch.

        Returns:
            DueBillingBatch: An object representing the retrieved billing batch.

        Raises:
            SdkException: If an error occurs while making the HTTP request or processing the response.
                           This includes issues related to network access, invalid responses,
                           and JSON mapping errors.
        """
        logging.info("RetrieveDueBillingBatchSituation {} id={}".format(config.client_id, batch_id))
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_SCHEDULED_BILLINGS_BATCH)}/{batch_id}/situacao/{situation}"
        
        json_response = HttpUtils.call_get(config, url, Constants.PIX_SCHEDULED_BILLING_BATCH_READ_SCOPE, "Error retrieving due billing batch by situation")
        
        try:
            return DueBillingBatch.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def get_page(
        self, 
        config: Config, 
        initial_date: str, 
        final_date: str, 
        page: int, 
        page_size: int
    ) -> DueBillingBatchPage:
        """
        Retrieves a specific page of due billing batches based on the provided criteria.

        Args:
            config (Config): The configuration object containing client information.
            initial_date (str): The start date for the retrieval range (inclusive).
            final_date (str): The end date for the retrieval range (inclusive).
            page (int): The page number to retrieve.
            page_size (Optional[int]): The number of items per page (optional).

        Returns:
            DueBillingBatchPage: An object containing the requested page of due billing batches.

        Raises:
            SdkException: If there is an error during the retrieval process, such as network issues
                           or API response errors.
        """
        url = f"{UrlUtils.build_url(config, Constants.URL_PIX_SCHEDULED_BILLINGS_BATCH)}?inicio={initial_date}&fim={final_date}&paginacao.paginaAtual={page}"
        
        if page_size is not None:
            url += f"&paginacao.itensPorPagina={page_size}"
        
        json_response = HttpUtils.call_get(config, url, Constants.PIX_SCHEDULED_BILLING_BATCH_READ_SCOPE, "Error retrieving due billing batch")
        
        try:
            return DueBillingBatchPage.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise