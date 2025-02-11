import json

from functional_tests.utils.FuncTestUtils import FuncTestUtils
from inter_sdk_python.InterSdk import InterSdk
from inter_sdk_python.pix.enums.DevolutionNature import DevolutionNature
from inter_sdk_python.pix.enums.ImmediateBillingType import ImmediateBillingType
from inter_sdk_python.pix.models.Calendar import Calendar
from inter_sdk_python.pix.models.CallbackRetrieveFilter import CallbackRetrieveFilter
from inter_sdk_python.pix.models.Debtor import Debtor
from inter_sdk_python.pix.models.DevolutionRequestBody import DevolutionRequestBody
from inter_sdk_python.pix.models.DueBilling import DueBilling
from inter_sdk_python.pix.models.DueBillingCalendar import DueBillingCalendar
from inter_sdk_python.pix.models.DueBillingValue import DueBillingValue
from inter_sdk_python.pix.models.IncludeDueBillingBatchRequest import IncludeDueBillingBatchRequest
from inter_sdk_python.pix.models.PixBilling import PixBilling
from inter_sdk_python.pix.models.PixValue import PixValue
from inter_sdk_python.pix.models.RetrieveDueBillingFilter import RetrieveDueBillingFilter
from inter_sdk_python.pix.models.RetrieveImmediateBillingsFilter import RetrieveImmediateBillingsFilter
from inter_sdk_python.pix.models.RetrieveLocationFilter import RetrieveLocationFilter
from inter_sdk_python.pix.models.RetrievedPixFilter import RetrievedPixFilter


class PixFunctionalTests:
    def __init__(self, inter_sdk: InterSdk):
        self.pix_sdk = inter_sdk.pix()

    def test_pix_include_due_billing(self) -> None:
        """
        Includes a due billing request for PIX payments.
        
        Raises:
            SdkException: If an error occurs during the inclusion of the due billing.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Include due billing:")

        document = FuncTestUtils.get_string("cnpj")
        name = FuncTestUtils.get_string("name")
        city = FuncTestUtils.get_string("city")
        street = FuncTestUtils.get_string("street")
        cep = FuncTestUtils.get_string("cep")
        email = FuncTestUtils.get_string("email")
        state = FuncTestUtils.get_string("state").upper()
        value = FuncTestUtils.get_string("value(99.99)")
        key = FuncTestUtils.get_string("key")
        tx_id = FuncTestUtils.get_string("txId")
        due_date = FuncTestUtils.get_string("dueDate (yyyy-MM-dd)")
        validity = FuncTestUtils.get_string("validity (days)")

        debtor = Debtor(
            cnpj=document,
            name=name,
            city=city,
            address=street,
            postal_code=cep,
            state=state,
            email=email
        )

        validity_after_expiration = int(validity)

        due_billing_value = DueBillingValue(
            original_value=value
        )
        calendar = DueBillingCalendar(
            due_date=due_date,
            validity_after_expiration=validity_after_expiration
        )
        due_billing = DueBilling(
            debtor=debtor,
            value=due_billing_value,
            key=key,
            calendar=calendar
        )

        generated_immediate_billing = self.pix_sdk.include_due_pix_billing(tx_id, due_billing)
        print(json.dumps(generated_immediate_billing.to_dict(), indent=4))

    def test_pix_retrieve_due_billing(self) -> None:
        """
        Retrieves detailed information for a specific due billing request by transaction ID.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the due billing.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving due billing:")

        tx_id = FuncTestUtils.get_string("txId")

        detailed_due_pix_billing = self.pix_sdk.retrieve_due_pix_billing(tx_id)
        print(json.dumps(detailed_due_pix_billing.to_dict(), indent=4))

    def test_pix_retrieve_due_billing_collection(self) -> None:
        """
        Retrieves a collection of due billing records within a specified date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the due billing collection.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving due billing collection:")

        initial_date = FuncTestUtils.get_string("initialDate(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        final_date = FuncTestUtils.get_string("finalDate(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        retrieve_due_billing_filter = RetrieveDueBillingFilter()

        due_pix_billing_list = self.pix_sdk.retrieve_due_billing_collection_in_range(initial_date, final_date, retrieve_due_billing_filter)
        due_pix_list_dict = [due_pix_billing.to_dict() for due_pix_billing in due_pix_billing_list]
        print(json.dumps(due_pix_list_dict, indent=4))

    def test_pix_retrieve_due_billing_collection_page(self) -> None:
        """
        Retrieves a paginated collection of due billing records within a specified date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the due billing collection page.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving due billing collection page:")

        initial_date = FuncTestUtils.get_string("initialDate(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        final_date = FuncTestUtils.get_string("finalDate(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        retrieve_due_billing_filter = RetrieveDueBillingFilter()
        page = 0
        page_size = 10

        due_billing_page = self.pix_sdk.retrieve_due_billing_collection_page(initial_date, final_date, page, page_size, retrieve_due_billing_filter)
        print(json.dumps(due_billing_page.to_dict(), indent=4))

    def test_pix_review_due_billing(self) -> None:
        """
        Reviews a due billing request by transaction ID.
        
        Raises:
            SdkException: If an error occurs during the review of the due billing.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Review due billing:")

        tx_id = FuncTestUtils.get_string("txId")

        document = FuncTestUtils.get_string("cnpj")
        name = FuncTestUtils.get_string("debtor name")
        value = FuncTestUtils.get_string("value(99.99)")

        debtor = Debtor(
            cnpj=document,
            name=name
        )

        due_billing_value = DueBillingValue(
            original_value=value
        )

        due_billing = DueBilling(
            debtor=debtor,
            value=due_billing_value
        )

        generated_due_billing = self.pix_sdk.review_due_pix_billing(tx_id, due_billing)
        print(json.dumps(generated_due_billing.to_dict(), indent=4))

    def test_pix_include_due_billing_batch(self) -> None:
        """
        Includes a batch of due billing requests for PIX payments.
        
        Raises:
            SdkException: If an error occurs during the inclusion of the due billing batch.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Include due billing batch:")

        batch_description = FuncTestUtils.get_string("batch description")
        batch_id = FuncTestUtils.get_string("batchId")

        document = FuncTestUtils.get_string("cpf")
        name = FuncTestUtils.get_string("debtor name")

        first_tx_id = FuncTestUtils.get_string("First billing txId")
        first_value = FuncTestUtils.get_string("First billing value(99.99)")
        first_key = FuncTestUtils.get_string("First billing key")
        first_due_billing_value = DueBillingValue(original_value=first_value)
        first_calendar = DueBillingCalendar(
            due_date=FuncTestUtils.get_string("First billing dueDate (yyyy-MM-dd)")
        )

        second_tx_id = FuncTestUtils.get_string("Second billing txId")
        second_value = FuncTestUtils.get_string("Second billing value(99.99)")
        second_key = FuncTestUtils.get_string("Second billing key")
        second_due_billing_value = DueBillingValue(original_value=second_value)
        second_calendar = DueBillingCalendar(
            due_date=FuncTestUtils.get_string("Second billing dueDate (yyyy-MM-dd)")
        )

        debtor = Debtor(cpf=document, name=name)

        due_billing1 = DueBilling(
            txid=first_tx_id,
            calendar=first_calendar,
            debtor=debtor,
            value=first_due_billing_value,
            key=first_key
        )

        due_billing2 = DueBilling(
            txid=second_tx_id,
            calendar=second_calendar,
            debtor=debtor,
            value=second_due_billing_value,
            key=second_key
        )

        due_billing_list = [due_billing1, due_billing2]

        batch = IncludeDueBillingBatchRequest(
            description=batch_description,
            due_billings=due_billing_list
        )

        self.pix_sdk.include_due_billing_batch(batch_id, batch)
        print("Batch included: " + batch_id)

    def test_pix_retrieve_due_billing_batch(self) -> None:
        """
        Retrieves a specific due billing batch by batch ID.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the due billing batch.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving due billing batch...")

        batch_id = FuncTestUtils.get_string("batchId")

        due_billing_batch = self.pix_sdk.retrieve_due_billing_batch(batch_id)
        print(json.dumps(due_billing_batch.to_dict(), indent=4))

    def test_pix_retrieve_due_billing_batch_collection_page(self) -> None:
        """
        Retrieves a paginated collection of due billing batches within a specified date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the due billing batch collection.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving due billing batch collection...")

        initial_date = FuncTestUtils.get_string("initialDate(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        final_date = FuncTestUtils.get_string("finalDate(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        page = 0
        page_size = 10

        due_billing_batch_page  = self.pix_sdk.retrieve_due_billing_batch_collection_page(initial_date, final_date, page, page_size)
        print(json.dumps(due_billing_batch_page.to_dict(), indent=4))

    def test_pix_retrieve_due_billing_batch_collection(self) -> None:
        """
        Retrieves a collection of due billing batches within a specified date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the due billing batch collection.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving due billing batch collection...")

        initial_date = FuncTestUtils.get_string("initialDate(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        final_date = FuncTestUtils.get_string("finalDate(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")

        due_billing_batch_collection = self.pix_sdk.retrieve_due_billing_batch_collection_in_range(initial_date, final_date)
        due_billing_batch_collection_dict = [due_billing_batch.to_dict() for due_billing_batch in due_billing_batch_collection]
        print(json.dumps(due_billing_batch_collection_dict, indent=4))

    def test_pix_retrieve_due_billing_batch_by_situation(self) -> None:
        """
        Retrieves a due billing batch by its situation.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the due billing batch by situation.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving due billing batch by situation...")

        batch_id = FuncTestUtils.get_string("batchId")
        situation = FuncTestUtils.get_string("batch situation: (EM_PROCESSAMENTO, CRIADA, NEGADA)")

        due_billing_batch = self.pix_sdk.retrieve_due_billing_batch_by_situation(batch_id, situation)
        print(json.dumps(due_billing_batch.to_dict(), indent=4))

    def test_pix_retrieve_due_billing_batch_summary(self) -> None:
        """
        Retrieves a summary of a due billing batch by batch ID.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the due billing batch summary.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving due billing batch summary...")

        batch_id = FuncTestUtils.get_string("batchId")

        due_billing_batch_summary = self.pix_sdk.retrieve_due_billing_batch_summary(batch_id)
        print(json.dumps(due_billing_batch_summary.to_dict(), indent=4))

    def test_pix_review_due_billing_batch(self) -> None:
        """
        Reviews a due billing batch by batch ID.
        
        Raises:
            SdkException: If an error occurs during the review of the due billing batch.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Reviewing due billing batch...")

        batch_description = FuncTestUtils.get_string("batch description")
        batch_id = FuncTestUtils.get_string("batchId")

        document = FuncTestUtils.get_string("cpf")
        name = FuncTestUtils.get_string("debtor name")

        first_tx_id = FuncTestUtils.get_string("First billing txId")
        first_value = FuncTestUtils.get_string("First billing value(99.99)")
        first_key = FuncTestUtils.get_string("First billing key")
        first_due_billing_value = DueBillingValue(original_value=first_value)
        first_calendar = DueBillingCalendar(
            due_date=FuncTestUtils.get_string("First billing dueDate (yyyy-MM-dd)")
        )

        second_tx_id = FuncTestUtils.get_string("Second billing txId")
        second_value = FuncTestUtils.get_string("Second billing value(99.99)")
        second_key = FuncTestUtils.get_string("Second billing key")
        second_due_billing_value = DueBillingValue(original_value=second_value)
        second_calendar = DueBillingCalendar(
            due_date=FuncTestUtils.get_string("Second billing dueDate (yyyy-MM-dd)")
        )

        debtor = Debtor(cpf=document, name=name)

        due_billing1 = DueBilling(
            txid=first_tx_id,
            calendar=first_calendar,
            debtor=debtor,
            value=first_due_billing_value,
            key=first_key
        )

        due_billing2 = DueBilling(
            txid=second_tx_id,
            calendar=second_calendar,
            debtor=debtor,
            value=second_due_billing_value,
            key=second_key
        )

        due_billing_list = [due_billing1, due_billing2]

        batch = IncludeDueBillingBatchRequest(
            description=batch_description,
            due_billings=due_billing_list
        )

        self.pix_sdk.review_due_billing_batch(batch_id, batch)
        print("Due billing batch reviewed.")

    def test_pix_include_immediate_billing(self) -> None:
        """
        Includes an immediate billing request for PIX payments.
        
        Raises:
            SdkException: If an error occurs during the inclusion of the immediate billing.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Include immediate billing:")

        document = FuncTestUtils.get_string("cnpj")
        name = FuncTestUtils.get_string("name")
        value = FuncTestUtils.get_string("value(99.99)")
        key = FuncTestUtils.get_string("key")
        expiration = 86400

        debtor = Debtor(cnpj=document, name=name)
        pix_value = PixValue(original=value)
        calendar = Calendar(expiration=expiration)
        pix_billing = PixBilling(
            debtor=debtor,
            value=pix_value,
            key=key,
            calendar=calendar
        )

        generated_immediate_billing = self.pix_sdk.include_immediate_billing(pix_billing)
        print(json.dumps(generated_immediate_billing.to_dict(), indent=4))

    def test_pix_include_immediate_billing_tx_id(self) -> None:
        """
        Includes an immediate billing request for PIX payments with a transaction ID.
        
        Raises:
            SdkException: If an error occurs during the inclusion of the immediate billing.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Include immediate billing:")

        tx_id = FuncTestUtils.get_string("txId")
        document = FuncTestUtils.get_string("cnpj")
        name = FuncTestUtils.get_string("name")
        value = FuncTestUtils.get_string("value(99.99)")
        key = FuncTestUtils.get_string("key")
        expiration = 86400

        debtor = Debtor(cnpj=document, name=name)
        pix_value = PixValue(original=value)
        calendar = Calendar(expiration=expiration)
        pix_billing = PixBilling(
            txid=tx_id,
            debtor=debtor,
            value=pix_value,
            key=key,
            calendar=calendar
        )

        generated_immediate_billing  = self.pix_sdk.include_immediate_billing(pix_billing)
        print(json.dumps(generated_immediate_billing.to_dict(), indent=4))

    def test_pix_retrieve_immediate_billing(self) -> None:
        """
        Retrieves detailed information for a specific immediate billing request by transaction ID.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the immediate billing.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving immediate billing...")

        tx_id = FuncTestUtils.get_string("txId")

        detailed_immediate_pix_billing = self.pix_sdk.retrieve_immediate_billing(tx_id)
        print(json.dumps(detailed_immediate_pix_billing.to_dict(), indent=4))

    def test_pix_retrieve_immediate_billing_collection(self) -> None:
        """
        Retrieves a list of immediate billings within a specified date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the immediate billing list.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving immediate billing list...")

        initial_date = FuncTestUtils.get_string("initialDate(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        final_date = FuncTestUtils.get_string("finalDate(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        filter = RetrieveImmediateBillingsFilter()
        
        detailed_immediate_pix_billings = self.pix_sdk.retrieve_immediate_billing_list(initial_date, final_date, filter)
        detailed_immediate_pix_billing_dict = [detailed_immediate_pix_billing.to_dict() for detailed_immediate_pix_billing in detailed_immediate_pix_billings]
        print(json.dumps(detailed_immediate_pix_billing_dict, indent=4))

    def test_pix_retrieve_immediate_billing_collection_page(self) -> None:
        """
        Retrieves a paginated list of immediate billings within a specified date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the immediate billing collection page.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving immediate billing list...")

        initial_date = FuncTestUtils.get_string("initialDate(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        final_date = FuncTestUtils.get_string("finalDate(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        filter = RetrieveImmediateBillingsFilter()
        page = 0
        page_size = 10

        billing_page = self.pix_sdk.retrieve_immediate_billing_page(initial_date, final_date, page, page_size, filter)
        print(json.dumps(billing_page.to_dict(), indent=4))

    def test_pix_review_immediate_billing(self) -> None:
        """
        Reviews an immediate billing request for PIX payments.
        
        Raises:
            SdkException: If an error occurs during the review of the immediate billing.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Review immediate billing list:")

        tx_id = FuncTestUtils.get_string("txId")
        document = FuncTestUtils.get_string("cnpj")
        name = FuncTestUtils.get_string("name")
        value = FuncTestUtils.get_string("value(99.99)")
        key = FuncTestUtils.get_string("key")
        expiration = 86400  # Expiração em segundos

        debtor = Debtor(cnpj=document, name=name)
        pix_value = PixValue(original=value)
        calendar = Calendar(expiration=expiration)
        pix_billing = PixBilling(
            txid=tx_id,
            debtor=debtor,
            value=pix_value,
            key=key,
            calendar=calendar
        )

        generated_immediate_billing = self.pix_sdk.review_immediate_billing(pix_billing)
        print(json.dumps(generated_immediate_billing.to_dict(), indent=4))

    def test_pix_include_location(self) -> None:
        """
        Includes a new location for PIX payment.
        
        Raises:
            SdkException: If an error occurs during the inclusion of the location.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Including location...")

        cob_type = ImmediateBillingType.cob

        location = self.pix_sdk.include_location(cob_type)
        print(json.dumps(location.to_dict(), indent=4))

    def test_pix_retrieve_location(self) -> None:
        """
        Retrieves a specific location by its ID.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the location.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving location...")

        location_id = FuncTestUtils.get_string("locationId")

        location = self.pix_sdk.retrieve_location(location_id)
        print(json.dumps(location.to_dict(), indent=4))

    def test_pix_retrieve_location_list(self) -> None:
        """
        Retrieves a list of locations within a specified date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the location list.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving location list...")

        initial_date = FuncTestUtils.get_string("initialDate(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        final_date = FuncTestUtils.get_string("finalDate(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        filter = RetrieveLocationFilter()
        
        locations = self.pix_sdk.retrieve_locations_list(initial_date, final_date, filter)
        locations_dict = [location.to_dict() for location in locations]
        print(json.dumps(locations_dict, indent=4))

    def test_pix_retrieve_location_list_page(self) -> None:
        """
        Retrieves a paginated list of locations within a specified date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the location list page.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving location list page...")

        initial_date = FuncTestUtils.get_string("initialDate(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        final_date = FuncTestUtils.get_string("finalDate(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        filter = RetrieveLocationFilter()
        page = 0
        page_size = 10

        location_page = self.pix_sdk.retrieve_locations_page(initial_date, final_date, page, page_size, filter)
        print(json.dumps(location_page.to_dict(), indent=4))

    def test_pix_unlink_location(self) -> None:
        """
        Unlinks a specific location by its ID.
        
        Raises:
            SdkException: If an error occurs during the unlinking of the location.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Unlink location:")

        location_id = FuncTestUtils.get_string("locationId")

        location = self.pix_sdk.unlink_location(location_id)

        print(json.dumps(location.to_dict(), indent=4))

    def test_pix_request_devolution(self) -> None:
        """
        Requests a devolution for a specific transaction.
        
        Raises:
            SdkException: If an error occurs during the devolution request.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Request devolution:")

        e2e_id = FuncTestUtils.get_string("e2eId")
        devolution_identifier = FuncTestUtils.get_string("devolutionIdentifier")
        value = FuncTestUtils.get_string("value(99.99)")
        description = FuncTestUtils.get_string("description")
        devolution_nature = DevolutionNature.ORIGINAL

        devolution = DevolutionRequestBody(
            value=value,
            nature=devolution_nature,
            description=description
        )

        detailed_devolution = self.pix_sdk.request_devolution(e2e_id, devolution_identifier, devolution)

        print(json.dumps(detailed_devolution.to_dict(), indent=4))

    def test_pix_retrieve_devolution(self) -> None:
        """
        Retrieves detailed information about a specific devolution request.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the devolution.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving devolution...")

        e2e_id = FuncTestUtils.get_string("e2eId")
        devolution_identifier = FuncTestUtils.get_string("devolutionIdentifier")

        detailed_devolution = self.pix_sdk.retrieve_devolution(e2e_id, devolution_identifier)

        print(json.dumps(detailed_devolution.to_dict(), indent=4))

    def test_pix_retrieve_pix_list(self) -> None:
        """
        Retrieves a list of PIX transactions within a specified date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the PIX list.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving pix list...")

        initial_date = FuncTestUtils.get_string("initialDate(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        final_date = FuncTestUtils.get_string("finalDate(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        filter = RetrievedPixFilter()

        detailed_pix_list = self.pix_sdk.retrieve_pix_list(initial_date, final_date, filter)
        detailed_pix_list_dict = [pix.to_dict() for pix in detailed_pix_list]
        print(json.dumps(detailed_pix_list_dict, indent=4))

    def test_pix_retrieve_pix_list_page(self) -> None:
        """
        Retrieves a paginated list of PIX transactions within a specified date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the PIX list page.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving pix list page...")

        initial_date = FuncTestUtils.get_string("initialDate(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        final_date = FuncTestUtils.get_string("finalDate(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        filter = RetrievedPixFilter()
        page = 0
        page_size = 10

        pix_page = self.pix_sdk.retrieve_pix_page(initial_date, final_date, page, page_size, filter)

        print(json.dumps(pix_page.to_dict(), indent=4))

    def test_pix_retrieve_pix(self) -> None:
        """
        Retrieves detailed information about a specific PIX transaction by its end-to-end ID.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the PIX transaction.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving pix...")

        e2e_id = FuncTestUtils.get_string("e2eId")

        pix = self.pix_sdk.retrieve_pix(e2e_id)

        print(json.dumps(pix.to_dict(), indent=4))

    def test_billing_retrieve_callbacks(self) -> None:
        """
        Retrieves a list of callbacks within a specified date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the callbacks.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving callbacks...")

        initial_date_hour = FuncTestUtils.get_string("initialDateHour(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        final_date_hour = FuncTestUtils.get_string("finalDateHour(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        filter = CallbackRetrieveFilter()

        callbacks = self.pix_sdk.retrieve_callbacks_in_range(initial_date_hour, final_date_hour, filter)
        callbacks_dict = [callback.to_dict() for callback in callbacks]
        print(json.dumps(callbacks_dict, indent=4))

    def test_billing_retrieve_callbacks_page(self) -> None:
        """
        Retrieves a paginated list of callbacks within a specified date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the callback page.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving callback page...")

        initial_date_hour = FuncTestUtils.get_string("initialDateHour(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        final_date_hour = FuncTestUtils.get_string("finalDateHour(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        filter = CallbackRetrieveFilter()
        page = 0
        page_size = 10

        callbacks_page = self.pix_sdk.retrieve_callbacks_page(initial_date_hour, final_date_hour, page, page_size, filter)
        print(json.dumps(callbacks_page.to_dict(), indent=4))

    def test_billing_include_webhook(self) -> None:
        """
        Includes a new webhook for billing notifications.
        
        Raises:
            SdkException: If an error occurs during the inclusion of the webhook.
        """
        print("Include webhook:")

        webhook_url = FuncTestUtils.get_string("webhookUrl")
        key = FuncTestUtils.get_string("key")

        self.pix_sdk.include_webhook(key, webhook_url)
        print("Webhook included.")

    def test_billing_retrieve_webhook(self) -> None:
        """
        Retrieves the webhook associated with a specific key.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the webhook.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving webhook...")

        key = FuncTestUtils.get_string("key")

        webhook = self.pix_sdk.retrieve_webhook(key)
        print(json.dumps(webhook.to_dict(), indent=4))

    def test_billing_delete_webhook(self) -> None:
        """
        Deletes a webhook associated with a specific key.
        
        Raises:
            SdkException: If an error occurs during the deletion of the webhook.
        """
        print("Deleting webhook...")

        key = FuncTestUtils.get_string("key")

        self.pix_sdk.delete_webhook(key)
        print("Webhook deleted.")