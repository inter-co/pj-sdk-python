from typing import List

from inter_sdk_python.banking.balance.BalanceClient import BalanceClient
from inter_sdk_python.banking.bankstatement.BankStatementClient import BankStatementClient
from inter_sdk_python.banking.models.Balance import Balance
from inter_sdk_python.banking.models.BankStatement import BankStatement
from inter_sdk_python.banking.models.BatchItem import BatchItem
from inter_sdk_python.banking.models.BatchProcessing import BatchProcessing
from inter_sdk_python.banking.models.BilletPayment import BilletPayment
from inter_sdk_python.banking.models.CallbackPage import CallbackPage
from inter_sdk_python.banking.models.CallbackRetrieveFilter import CallbackRetrieveFilter
from inter_sdk_python.banking.models.DarfPayment import DarfPayment
from inter_sdk_python.banking.models.DarfPaymentResponse import DarfPaymentResponse
from inter_sdk_python.banking.models.DarfPaymentSearchFilter import DarfPaymentSearchFilter
from inter_sdk_python.banking.models.EnrichedBankStatementPage import EnrichedBankStatementPage
from inter_sdk_python.banking.models.EnrichedTransaction import EnrichedTransaction
from inter_sdk_python.banking.models.FilterRetrieveEnrichedStatement import FilterRetrieveEnrichedStatement
from inter_sdk_python.banking.models.IncludeBatchPaymentResponse import IncludeBatchPaymentResponse
from inter_sdk_python.banking.models.IncludeDarfPaymentResponse import IncludeDarfPaymentResponse
from inter_sdk_python.banking.models.IncludePaymentResponse import IncludePaymentResponse
from inter_sdk_python.banking.models.IncludePixResponse import IncludePixResponse
from inter_sdk_python.banking.models.Payment import Payment
from inter_sdk_python.banking.models.PaymentSearchFilter import PaymentSearchFilter
from inter_sdk_python.banking.models.Pix import Pix
from inter_sdk_python.banking.models.RetrieveCallbackResponse import RetrieveCallbackResponse
from inter_sdk_python.banking.models.RetrievePixResponse import RetrievePixResponse
from inter_sdk_python.banking.models.Transaction import Transaction
from inter_sdk_python.banking.payments.BankingPaymentClient import BankingPaymentClient
from inter_sdk_python.banking.pix.BankingPixClient import BankingPixClient
from inter_sdk_python.banking.webhooks.BankingWebhookClient import BankingWebhookClient
from inter_sdk_python.commons.models.Config import Config
from inter_sdk_python.commons.models.Webhook import Webhook


class BankingSdk:
    def __init__(self, config: Config):
        self.config = config
        self.bank_statement_client = None
        self.balance_client = None
        self.banking_payment_client = None
        self.banking_pix_client = None
        self.banking_webhook_client = None

    def retrieve_statement(self, initial_date: str, final_date: str) -> BankStatement:
        """
        Retrieves the statement for a specific period. The maximum period between the dates is 90 days.

        Args:
            initial_date (str): Starting date for the statement query in YYYY-MM-DD format.
            final_date (str): Ending date for the statement query in YYYY-MM-DD format.

        Returns:
            List[Transaction]: A list of transactions.

        Raises:
            SdkException: If there is an error during the statement retrieval process.
        
        See: https://developers.bancointer.com.br/v4/reference/extrato-1
        """
        if self.bank_statement_client is None:
            self.bank_statement_client = BankStatementClient()

        return self.bank_statement_client.retrieve_statement(self.config, initial_date, final_date)
    
    def retrieve_statement_in_pdf(self, initial_date: str, final_date: str, file: str) -> None:
        """
        Retrieves the statement in PDF format for a specific period. The maximum period between the dates is 90 days.

        Args:
            initial_date (str): Starting date for the statement export in YYYY-MM-DD format.
            final_date (str): Ending date for the statement export in YYYY-MM-DD format.
            file (str): PDF file path that will be saved.

        Raises:
            SdkException: If there is an error during the PDF statement retrieval process.

        See: https://developers.bancointer.com.br/v4/reference/extratoexport
        """
        if self.bank_statement_client is None:
            self.bank_statement_client = BankStatementClient()
        
        self.bank_statement_client.retrieve_statement_in_pdf(self.config, initial_date, final_date, file)

    def retrieve_enriched_statement(
        self, 
        initial_date: str, 
        final_date: str, 
        filter_retrieve: FilterRetrieveEnrichedStatement,
        page: int, 
        page_size: int
    ) -> EnrichedBankStatementPage:
        """
        Retrieves enriched statements with detailed information about each transaction for a specific period. The maximum period between the dates is 90 days.

        Args:
            initial_date (str): Starting date for the statement export in YYYY-MM-DD format.
            final_date (str): Ending date for the statement export in YYYY-MM-DD format.
            filter_retrieve (Optional[FilterRetrieveEnrichedStatement]): Filters for the query (optional, can be None).
            page (int): Page number starting from 0.
            page_size (int): Size of the page, default = 50.

        Returns:
            EnrichedBankStatementPage: A list of enriched transactions.

        Raises:
            SdkException: If there is an error during the enriched statement retrieval process.
        
        See: https://developers.bancointer.com.br/v4/reference/extratocomplete-1
        """
        if self.bank_statement_client is None:
            self.bank_statement_client = BankStatementClient()
        
        return self.bank_statement_client.retrieve_statement_page(self.config, initial_date, final_date, page, page_size, filter_retrieve)
    
    def retrieve_enriched_statement_with_range(
        self, 
        initial_date: str, 
        final_date: str, 
        filter: FilterRetrieveEnrichedStatement
    ) -> list[EnrichedBankStatementPage]:
        """
        Retrieves enriched statements within a date range using the specified filters.

        Args:
            initial_date (str): Starting date for the query in YYYY-MM-DD format.
            final_date (str): Ending date for the query in YYYY-MM-DD format.
            filter (Optional[FilterRetrieveEnrichedStatement]): Filters for the query (optional, can be None).

        Returns:
            List[EnrichedTransaction]: A list of enriched transactions.

        Raises:
            SdkException: If there is an error during the enriched statement retrieval process.
        
        See: https://developers.bancointer.com.br/v4/reference/extratocomplete
        """
        if self.bank_statement_client is None:
            self.bank_statement_client = BankStatementClient()
        
        return self.bank_statement_client.retrieve_statement_with_range(self.config, initial_date, final_date, filter)
    
    def retrieve_enriched_statement_page(
        self, 
        initial_date: str, 
        final_date: str, 
        filter: FilterRetrieveEnrichedStatement, 
        page: int
    ) -> BankStatement:
        """
        Retrieves enriched statements with detailed information about each transaction for a specific period. The maximum period between the dates is 90 days.

        Args:
            initial_date (str): Starting date for the statement export in YYYY-MM-DD format.
            final_date (str): Ending date for the statement export in YYYY-MM-DD format.
            filter (Optional[FilterRetrieveEnrichedStatement]): Filters for the query (optional, can be None).
            page (int): Page number starting from 0.

        Returns:
            EnrichedBankStatementPage: A list of enriched transactions.

        Raises:
            SdkException: If there is an error during the enriched statement retrieval process.
        
        See: https://developers.bancointer.com.br/v4/reference/extratocomplete-1
        """
        if self.bank_statement_client is None:
            self.bank_statement_client = BankStatementClient()
        
        return self.bank_statement_client.retrieve_statement(self.config, initial_date, final_date, page, None, filter)
    
    def retrieve_balance(self, balance_date: str) -> Balance:
        """
        Retrieves the balance for a specific period.

        Args:
            balance_date (str): Date for querying the positional balance in YYYY-MM-DD format.

        Returns:
            Balance: An object containing the account balances as of the specified date.

        Raises:
            SdkException: If there is an error during the balance retrieval process.
        
        See: https://developers.bancointer.com.br/v4/reference/saldo-1
        """
        if self.balance_client is None:
            self.balance_client = BalanceClient()
        
        return self.balance_client.retrieve_balance(self.config, balance_date)
    
    def include_payment(self, payment: BilletPayment) -> IncludePaymentResponse:
        """
        Method for including an immediate payment or scheduling the payment of a billet, agreement, or tax with a barcode.

        Args:
            payment (BilletPayment): Payment data.

        Returns:
            IncludePaymentResponse: An object containing quantity of approvers, payment status, transaction code, etc.

        Raises:
            SdkException: If there is an error during the payment inclusion process.
        
        See: https://developers.bancointer.com.br/v4/reference/pagarboleto
        """
        if self.banking_payment_client is None:
            self.banking_payment_client = BankingPaymentClient()
        
        return self.banking_payment_client.include_billet_payment(self.config, payment)
    
    def retrieve_payment(
        self, 
        initial_date: str, 
        final_date: str, 
        filter: PaymentSearchFilter
    ) -> List[Payment]:
        """
        Retrieves information about billets payments.

        Args:
            initial_date (str): Starting date, according to the "filterDateBy" field. Accepted format: YYYY-MM-DD.
            final_date (str): Ending date, according to the "filterDateBy" field. Accepted format: YYYY-MM-DD.
            filter (Optional[PaymentSearchFilter]): Filters for the query (optional, can be None).

        Returns:
            List[Payment]: A list of payments.

        Raises:
            SdkException: If there is an error during the payment retrieval process.
        
        See: https://developers.bancointer.com.br/v4/reference/buscarinformacoespagamentos
        """
        if self.banking_payment_client is None:
            self.banking_payment_client = BankingPaymentClient()
        
        return self.banking_payment_client.retrieve_payment_list_in_range(self.config, initial_date, final_date, filter)
    
    def include_darf_payment(self, payment: DarfPayment) -> IncludeDarfPaymentResponse:
        """
        Method for including an immediate DARF payment without a barcode.

        Args:
            payment (DarfPayment): Payment data.

        Returns:
            IncludeDarfPaymentResponse: An object containing authentication, operation number, return type, transaction code, etc.

        Raises:
            SdkException: If there is an error during the DARF payment inclusion process.
        
        See: https://developers.bancointer.com.br/v4/reference/pagamentosdarf-1
        """
        if self.banking_payment_client is None:
            self.banking_payment_client = BankingPaymentClient()
        
        return self.banking_payment_client.include_darf_payment(self.config, payment)
    
    def retrieve_darf_payments(
        self, 
        initial_date: str, 
        final_date: str, 
        filter: DarfPaymentSearchFilter
    ) -> List[DarfPaymentResponse]:
        """
        Retrieves information about DARF payments.

        Args:
            initial_date (str): Starting date, according to the "filterDateBy" field. Accepted format: YYYY-MM-DD.
            final_date (str): Ending date, according to the "filterDateBy" field. Accepted format: YYYY-MM-DD.
            filter (Optional[DarfPaymentSearchFilter]): Filters for the query (optional, can be None).

        Returns:
            List[DarfPaymentResponse]: A list of DARF payments.

        Raises:
            SdkException: If there is an error during the DARF payment retrieval process.
        
        See: https://developers.bancointer.com.br/v4/reference/buscarinformacoespagamentodarf
        """
        if self.banking_payment_client is None:
            self.banking_payment_client = BankingPaymentClient()
        
        return self.banking_payment_client.retrieve_darf_list(self.config, initial_date, final_date, filter)

    def include_batch_payment(
        self, 
        my_identifier: str, 
        payments: List[BatchItem]
    ) -> IncludeBatchPaymentResponse:
        """
        Inclusion of a batch of payments entered by the client.

        Args:
            my_identifier (str): Identifier for the batch for the client.
            payments (List[BatchItem]): Payments to be processed.

        Returns:
            IncludeBatchPaymentResponse: Information regarding the batch processing.

        Raises:
            SdkException: If there is an error during the batch payment inclusion process.
        
        See: https://developers.bancointer.com.br/v4/reference/pagamentoslote
        """
        if self.banking_payment_client is None:
            self.banking_payment_client = BankingPaymentClient()
        
        return self.banking_payment_client.include_batch_payment(self.config, my_identifier, payments)
    
    def retrieve_payment_batch(self, batch_id: str) -> BatchProcessing:
        """
        Retrieves a batch of payments entered by the client.

        Args:
            batch_id (str): Identifier for the batch.

        Returns:
            BatchProcessing: Information regarding the batch processing.

        Raises:
            SdkException: If there is an error during the batch payment retrieval process.
        
        See: https://developers.bancointer.com.br/v4/reference/buscarinformacoespagamentolote
        """
        if self.banking_payment_client is None:
            self.banking_payment_client = BankingPaymentClient()
        
        return self.banking_payment_client.retrieve_payment_batch(self.config, batch_id)
    
    def include_pix(self, pix: Pix) -> IncludePixResponse:
        """
        Method for including a Pix payment/transfer using banking data or a key.

        Args:
            pix (Pix): Pix data.

        Returns:
            IncludePixResponse: An object containing endToEndId, etc.

        Raises:
            SdkException: If there is an error during the Pix payment inclusion process.
        
        See: https://developers.bancointer.com.br/v4/reference/realizarpagamentopix-1
        """
        if self.banking_pix_client is None:
            self.banking_pix_client = BankingPixClient()
        
        return self.banking_pix_client.include_pix(self.config, pix)
    
    def retrieve_pix(self, request_code: str) -> RetrievePixResponse:
        """
        Method for retrieving a Pix payment/transfer.

        Args:
            request_code (str): Pix data.

        Returns:
            RetrievePixResponse: An object containing endToEndId, etc.

        Raises:
            SdkException: If there is an error during the Pix retrieval process.
        
        See: https://developers.bancointer.com.br/v4/reference/realizarpagamentopix-1
        """
        if self.banking_pix_client is None:
            self.banking_pix_client = BankingPixClient()
        
        return self.banking_pix_client.retrieve_pix(self.config, request_code)

    def include_webhook(self, webhook_type: str, webhook_url: str) -> None:
        """
        Method intended to create a webhook to receive notifications for confirmation of Pix payments (callbacks).

        Args:
            webhook_type (str): The type of the webhook.
            webhook_url (str): The client's HTTPS server URL.

        Raises:
            SdkException: If there is an error during the webhook inclusion process.
        
        See: https://developers.bancointer.com.br/v4/reference/webhookput
        """
        if self.banking_webhook_client is None:
            self.banking_webhook_client = BankingWebhookClient()
        
        self.banking_webhook_client.include_webhook(self.config, webhook_type, webhook_url)

    def retrieve_webhook(self, webhook_type: str) -> Webhook:
        """
        Retrieve the registered webhook.

        Args:
            webhook_type (str): The type of the webhook.

        Returns:
            Webhook: The registered webhook.

        Raises:
            SdkException: If there is an error during the retrieval process.
        
        See: https://developers.bancointer.com.br/v4/reference/webhookget-3
        """
        if self.banking_webhook_client is None:
            self.banking_webhook_client = BankingWebhookClient()
        
        return self.banking_webhook_client.retrieve_webhook(self.config, webhook_type)

    def delete_webhook(self, webhook_type: str) -> None:
        """
        Deletes the webhook.

        Args:
            webhook_type (str): The type of the webhook to delete.

        Raises:
            SdkException: If there is an error during the deletion process.
        
        See: https://developers.bancointer.com.br/v4/reference/webhookdelete-3
        """
        if self.banking_webhook_client is None:
            self.banking_webhook_client = BankingWebhookClient()
        
        self.banking_webhook_client.delete_webhook(self.config, webhook_type)

    def retrieve_callback(
        self, 
        webhook_type: str, 
        initial_date_hour: str, 
        final_date_hour: str, 
        filter: CallbackRetrieveFilter
    ) -> List[RetrieveCallbackResponse]:
        """
        Retrieves a collection of callbacks for a specific period, according to the provided parameters, without pagination.

        Args:
            webhook_type (str): The type of the webhook.
            initial_date_hour (str): Starting date, accepted format: YYYY-MM-DD.
            final_date_hour (str): Ending date, accepted format: YYYY-MM-DD.
            filter (Optional[CallbackRetrieveFilter]): Filters for the query (optional, can be None).

        Returns:
            List[RetrieveCallbackResponse]: A list of callback responses.

        Raises:
            SdkException: If there is an error during the retrieval process.
        
        See: https://developers.bancointer.com.br/v4/reference/pesquisarboletos
        """
        if self.banking_webhook_client is None:
            self.banking_webhook_client = BankingWebhookClient()
        
        return self.banking_webhook_client.retrieve_callbacks_in_range(self.config, webhook_type, initial_date_hour, final_date_hour, filter)

    def retrieve_callback_page(
        self, 
        webhook_type: str, 
        initial_date_hour: str, 
        final_date_hour: str, 
        filter: CallbackRetrieveFilter, 
        page: int = 1, 
        page_size: int = 10
    ) -> CallbackPage:
        """
        Retrieves a collection of billets for a specific period, according to the provided parameters, with pagination.

        Args:
            webhook_type (str): The type of the webhook.
            initial_date_hour (str): Starting date, accepted format: YYYY-MM-DD.
            final_date_hour (str): Ending date, accepted format: YYYY-MM-DD.
            filter (Optional[CallbackRetrieveFilter]): Filters for the query (optional, can be None).
            page (int): The page number to retrieve.
            page_size (int): The number of items per page.

        Returns:
            CallbackPage: A paginated response containing callbacks.

        Raises:
            SdkException: If there is an error during the retrieval process.
        
        See: https://developers.bancointer.com.br/v4/reference/pesquisarboletos
        """
        if self.banking_webhook_client is None:
            self.banking_webhook_client = BankingWebhookClient()
        
        return self.banking_webhook_client.retrieve_callbacks_page(self.config, webhook_type, initial_date_hour, final_date_hour, page, page_size, filter)

    def payment_scheduling_cancel(self, transaction_code: str) -> None:
        """
        Cancels the scheduling of a payment.

        Args:
            transaction_code (str): Unique transaction code.

        Raises:
            SdkException: If there is an error during the cancellation process.
        """
        if self.banking_payment_client is None:
            self.banking_payment_client = BankingPaymentClient()
        
        self.banking_payment_client.cancel(self.config, transaction_code)