from typing import List

from inter_sdk_python.billing.billing.BillingClient import BillingClient
from inter_sdk_python.billing.models.BillingCallbackPage import BillingCallbackPage
from inter_sdk_python.billing.models.BillingIssueRequest import BillingIssueRequest
from inter_sdk_python.billing.models.BillingIssueResponse import BillingIssueResponse
from inter_sdk_python.billing.models.BillingPage import BillingPage
from inter_sdk_python.billing.models.BillingRetrievalFilter import BillingRetrievalFilter
from inter_sdk_python.billing.models.BillingRetrieveCallbackResponse import BillingRetrieveCallbackResponse
from inter_sdk_python.billing.models.BillingRetrieveCallbacksFilter import BillingRetrieveCallbacksFilter
from inter_sdk_python.billing.models.RetrievedBilling import RetrievedBilling
from inter_sdk_python.billing.models.Sorting import Sorting
from inter_sdk_python.billing.models.Summary import Summary
from inter_sdk_python.billing.models.SummaryItem import SummaryItem
from inter_sdk_python.billing.webhooks.BillingWebhookClient import BillingWebhookClient
from inter_sdk_python.commons.models.Config import Config
from inter_sdk_python.commons.models.Webhook import Webhook


class BillingSdk:
    def __init__(self, config: Config):
        self.config = config
        self.billing_client = None
        self.billing_webhook_client = None

    def cancel_billing(self, request_code: str, cancellation_reason: str) -> None:
        """
        Cancels a billing request specified by the request code.

        Args:
            request_code (str): The unique code identifying the billing request to be canceled.
            cancellation_reason (str): Reason for canceling the billing request.

        Raises:
            SdkException: If an error occurs during the cancellation process.
        """
        if self.billing_client is None:
            self.billing_client = BillingClient()
        
        self.billing_client.cancel_billing(self.config, request_code, cancellation_reason)

    def issue_billing(self, billing_issue_request: BillingIssueRequest) -> BillingIssueResponse:
        """
        Issues a billing request based on the provided billing issue details.

        Args:
            billing_issue_request (BillingIssueRequest): The request object containing details for the billing issue.

        Returns:
            BillingIssueResponse: A response object containing the outcome of the billing issue process.

        Raises:
            SdkException: If an error occurs during the billing issue process.
        """
        if self.billing_client is None:
            self.billing_client = BillingClient()
        
        return self.billing_client.issue_billing(self.config, billing_issue_request)

    def retrieve_billing(self, request_code: str) -> RetrievedBilling:
        """
        Retrieves the billing information based on the specified request code.

        Args:
            request_code (str): The unique code identifying the billing request to retrieve.

        Returns:
            RetrievedBilling: An object containing the details of the retrieved billing information.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.billing_client is None:
            self.billing_client = BillingClient()
        
        return self.billing_client.retrieve_billing(self.config, request_code)
    
    def retrieve_billing_collection(
        self, 
        initial_date: str, 
        final_date: str, 
        filter: BillingRetrievalFilter, 
        sort: Sorting
    ) -> List[RetrievedBilling]:
        """
        Retrieves a collection of billing information for a specified period, applying optional filters and sorting.

        Args:
            initial_date (str): The starting date for the billing retrieval. Format: YYYY-MM-DD.
            final_date (str): The ending date for the billing retrieval. Format: YYYY-MM-DD.
            filter (Optional[BillingRetrievalFilter]): Optional filter criteria to refine the billing retrieval.
            sort (Optional[Sorting]): Optional sorting parameters for the retrieved collection.

        Returns:
            List[RetrievedBilling]: A list of retrieved billing information objects.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.billing_client is None:
            self.billing_client = BillingClient()
        
        return self.billing_client.retrieve_billing_in_range(self.config, initial_date, final_date, filter, sort)

    def retrieve_billing_collection_page(
        self, 
        initial_date: str, 
        final_date: str, 
        page: int, 
        page_size: int, 
        filter: BillingRetrievalFilter, 
        sort: Sorting
    ) -> BillingPage:
        """
        Retrieves a paginated collection of billing information for a specified period, applying optional filters and sorting.

        Args:
            initial_date (str): The starting date for the billing retrieval. Format: YYYY-MM-DD.
            final_date (str): The ending date for the billing retrieval. Format: YYYY-MM-DD.
            page (int): The page number for pagination.
            page_size (Optional[int]): The number of items per page. If None, default size will be used.
            filter (Optional[BillingRetrievalFilter]): Optional filter criteria to refine the billing retrieval.
            sort (Optional[Sorting]): Optional sorting parameters for the retrieved collection.

        Returns:
            BillingPage: A BillingPage object containing the retrieved billing information.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.billing_client is None:
            self.billing_client = BillingClient()
        
        return self.billing_client.retrieve_billing_page(self.config, initial_date, final_date, page, page_size, filter, sort)
    
    def retrieve_billing_pdf(self, request_code: str, file: str) -> None:
        """
        Retrieves the billing PDF document based on the specified request code and saves it to a file.

        Args:
            request_code (str): The unique code identifying the billing request for which the PDF should be retrieved.
            file (str): The path to the file where the PDF will be saved.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.billing_client is None:
            self.billing_client = BillingClient()
        
        self.billing_client.retrieve_billing_in_pdf(self.config, request_code, file)

    def retrieve_billing_summary(
        self, 
        initial_date: str, 
        final_date: str, 
        filter: BillingRetrievalFilter
    ) -> list[SummaryItem]:
        """
        Retrieves a summary of billing information for a specified period, applying optional filters.

        Args:
            initial_date (str): The starting date for the billing summary retrieval. Format: YYYY-MM-DD.
            final_date (str): The ending date for the billing summary retrieval. Format: YYYY-MM-DD.
            filter (Optional[BillingRetrievalFilter]): Optional filter criteria to refine the billing summary retrieval.

        Returns:
            Summary: A Summary object containing the billing information summary.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.billing_client is None:
            self.billing_client = BillingClient()
        
        return self.billing_client.retrieve_billing_summary(self.config, initial_date, final_date, filter)
    
    def retrieve_callbacks(
        self, 
        initial_date_hour: str, 
        final_date_hour: str, 
        filter: BillingRetrieveCallbacksFilter,
        page_size: int
    ) -> List[BillingRetrieveCallbackResponse]:
        """
        Retrieves a list of callback responses for a specified period, applying optional filters.

        Args:
            initial_date_hour (str): The starting date and hour for the callback retrieval. Format: YYYY-MM-DDTHH:mm.
            final_date_hour (str): The ending date and hour for the callback retrieval. Format: YYYY-MM-DDTHH:mm.
            filter (Optional[BillingRetrieveCallbacksFilter]): Optional filter criteria to refine the callback retrieval.

        Returns:
            List[BillingRetrieveCallbackResponse]: A list of RetrieveCallbackResponse objects containing the retrieved callback information.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.billing_webhook_client is None:
            self.billing_webhook_client = BillingWebhookClient()
        
        return self.billing_webhook_client.retrieve_callbacks_in_range(self.config, initial_date_hour, final_date_hour, filter, page_size)

    def retrieve_callbacks_page(
        self, 
        initial_date_hour: str, 
        final_date_hour: str, 
        page: int, 
        page_size: int, 
        filter: BillingRetrieveCallbacksFilter
    ) -> BillingCallbackPage:
        """
        Retrieves a paginated list of callbacks for a specified period, applying optional filters.

        Args:
            initial_date_hour (str): The starting date and hour for the callback retrieval. Format: YYYY-MM-DDTHH:mm.
            final_date_hour (str): The ending date and hour for the callback retrieval. Format: YYYY-MM-DDTHH:mm.
            page (int): The page number for pagination.
            page_size (Optional[int]): The number of items per page. If None, default size will be used.
            filter (Optional[BillingRetrieveCallbacksFilter]): Optional filter criteria to refine the callback retrieval.

        Returns:
            BillingCallbackPage: A CallbackPage object containing the paginated list of retrieved callbacks.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.billing_webhook_client is None:
            self.billing_webhook_client = BillingWebhookClient()
        
        return self.billing_webhook_client.retrieve_callback_page(self.config, initial_date_hour, final_date_hour, page, page_size, filter)
    
    def include_webhook(self, url: str) -> None:
        """
        Includes a webhook URL for receiving notifications.

        Args:
            url (str): The URL of the webhook to be included.

        Raises:
            SdkException: If an error occurs during the inclusion process.
        """
        if self.billing_webhook_client is None:
            self.billing_webhook_client = BillingWebhookClient()
        
        self.billing_webhook_client.include_webhook(self.config, url)

    def retrieve_webhook(self) -> Webhook:
        """
        Retrieves the currently configured webhook information.

        Returns:
            Webhook: A Webhook object containing the details of the configured webhook.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.billing_webhook_client is None:
            self.billing_webhook_client = BillingWebhookClient()
        
        return self.billing_webhook_client.retrieve_webhook(self.config)

    def delete_webhook(self) -> None:
        """
        Deletes the currently configured webhook.

        Raises:
            SdkException: If an error occurs during the deletion process.
        """
        if self.billing_webhook_client is None:
            self.billing_webhook_client = BillingWebhookClient()
        
        self.billing_webhook_client.delete_webhook(self.config)