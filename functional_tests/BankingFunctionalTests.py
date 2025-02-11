import json

from functional_tests.utils.FuncTestUtils import FuncTestUtils
from inter_sdk_python.InterSdk import InterSdk
from inter_sdk_python.banking.enums.DarfPaymentDateType import DarfPaymentDateType
from inter_sdk_python.banking.enums.OperationType import OperationType
from inter_sdk_python.banking.enums.PaymentDateType import PaymentDateType
from inter_sdk_python.banking.models.Batch import BilletBatch, DarfPaymentBatch
from inter_sdk_python.banking.models.BilletPayment import BilletPayment
from inter_sdk_python.banking.models.CallbackRetrieveFilter import CallbackRetrieveFilter
from inter_sdk_python.banking.models.DarfPayment import DarfPayment
from inter_sdk_python.banking.models.DarfPaymentSearchFilter import DarfPaymentSearchFilter
from inter_sdk_python.banking.models.FilterRetrieveEnrichedStatement import FilterRetrieveEnrichedStatement
from inter_sdk_python.banking.models.Key import Key
from inter_sdk_python.banking.models.PaymentSearchFilter import PaymentSearchFilter
from inter_sdk_python.banking.models.Pix import Pix

class BankingFunctionalTests:
    def __init__(self, inter_sdk: InterSdk):
        self.banking_sdk = inter_sdk.banking()

    def test_banking_statement(self) -> None:
        """
        Retrieves and prints the banking statement for a specified period.
        Raises:
            SdkException: If an error occurs during the retrieval of the statement.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving statement...")

        initial_date = FuncTestUtils.get_string("initialDate(YYYY-MM-DD)")
        final_date = FuncTestUtils.get_string("finalDate(YYYY-MM-DD)")

        statement = self.banking_sdk.retrieve_statement(initial_date, final_date)
        print(json.dumps(statement.to_dict(), indent=4))

    def test_banking_statement_pdf(self) -> None:
        """
        Retrieves the banking statement in PDF format and saves it to a file.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the statement.
        """
        print("Retrieving statement in pdf...")

        initial_date = FuncTestUtils.get_string("initialDate(YYYY-MM-DD)")
        final_date = FuncTestUtils.get_string("finalDate(YYYY-MM-DD)")
        file = "statement.pdf"

        self.banking_sdk.retrieve_statement_in_pdf(initial_date, final_date, file)
        print(f"Generated file: {file}")

    def test_banking_enriched_statement(self) -> None:
        """
        Retrieves the enriched banking statement for a specified period.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the statement.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving enriched statement...")

        initial_date = FuncTestUtils.get_string("initialDate(YYYY-MM-DD)")
        final_date = FuncTestUtils.get_string("finalDate(YYYY-MM-DD)")
        filter = FilterRetrieveEnrichedStatement(OperationType.C.name)

        enriched_transactions = self.banking_sdk.retrieve_enriched_statement_with_range(initial_date, final_date, filter)
        transactions_dict = [transaction.to_dict() for transaction in enriched_transactions]
        print(json.dumps(transactions_dict, indent=4))

    def test_banking_enriched_statement_page(self) -> None:
        """
        Retrieves a page of enriched banking statements for a specified period.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the statement.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving enriched statement page...")

        initial_date = FuncTestUtils.get_string("initialDate(YYYY-MM-DD)")
        final_date = FuncTestUtils.get_string("finalDate(YYYY-MM-DD)")
        filter_retrieve = FilterRetrieveEnrichedStatement(OperationType.C.name)
        page = 0
        pagesize = 10

        enriched_transactions = self.banking_sdk.retrieve_enriched_statement(initial_date, final_date, filter_retrieve, page, pagesize)
        print(json.dumps(enriched_transactions.to_dict(), indent=4))

    def test_banking_balance(self) -> None:
        """
        Retrieves the banking balance for a specified date.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the balance.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving balance...")
        balance = self.banking_sdk.retrieve_balance(None)
        print(json.dumps(balance.to_dict(), indent=4))

    def test_banking_include_payment(self) -> None:
        """
        Includes a payment to be processed.
        
        Raises:
            SdkException: If an error occurs during the payment inclusion.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Include payment:")

        bar_code = FuncTestUtils.get_string("barCode")
        value = FuncTestUtils.get_big_decimal("value(99.99)")
        due_date = FuncTestUtils.get_string("dueDate(YYYY-MM-DD)")
        payment_date = FuncTestUtils.get_string("payment_date(YYYY-MM-DD)")

        payment = BilletPayment(barcode=bar_code, amount_to_pay=value, due_date=due_date, payment_date=payment_date)

        payment_response = self.banking_sdk.include_payment(payment)
        print(json.dumps(payment_response.to_dict(), indent=4))

    def test_banking_cancel_payment(self) -> None:
        """
        Cancels a scheduled payment.
        
        Raises:
            SdkException: If an error occurs during the cancellation of the payment.
        """
        print("Canceling payment:")

        request_code = FuncTestUtils.get_string("requestCode")

        self.banking_sdk.payment_scheduling_cancel(request_code)

        print("Payment canceled.")

    def test_banking_retrieve_payment_list(self) -> None:
        """
        Retrieves a list of payments for a specified date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the payment list.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving payment list...")

        initial_date = FuncTestUtils.get_string("initialDate(YYYY-MM-DD)")
        final_date = FuncTestUtils.get_string("finalDate(YYYY-MM-DD)")
        filter = PaymentSearchFilter(filter_date_by=PaymentDateType.PAGAMENTO.name)

        payments = self.banking_sdk.retrieve_payment(initial_date, final_date, filter)
        payments_dict = [payment.to_dict() for payment in payments]
        print(json.dumps(payments_dict, indent=4))

    def test_banking_include_darf_payment(self) -> None:
        """
        Includes a DARF payment.
        
        Raises:
            SdkException: If an error occurs during the inclusion of the DARF payment.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Include DARF payment:")

        document = FuncTestUtils.get_string("document")
        codigo_receita = FuncTestUtils.get_string("codigoReceita")
        due_date = FuncTestUtils.get_string("dueDate(YYYY-MM-DD)")
        description = FuncTestUtils.get_string("description")
        enterprise = FuncTestUtils.get_string("enterprise")
        calculation_period = FuncTestUtils.get_string("calculationPeriod(YYYY-MM-DD)")
        principal_value = FuncTestUtils.get_string("principalValue(99.99)")
        reference = FuncTestUtils.get_string("reference")

        darf_payment = DarfPayment(
            cnpj_or_cpf=document,
            revenue_code=codigo_receita,
            due_date=due_date,
            description=description,
            enterprise_name=enterprise,
            assessment_period=calculation_period,
            principal_value=principal_value,
            reference=reference
        )

        darf_payment_response = self.banking_sdk.include_darf_payment(darf_payment)
        print(json.dumps(darf_payment_response.to_dict(), indent=4))

    def test_banking_retrieve_darf_payment(self) -> None:
        """
        Retrieves a list of DARF payments for a specified date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of DARF payments.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving DARF payment...")

        initial_date = FuncTestUtils.get_string("initialDate(YYYY-MM-DD)")
        final_date = FuncTestUtils.get_string("finalDate(YYYY-MM-DD)")
        filter = DarfPaymentSearchFilter(filter_date_by=DarfPaymentDateType.PAGAMENTO.name)

        retrieve_darf_payments = self.banking_sdk.retrieve_darf_payments(initial_date, final_date, filter)
        transactions_dict = [darf.to_dict() for darf in retrieve_darf_payments]
        print(json.dumps(transactions_dict, indent=4))

    def test_banking_include_payment_batch(self) -> None:
        """
        Includes a batch of payments consisting of billet and DARF payments.
        
        Raises:
            SdkException: If an error occurs during the inclusion of the payment batch.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Include batch of payments:")

        print("Billet payment: ")
        bar_code = FuncTestUtils.get_string("barCode")
        billet_value = FuncTestUtils.get_big_decimal("billetValue")
        billet_due_date = FuncTestUtils.get_string("billetDueDate(YYYY-MM-DD)")
        
        print("DARF payment: ")
        document = FuncTestUtils.get_string("document(cpf)")
        codigo_receita = FuncTestUtils.get_string("codigoReceita")
        daf_due_date = FuncTestUtils.get_string("darfDueDate(YYYY-MM-DD)")
        description = FuncTestUtils.get_string("description")
        enterprise = FuncTestUtils.get_string("enterprise")
        calculation_period = FuncTestUtils.get_string("calculationPeriod")
        darf_value = FuncTestUtils.get_string("darfValue(99.99)")
        reference = FuncTestUtils.get_string("reference")
        my_identifier = FuncTestUtils.get_string("batch identifier")

        billet_batch = BilletBatch(
            barcode=bar_code,
            amount_to_pay=billet_value,
            due_date=billet_due_date
        )

        darf_batch = DarfPaymentBatch(
            cnpj_or_cpf=document,
            revenue_code=codigo_receita,
            due_date=daf_due_date,
            description=description,
            enterprise_name=enterprise,
            assessment_period=calculation_period,
            principal_value=darf_value,
            reference=reference
        )

        payments = [billet_batch, darf_batch]

        batch_payment_response = self.banking_sdk.include_batch_payment(my_identifier, payments)
        print(json.dumps(batch_payment_response.to_dict(), indent=4))

    def test_banking_retrieve_payment_batch(self) -> None:
        """
        Retrieves a batch of payments by its identifier.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the payment batch.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving batch of payments...")

        batch_id = FuncTestUtils.get_string("batchId")

        batch_processing = self.banking_sdk.retrieve_payment_batch(batch_id)
        print(json.dumps(batch_processing.to_dict(), indent=4))

    def test_banking_include_pix(self) -> None:
        """
        Includes a PIX payment.
        
        Raises:
            SdkException: If an error occurs during the inclusion of the PIX.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Include pix:")

        key = FuncTestUtils.get_string("key")
        value = FuncTestUtils.get_string("value(99.99)")

        recipient = Key(key=key)

        pix = Pix(amount=value, recipient=recipient)

        include_pix_response = self.banking_sdk.include_pix(pix)
        print(json.dumps(include_pix_response.to_dict(), indent=4))

    def test_banking_retrieve_pix(self) -> None:
        """
        Retrieves a PIX payment by its request code.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the PIX.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving pix...")

        request_code = FuncTestUtils.get_string("requestCode")

        retrieve_pix_response = self.banking_sdk.retrieve_pix(request_code)
        print(json.dumps(retrieve_pix_response.to_dict(), indent=4))

    def test_banking_include_webhook(self) -> None:
        """
        Includes a webhook for payment notifications.
        
        Raises:
            SdkException: If an error occurs during the inclusion of the webhook.
        """
        print("Include webhook:")

        webhook_type = FuncTestUtils.get_string("webhookType (pix-pagamento,boleto-pagamento)")
        webhook_url = FuncTestUtils.get_string("webhookUrl")

        self.banking_sdk.include_webhook(webhook_type, webhook_url)
        print("Webhook included.")

    def test_banking_retrieve_webhook(self) -> None:
        """
        Retrieves a webhook configuration by its type.
        
        Raises:
            SdkException: If an error occurs during the retrieval of the webhook.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving webhook...")

        webhook_type = FuncTestUtils.get_string("webhookType (pix-pagamento,boleto-pagamento)")

        webhook = self.banking_sdk.retrieve_webhook(webhook_type)
        print(json.dumps(webhook.to_dict(), indent=4))

    def test_banking_delete_webhook(self) -> None:
        """
        Deletes a specified webhook.
        
        Raises:
            SdkException: If an error occurs during the deletion of the webhook.
        """
        print("Deleting webhook...")

        webhook_type = FuncTestUtils.get_string("webhookType (pix-pagamento,boleto-pagamento)")

        self.banking_sdk.delete_webhook(webhook_type)
        print("Webhook deleted.")

    def test_banking_retrieve_callbacks(self) -> None:
        """
        Retrieves a list of callbacks for a specified webhook type and date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of callbacks.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving callbacks...")

        webhook_type = FuncTestUtils.get_string("webhookType (pix-pagamento,boleto-pagamento)")
        initial_date_hour = FuncTestUtils.get_string("initialDateHour(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        final_date_hour = FuncTestUtils.get_string("finalDateHour(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        filter = CallbackRetrieveFilter()

        callbacks = self.banking_sdk.retrieve_callback(webhook_type, initial_date_hour, final_date_hour, filter)
        callbacks_dict = [callback.to_dict() for callback in callbacks]
        print(json.dumps(callbacks_dict, indent=4))

    def test_banking_retrieve_callback_paginated(self) -> None:
        """
        Retrieves a paginated list of callbacks for a specified webhook type and date range.
        
        Raises:
            SdkException: If an error occurs during the retrieval of callbacks.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        print("Retrieving callbacks...")

        webhook_type = FuncTestUtils.get_string("webhookType (pix-pagamento,boleto-pagamento)")
        initial_date_hour = FuncTestUtils.get_string("initialDateHour(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        final_date_hour = FuncTestUtils.get_string("finalDateHour(YYYY-MM-DDTHH:MM:SSZ ex:2022-04-01T10:30:00Z)")
        filter = CallbackRetrieveFilter()
        page = 0
        page_size = 10

        callbacks_page = self.banking_sdk.retrieve_callback_page(webhook_type, initial_date_hour, final_date_hour, filter, page, page_size)
        print(json.dumps(callbacks_page.to_dict(), indent=4))