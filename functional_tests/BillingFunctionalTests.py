import json

from functional_tests.utils.FuncTestUtils import FuncTestUtils
from inter_sdk_python.InterSdk import InterSdk
from inter_sdk_python.billing.enums.PersonType import PersonType
from inter_sdk_python.billing.models.BillingIssueRequest import BillingIssueRequest
from inter_sdk_python.billing.models.BillingRetrievalFilter import BillingRetrievalFilter
from inter_sdk_python.billing.models.BillingRetrieveCallbacksFilter import BillingRetrieveCallbacksFilter
from inter_sdk_python.billing.models.Person import Person
from inter_sdk_python.billing.models.Sorting import Sorting


class BillingFunctionalTests:
    def __init__(self, inter_sdk: InterSdk):
        self.billing_sdk = inter_sdk.billing()

    def test_billing_issue_billing(self) -> None:
        """
        Issues a billing request for a specified payer and amount.
        
        Raises:
            SdkException: If an error occurs during the billing process.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Include billing:")

        person_type = PersonType.FISICA

        your_number = FuncTestUtils.get_string("yourNumber")
        due_date = FuncTestUtils.get_string("dueDate(YYYY-MM-DD)")
        value = FuncTestUtils.get_big_decimal("value(99.99)")

        print("Payer data:")
        document = FuncTestUtils.get_string("cpf")
        name = FuncTestUtils.get_string("name")
        street = FuncTestUtils.get_string("street")
        city = FuncTestUtils.get_string("city")
        state = FuncTestUtils.get_string("state").upper()
        cep = FuncTestUtils.get_string("cep")

        payer = Person(
            cpf_cnpj=document,
            person_type=person_type,
            name=name,
            address=street,
            city=city,
            state=state,
            zip_code=cep
        )

        billing = BillingIssueRequest(
            your_number=your_number,
            nominal_value=value,
            due_date=due_date,
            scheduled_days=0,
            payer=payer
        )

        billing_issue_response = self.billing_sdk.issue_billing(billing)
        print(json.dumps(billing_issue_response.to_dict(), indent=4))

    def test_billing_cancel_billing(self) -> None:
        """
        Cancels a billing request using the specified request code and reason.
        
        Raises:
            SdkException: If an error occurs during the cancellation of the billing.
        """
        print("Cancel billing:")

        request_code = FuncTestUtils.get_string("requestCode")
        cancellation_reason = FuncTestUtils.get_string("cancellationReason")

        self.billing_sdk.cancel_billing(request_code, cancellation_reason)
        print("Billing canceled.")

    def test_billing_retrieve_billing(self) -> None:
        """
        Retrieves billing information for a specified request code.
        
        Raises:
            SdkException: If an error occurs during the retrieval of billing.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving billing...")

        request_code = FuncTestUtils.get_string("requestCode")

        retrieved_billing = self.billing_sdk.retrieve_billing(request_code)
        print(json.dumps(retrieved_billing.to_dict(), indent=4))

    def test_billing_retrieve_billing_collection(self) -> None:
        """
        Retrieves a collection of billing records within a specified date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of billing collection.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving billing collection...")

        initial_date = FuncTestUtils.get_string("initialDate(YYYY-MM-DD)")
        final_date = FuncTestUtils.get_string("finalDate(YYYY-MM-DD)")
        billing_retrieval_filter = BillingRetrievalFilter() 
        sorting = Sorting() 

        retrieve_billings = self.billing_sdk.retrieve_billing_collection(initial_date, final_date, billing_retrieval_filter, sorting)
        billings_dict = [billing.to_dict() for billing in retrieve_billings]
        print(json.dumps(billings_dict, indent=4))

    def test_billing_retrieve_billing_collection_page(self) -> None:
        """
        Retrieves a paginated collection of billing records within a specified date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of billing collection.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving billing collection page...")

        initial_date = FuncTestUtils.get_string("initialDate(YYYY-MM-DD)")
        final_date = FuncTestUtils.get_string("finalDate(YYYY-MM-DD)")
        billing_retrieval_filter = BillingRetrievalFilter() 
        page = 0
        page_size = 10
        sorting = Sorting() 

        billing_page = self.billing_sdk.retrieve_billing_collection_page(initial_date, final_date, page, page_size, billing_retrieval_filter, sorting)
        print(json.dumps(billing_page.to_dict(), indent=4))

    def test_billing_retrieve_billing_pdf(self) -> None:
        """
        Retrieves a billing document in PDF format.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the billing PDF.
        """
        print("Retrieving billing in PDF...")

        request_code = FuncTestUtils.get_string("requestCode")
        file = f"file_{request_code}.pdf"

        self.billing_sdk.retrieve_billing_pdf(request_code, file)
        print("Generated file: " + file)

    def test_billing_retrieve_billing_summary(self) -> None:
        """
        Retrieves a summary of billing records within a specified date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the billing summary.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving billing summary...")

        initial_date = FuncTestUtils.get_string("initialDate")
        final_date = FuncTestUtils.get_string("finalDate")
        billing_retrieval_filter = BillingRetrievalFilter() 

        summary_list = self.billing_sdk.retrieve_billing_summary(initial_date, final_date, billing_retrieval_filter)
        summary_dict = [summary_list.to_dict() for summary_list in summary_list]
        print(json.dumps(summary_dict, indent=4))
        
    def test_billing_retrieve_callbacks(self) -> None:
        """
        Retrieves a list of billing callbacks within a specified date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of callbacks.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving callbacks...")

        initial_date_hour = FuncTestUtils.get_string("initialDateHour(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        final_date_hour = FuncTestUtils.get_string("finalDateHour(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        filter = BillingRetrieveCallbacksFilter() 
        page_size = 50

        callbacks = self.billing_sdk.retrieve_callbacks(initial_date_hour, final_date_hour, filter, page_size)
        callback_dict = [callback.to_dict() for callback in callbacks]
        print(json.dumps(callback_dict, indent=4))

    def test_billing_retrieve_callbacks_page(self) -> None:
        """
        Retrieves a paginated list of billing callbacks within a specified date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of callbacks.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving callback page...")

        initial_date_hour = FuncTestUtils.get_string("initialDateHour(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        final_date_hour = FuncTestUtils.get_string("finalDateHour(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        filter = BillingRetrieveCallbacksFilter() 
        page = 0
        page_size = 10

        callback = self.billing_sdk.retrieve_callbacks_page(initial_date_hour, final_date_hour, page, page_size, filter)
        print(json.dumps(callback.to_dict(), indent=4))

    def test_billing_include_webhook(self) -> None:
        """
        Includes a webhook for billing notifications.
        
        Raises:
            SdkException: If an error occurs during the inclusion of the webhook.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Include webhook:")

        webhook_url = FuncTestUtils.get_string("webhookUrl")

        self.billing_sdk.include_webhook(webhook_url)
        print("Webhook included.")

    def test_billing_retrieve_webhook(self) -> None:
        """
        Retrieves the current webhook configuration.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the webhook.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving webhook...")

        webhook = self.billing_sdk.retrieve_webhook()
        print(json.dumps(webhook.to_dict(), indent=4))

    def test_billing_delete_webhook(self) -> None:
        """
        Deletes the current webhook configuration.
        
        Raises:
            SdkException: If an error occurs during the deletion of the webhook.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Deleting webhook...")

        self.billing_sdk.delete_webhook()
        print("Webhook deleted.")
