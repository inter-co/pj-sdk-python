from typing import List

from inter_sdk_python.commons.models.Config import Config
from inter_sdk_python.commons.models.Webhook import Webhook
from inter_sdk_python.pix.duebilling.DueBillingClient import DueBillingClient
from inter_sdk_python.pix.duebillingbatch.DueBillingBatchClient import DueBillingBatchClient
from inter_sdk_python.pix.enums.ImmediateBillingType import ImmediateBillingType
from inter_sdk_python.pix.immediatebillings.ImmediateBillingClient import ImmediateBillingClient
from inter_sdk_python.pix.locations.LocationClient import LocationClient
from inter_sdk_python.pix.models.BillingPage import BillingPage
from inter_sdk_python.pix.models.CallbackRetrieveFilter import CallbackRetrieveFilter
from inter_sdk_python.pix.models.DetailedDevolution import DetailedDevolution
from inter_sdk_python.pix.models.DetailedDuePixBilling import DetailedDuePixBilling
from inter_sdk_python.pix.models.DetailedImmediatePixBilling import DetailedImmediatePixBilling
from inter_sdk_python.pix.models.DevolutionRequestBody import DevolutionRequestBody
from inter_sdk_python.pix.models.DueBilling import DueBilling
from inter_sdk_python.pix.models.DueBillingBatch import DueBillingBatch
from inter_sdk_python.pix.models.DueBillingBatchPage import DueBillingBatchPage
from inter_sdk_python.pix.models.DueBillingBatchSummary import DueBillingBatchSummary
from inter_sdk_python.pix.models.DueBillingPage import DueBillingPage
from inter_sdk_python.pix.models.GeneratedDueBilling import GeneratedDueBilling
from inter_sdk_python.pix.models.GeneratedImmediateBilling import GeneratedImmediateBilling
from inter_sdk_python.pix.models.IncludeDueBillingBatchRequest import IncludeDueBillingBatchRequest
from inter_sdk_python.pix.models.Location import Location
from inter_sdk_python.pix.models.LocationPage import LocationPage
from inter_sdk_python.pix.models.Pix import Pix
from inter_sdk_python.pix.models.PixBilling import PixBilling
from inter_sdk_python.pix.models.PixCallbackPage import PixCallbackPage
from inter_sdk_python.pix.models.PixPage import PixPage
from inter_sdk_python.pix.models.RetrieveCallbackResponse import RetrieveCallbackResponse
from inter_sdk_python.pix.models.RetrieveDueBillingFilter import RetrieveDueBillingFilter
from inter_sdk_python.pix.models.RetrieveImmediateBillingsFilter import RetrieveImmediateBillingsFilter
from inter_sdk_python.pix.models.RetrieveLocationFilter import RetrieveLocationFilter
from inter_sdk_python.pix.models.RetrievedPixFilter import RetrievedPixFilter
from inter_sdk_python.pix.pix.PixClient import PixClient
from inter_sdk_python.pix.webhooks.PixWebhookClient import PixWebhookClient


class PixSdk:
    def __init__(self, config: Config):
        self.config = config
        self.due_billing_client = None
        self.due_billing_batch_client = None
        self.immediate_billing_client = None
        self.location_client = None
        self.pix_client = None
        self.pix_webhook_sdk = None

    def include_due_pix_billing(self, txid: str, billing: DueBilling) -> GeneratedDueBilling:
        """
        Includes a due billing entry for a PIX transaction.

        Args:
            txid (str): The transaction ID associated with the due billing.
            billing (DueBilling): The DueBilling object containing the billing details to be included.

        Returns:
            GeneratedDueBilling: A GeneratedDueBilling object containing the details of the included due billing.

        Raises:
            SdkException: If an error occurs during the inclusion process.
        """
        if self.due_billing_client is None:
            self.due_billing_client = DueBillingClient()

        return self.due_billing_client.include_due_billing(self.config, txid, billing)

    def retrieve_due_pix_billing(self, txid: str) -> DetailedDuePixBilling:
        """
        Retrieves the detailed due billing information for a specific PIX transaction.

        Args:
            txid (str): The transaction ID associated with the due billing to be retrieved.

        Returns:
            DetailedDuePixBilling: A DetailedDuePixBilling object containing the details of the retrieved due billing.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.due_billing_client is None:
            self.due_billing_client = DueBillingClient()

        return self.due_billing_client.retrieve_due_billing(self.config, txid)

    def retrieve_due_billing_collection_in_range(
        self,
        initial_date: str,
        final_date: str,
        filter: RetrieveDueBillingFilter
    ) -> List[DetailedDuePixBilling]:
        """
        Retrieves a list of detailed due billing entries for a specified period, applying optional filters.

        Args:
            initial_date (str): The starting date for the billing collection retrieval. Format: YYYY-MM-DD.
            final_date (str): The ending date for the billing collection retrieval. Format: YYYY-MM-DD.
            filter (Optional[RetrieveDueBillingFilter]): Optional filter criteria to refine the billing collection retrieval.

        Returns:
            List[DetailedDuePixBilling]: A list of DetailedDuePixBilling objects containing the retrieved billing information.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.due_billing_client is None:
            self.due_billing_client = DueBillingClient()

        return self.due_billing_client.retrieve_due_billings_in_range(self.config, initial_date, final_date, filter)

    def retrieve_due_billing_collection_page(
        self,
        initial_date: str,
        final_date: str,
        page: int,
        page_size: int,
        filter: RetrieveDueBillingFilter
    ) -> DueBillingPage:
        """
        Retrieves a paginated collection of due billing entries for a specified period, applying optional filters.

        Args:
            initial_date (str): The starting date for the billing collection retrieval. Format: YYYY-MM-DD.
            final_date (str): The ending date for the billing collection retrieval. Format: YYYY-MM-DD.
            page (int): The page number for pagination.
            page_size (Optional[int]): The number of items per page. If None, a default size will be used.
            filter (Optional[RetrieveDueBillingFilter]): Optional filter criteria to refine the billing collection retrieval.

        Returns:
            DueBillingPage: A DueBillingPage object containing the paginated list of retrieved due billing entries.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.due_billing_client is None:
            self.due_billing_client = DueBillingClient()

        return self.due_billing_client.retrieve_due_billing_page(self.config, initial_date, final_date, page, page_size, filter)

    def review_due_pix_billing(self, txid: str, billing: DueBilling) -> GeneratedDueBilling:
        """
        Reviews a due billing entry for a PIX transaction.

        Args:
            txid (str): The transaction ID associated with the due billing to be reviewed.
            billing (DueBilling): The DueBilling object containing the billing details to be reviewed.

        Returns:
            GeneratedDueBilling: A GeneratedDueBilling object containing the details of the reviewed due billing.

        Raises:
            SdkException: If an error occurs during the review process.
        """
        if self.due_billing_client is None:
            self.due_billing_client = DueBillingClient()

        return self.due_billing_client.review_due_billing(self.config, txid, billing)

    def include_due_billing_batch(self, txid: str, batch_request: IncludeDueBillingBatchRequest) -> None:
        """
        Includes a batch of due billing entries for a specific PIX transaction.

        Args:
            txid (str): The transaction ID associated with the due billing batch.
            batch_request (IncludeDueBillingBatchRequest): The IncludeDueBillingBatchRequest object containing the details of the billing batch to be included.

        Raises:
            SdkException: If an error occurs during the inclusion process.
        """
        if self.due_billing_batch_client is None:
            self.due_billing_batch_client = DueBillingBatchClient()

        self.due_billing_batch_client.include_due_billing_batch(self.config, txid, batch_request)

    def retrieve_due_billing_batch(self, id: str) -> DueBillingBatch:
        """
        Retrieves a due billing batch by its identifier.

        Args:
            id (str): The identifier of the billing batch to be retrieved.

        Returns:
            DueBillingBatch: A DueBillingBatch object containing the details of the retrieved billing batch.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.due_billing_batch_client is None:
            self.due_billing_batch_client = DueBillingBatchClient()

        return self.due_billing_batch_client.retrieve_due_billing_batch(self.config, id)

    def retrieve_due_billing_batch_collection_page(
        self,
        initial_date: str,
        final_date: str,
        page: int,
        page_size: int
    ) -> DueBillingBatchPage:
        """
        Retrieves a paginated collection of due billing batches for a specified period.

        Args:
            initial_date (str): The starting date for the billing batch collection retrieval. Format: YYYY-MM-DD.
            final_date (str): The ending date for the billing batch collection retrieval. Format: YYYY-MM-DD.
            page (int): The page number for pagination.
            page_size (Optional[int]): The number of items per page. If None, a default size will be used.

        Returns:
            DueBillingBatchPage: A DueBillingBatchPage object containing the paginated list of retrieved due billing batches.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.due_billing_batch_client is None:
            self.due_billing_batch_client = DueBillingBatchClient()

        return self.due_billing_batch_client.retrieve_due_billing_batch_page(self.config, initial_date, final_date, page, page_size)

    def retrieve_due_billing_batch_collection_in_range(
        self,
        initial_date: str,
        final_date: str
    ) -> List[DueBillingBatch]:
        """
        Retrieves a list of due billing batches for a specified period.

        Args:
            initial_date (str): The starting date for the billing batch collection retrieval. Format: YYYY-MM-DD.
            final_date (str): The ending date for the billing batch collection retrieval. Format: YYYY-MM-DD.

        Returns:
            List[DueBillingBatch]: A list of DueBillingBatch objects containing the retrieved billing batches.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.due_billing_batch_client is None:
            self.due_billing_batch_client = DueBillingBatchClient()

        return self.due_billing_batch_client.retrieve_due_billing_batches_in_range(self.config, initial_date, final_date)

    def retrieve_due_billing_batch_by_situation(self, id: str, situation: str) -> DueBillingBatch:
        """
        Retrieves the situation of a specific due billing batch by its identifier.

        Args:
            id (str): The identifier of the billing batch whose situation is to be retrieved.
            situation (str): The specific situation to filter the results.

        Returns:
            DueBillingBatch: A DueBillingBatch object containing the details of the retrieved billing batch situation.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.due_billing_batch_client is None:
            self.due_billing_batch_client = DueBillingBatchClient()

        return self.due_billing_batch_client.retrieve_due_billing_batch_by_situation(self.config, id, situation)

    def retrieve_due_billing_batch_summary(self, id: str) -> DueBillingBatchSummary:
        """
        Retrieves the summary of a specific due billing batch by its identifier.

        Args:
            id (str): The identifier of the billing batch whose summary is to be retrieved.

        Returns:
            DueBillingBatchSummary: A DueBillingBatchSummary object containing the summary details of the retrieved billing batch.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.due_billing_batch_client is None:
            self.due_billing_batch_client = DueBillingBatchClient()

        return self.due_billing_batch_client.retrieve_due_billing_batch_summary(self.config, id)

    def review_due_billing_batch(self, id: str, request: IncludeDueBillingBatchRequest) -> None:
        """
        Reviews a due billing batch identified by its ID.

        Args:
            id (str): The identifier of the billing batch to be reviewed.
            request (IncludeDueBillingBatchRequest): The IncludeDueBillingBatchRequest object containing details for the review process.

        Raises:
            SdkException: If an error occurs during the review process.
        """
        if self.due_billing_batch_client is None:
            self.due_billing_batch_client = DueBillingBatchClient()

        self.due_billing_batch_client.review_due_billing_batch(self.config, id, request)

    def include_immediate_billing(self, billing: PixBilling) -> GeneratedImmediateBilling:
        """
        Includes an immediate billing entry for a PIX transaction.

        Args:
            billing (PixBilling): The PixBilling object containing the details of the immediate billing to be included.

        Returns:
            GeneratedImmediateBilling: A GeneratedImmediateBilling object containing the details of the included immediate billing.

        Raises:
            SdkException: If an error occurs during the inclusion process.
        """
        if self.immediate_billing_client is None:
            self.immediate_billing_client = ImmediateBillingClient()

        return self.immediate_billing_client.include_immediate_billing(self.config, billing)

    def retrieve_immediate_billing(self, txid: str) -> DetailedImmediatePixBilling:
        """
        Retrieves the details of an immediate billing entry by its transaction ID.

        Args:
            txid (str): The transaction ID associated with the immediate billing to be retrieved.

        Returns:
            DetailedImmediatePixBilling: A DetailedImmediatePixBilling object containing the details of the retrieved immediate billing.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.immediate_billing_client is None:
            self.immediate_billing_client = ImmediateBillingClient()

        return self.immediate_billing_client.retrieve_immediate_billing(self.config, txid)

    def retrieve_immediate_billing_list(
        self,
        initial_date: str,
        final_date: str,
        filter: RetrieveImmediateBillingsFilter
    ) -> List[DetailedImmediatePixBilling]:
        """
        Retrieves a list of detailed immediate billing entries for a specified period, optionally filtered.

        Args:
            initial_date (str): The starting date for the retrieval of immediate billings. Format: YYYY-MM-DD.
            final_date (str): The ending date for the retrieval of immediate billings. Format: YYYY-MM-DD.
            filter (Optional[RetrieveImmediateBillingsFilter]): The filter criteria for retrieving the immediate billings.

        Returns:
            List[DetailedImmediatePixBilling]: A list of DetailedImmediatePixBilling objects containing the details of the retrieved immediate billings.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.immediate_billing_client is None:
            self.immediate_billing_client = ImmediateBillingClient()

        return self.immediate_billing_client.retrieve_immediate_billings_in_range(self.config, initial_date, final_date, filter)

    def retrieve_immediate_billing_page(
        self,
        initial_date: str,
        final_date: str,
        page: int,
        page_size: int,
        filter: RetrieveImmediateBillingsFilter
    ) -> BillingPage:
        """
        Retrieves a paginated list of immediate billing entries for a specified period, optionally filtered.

        Args:
            initial_date (str): The starting date for the retrieval of immediate billings. Format: YYYY-MM-DD.
            final_date (str): The ending date for the retrieval of immediate billings. Format: YYYY-MM-DD.
            page (int): The page number for pagination.
            page_size (Optional[int]): The number of items per page. If None, a default size will be used.
            filter (Optional[RetrieveImmediateBillingsFilter]): The filter criteria for retrieving the immediate billings.

        Returns:
            BillingPage: A BillingPage object containing the paginated list of retrieved immediate billings.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.immediate_billing_client is None:
            self.immediate_billing_client = ImmediateBillingClient()

        return self.immediate_billing_client.retrieve_immediate_billing_page(self.config, initial_date, final_date, page, page_size, filter)

    def review_immediate_billing(self, billing: PixBilling) -> GeneratedImmediateBilling:
        """
        Reviews an immediate billing entry for a PIX transaction.

        Args:
            billing (PixBilling): The PixBilling object containing the details of the immediate billing to be reviewed.

        Returns:
            GeneratedImmediateBilling: A GeneratedImmediateBilling object containing the details of the reviewed immediate billing.

        Raises:
            SdkException: If an error occurs during the review process.
        """
        if self.immediate_billing_client is None:
            self.immediate_billing_client = ImmediateBillingClient()

        return self.immediate_billing_client.review_immediate_billing(self.config, billing)

    def include_location(self, immediate_billing_type: ImmediateBillingType) -> Location:
        """
        Includes a location associated with an immediate billing type.

        Args:
            immediate_billing_type (ImmediateBillingType): The ImmediateBillingType object containing the details of the location to be included.

        Returns:
            Location: A Location object containing the details of the included location.

        Raises:
            SdkException: If an error occurs during the inclusion process.
        """
        if self.location_client is None:
            self.location_client = LocationClient()

        return self.location_client.include_location(self.config, immediate_billing_type)

    def retrieve_location(self, location_id: str) -> Location:
        """
        Retrieves a location by its identifier.

        Args:
            location_id (str): The identifier of the location to be retrieved.

        Returns:
            Location: A Location object containing the details of the retrieved location.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.location_client is None:
            self.location_client = LocationClient()

        return self.location_client.retrieve_location(self.config, location_id)

    def retrieve_locations_list(
        self,
        initial_date: str,
        final_date: str,
        filter: RetrieveLocationFilter
    ) -> List[Location]:
        """
        Retrieves a list of locations for a specified period, optionally filtered.

        Args:
            initial_date (str): The starting date for the retrieval of locations. Format: YYYY-MM-DD.
            final_date (str): The ending date for the retrieval of locations. Format: YYYY-MM-DD.
            filter (Optional[RetrieveLocationFilter]): The filter criteria for retrieving the locations.

        Returns:
            List[Location]: A list of Location objects containing the details of the retrieved locations.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.location_client is None:
            self.location_client = LocationClient()

        return self.location_client.retrieve_location_in_range(self.config, initial_date, final_date, filter)

    def retrieve_locations_page(
        self,
        initial_date: str,
        final_date: str,
        page: int,
        page_size: int,
        filter: RetrieveLocationFilter
    ) -> LocationPage:
        """
        Retrieves a paginated list of locations for a specified period, optionally filtered.

        Args:
            initial_date (str): The starting date for the retrieval of locations. Format: YYYY-MM-DD.
            final_date (str): The ending date for the retrieval of locations. Format: YYYY-MM-DD.
            page (int): The page number for pagination.
            page_size (Optional[int]): The number of items per page. If None, a default size will be used.
            filter (Optional[RetrieveLocationFilter]): The filter criteria for retrieving the locations.

        Returns:
            LocationPage: A LocationPage object containing the paginated list of retrieved locations.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.location_client is None:
            self.location_client = LocationClient()

        return self.location_client.retrieve_location_page(self.config, initial_date, final_date, page, page_size, filter)

    def unlink_location(self, id: str) -> Location:
        """
        Unlinks a location by its identifier.

        Args:
            id (str): The identifier of the location to be unlinked.

        Returns:
            Location: A Location object containing the details of the unlinked location.

        Raises:
            SdkException: If an error occurs during the unlinking process.
        """
        if self.location_client is None:
            self.location_client = LocationClient()

        return self.location_client.unlink_location(self.config, id)

    def request_devolution(
        self,
        e2e_id: str,
        id: str,
        devolution_request_body: DevolutionRequestBody
    ) -> DetailedDevolution:
        """
        Requests a devolution for a specific transaction.

        Args:
            e2e_id (str): The end-to-end identifier for the transaction.
            id (str): The identifier of the devolution request.
            devolution_request_body (DevolutionRequestBody): The body containing the details for the devolution request.

        Returns:
            DetailedDevolution: A DetailedDevolution object containing the details of the requested devolution.

        Raises:
            SdkException: If an error occurs during the request process.
        """
        if self.pix_client is None:
            self.pix_client = PixClient()

        return self.pix_client.request_devolution(self.config, e2e_id, id, devolution_request_body)

    def retrieve_devolution(self, e2e_id: str, id: str) -> DetailedDevolution:
        """
        Retrieves the details of a specific devolution by its identifiers.

        Args:
            e2e_id (str): The end-to-end identifier for the transaction.
            id (str): The identifier of the devolution to be retrieved.

        Returns:
            DetailedDevolution: A DetailedDevolution object containing the details of the retrieved devolution.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.pix_client is None:
            self.pix_client = PixClient()

        return self.pix_client.retrieve_devolution(self.config, e2e_id, id)

    def retrieve_pix_list(
        self,
        initial_date: str,
        final_date: str,
        filter: RetrievedPixFilter
    ) -> List[Pix]:
        """
        Retrieves a list of PIX transactions for a specified period, optionally filtered.

        Args:
            initial_date (str): The starting date for the retrieval of PIX transactions. Format: YYYY-MM-DD.
            final_date (str): The ending date for the retrieval of PIX transactions. Format: YYYY-MM-DD.
            filter (Optional[RetrievedPixFilter]): The filter criteria for retrieving the PIX transactions.

        Returns:
            List[Pix]: A list of Pix objects containing the details of the retrieved PIX transactions.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.pix_client is None:
            self.pix_client = PixClient()

        return self.pix_client.retrieve_pix_list_in_range(self.config, initial_date, final_date, filter)

    def retrieve_pix_page(
        self,
        initial_date: str,
        final_date: str,
        page: int,
        page_size: int,
        filter: RetrievedPixFilter
    ) -> PixPage:
        """
        Retrieves a paginated list of PIX transactions for a specified period, optionally filtered.

        Args:
            initial_date (str): The starting date for the retrieval of PIX transactions. Format: YYYY-MM-DD.
            final_date (str): The ending date for the retrieval of PIX transactions. Format: YYYY-MM-DD.
            page (int): The page number for pagination.
            page_size (Optional[int]): The number of items per page. If None, a default size will be used.
            filter (Optional[RetrievedPixFilter]): The filter criteria for retrieving the PIX transactions.

        Returns:
            PixPage: A PixPage object containing the paginated list of retrieved PIX transactions.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.pix_client is None:
            self.pix_client = PixClient()

        return self.pix_client.retrieve_pix_page(self.config, initial_date, final_date, page, page_size, filter)

    def retrieve_pix(self, e2e_id: str) -> Pix:
        """
        Retrieves the details of a specific PIX transaction by its end-to-end identifier.

        Args:
            e2e_id (str): The end-to-end identifier for the PIX transaction.

        Returns:
            Pix: A Pix object containing the details of the retrieved PIX transaction.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.pix_client is None:
            self.pix_client = PixClient()

        return self.pix_client.retrieve_pix_transaction(self.config, e2e_id)

    def retrieve_callbacks_in_range(
        self,
        initial_date_hour: str,
        final_date_hour: str,
        filter: CallbackRetrieveFilter
    ) -> List[RetrieveCallbackResponse]:
        """
        Retrieves a list of callback responses for a specified period, optionally filtered.

        Args:
            initial_date_hour (str): The starting date and hour for the retrieval of callbacks. Format: YYYY-MM-DD HH:mm.
            final_date_hour (str): The ending date and hour for the retrieval of callbacks. Format: YYYY-MM-DD HH:mm.
            filter (Optional[CallbackRetrieveFilter]): The filter criteria for retrieving the callback responses.

        Returns:
            List[RetrieveCallbackResponse]: A list of RetrieveCallbackResponse objects containing the details of the retrieved callbacks.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.pix_webhook_sdk is None:
            self.pix_webhook_sdk = PixWebhookClient()

        return self.pix_webhook_sdk.retrieve_callbacks_in_range(self.config, initial_date_hour, final_date_hour, filter)

    def retrieve_callbacks_page(
        self,
        initial_date_hour: str,
        final_date_hour: str,
        page: int,
        page_size: int,
        filter: CallbackRetrieveFilter
    ) -> PixCallbackPage:
        """
        Retrieves a paginated list of callback responses for a specified period, optionally filtered.

        Args:
            initial_date_hour (str): The starting date and hour for the retrieval of callbacks. Format: YYYY-MM-DD HH:mm.
            final_date_hour (str): The ending date and hour for the retrieval of callbacks. Format: YYYY-MM-DD HH:mm.
            page (int): The page number for pagination.
            page_size (Optional[int]): The number of items per page. If None, a default size will be used.
            filter (Optional[CallbackRetrieveFilter]): The filter criteria for retrieving the callback responses.

        Returns:
            PixCallbackPage: A PixCallbackPage object containing the paginated list of retrieved callbacks.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.pix_webhook_sdk is None:
            self.pix_webhook_sdk = PixWebhookClient()

        return self.pix_webhook_sdk.retrieve_callbacks_page(self.config, initial_date_hour, final_date_hour, page, page_size, filter)

    def include_webhook(self, key: str, webhook_url: str) -> None:
        """
        Includes a new webhook for a specified key.

        Args:
            key (str): The identifier key for which the webhook is being included.
            webhook_url (str): The URL of the webhook to be included.

        Raises:
            SdkException: If an error occurs during the inclusion of the webhook.
        """
        if self.pix_webhook_sdk is None:
            self.pix_webhook_sdk = PixWebhookClient()

        self.pix_webhook_sdk.include_webhook(self.config, key, webhook_url)

    def retrieve_webhook(self, key: str) -> Webhook:
        """
        Retrieves the details of a specific webhook by its identifier key.

        Args:
            key (str): The identifier key for the webhook to be retrieved.

        Returns:
            Webhook: A Webhook object containing the details of the retrieved webhook.

        Raises:
            SdkException: If an error occurs during the retrieval process.
        """
        if self.pix_webhook_sdk is None:
            self.pix_webhook_sdk = PixWebhookClient()

        return self.pix_webhook_sdk.retrieve_webhook(self.config, key)

    def delete_webhook(self, key: str) -> None:
        """
        Deletes a specific webhook identified by its key.

        Args:
            key (str): The identifier key for the webhook to be deleted.

        Raises:
            SdkException: If an error occurs during the deletion process.
        """
        if self.pix_webhook_sdk is None:
            self.pix_webhook_sdk = PixWebhookClient()

        self.pix_webhook_sdk.delete_webhook(self.config, key)