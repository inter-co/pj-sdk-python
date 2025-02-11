from functional_tests.BankingFunctionalTests import BankingFunctionalTests

class BankingMenu:
    RETRIEVE_STATEMENT = 1
    RETRIEVE_STATEMENT_PDF = 2
    RETRIEVE_ENRICHED_STATEMENT = 3
    RETRIEVE_ENRICHED_STATEMENT_PAGINATION = 4
    RETRIEVE_BALANCE = 5
    INCLUDE_PAYMENT = 6
    SEARCH_PAYMENTS = 7
    INCLUDE_DARF_PAYMENT = 8
    SEARCH_DARF_PAYMENTS = 9
    INCLUDE_PAYMENT_BATCH = 10
    SEARCH_PAYMENT_BATCH = 11
    CANCEL_SCHEDULING = 12
    INCLUDE_PIX_KEY = 13
    GET_PIX = 14
    CREATE_WEBHOOK = 15
    GET_WEBHOOK = 16
    DELETE_WEBHOOK = 17
    RETRIEVE_CALLBACKS = 18
    RETRIEVE_CALLBACKS_PAGINATION = 19

    def show_menu(self, environment: str) -> int:
        """
        Displays a menu for various banking operations and returns the user's choice.
        
        Args:
            environment (str): The current environment (e.g. development, production).
        
        Returns:
            int: The option selected by the user.
        """
        print("ENVIRONMENT", environment)
        print(f"{self.RETRIEVE_STATEMENT} - Retrieve Bank Statement")
        print(f"{self.RETRIEVE_STATEMENT_PDF} - Retrieve Bank Statement PDF")
        print(f"{self.RETRIEVE_ENRICHED_STATEMENT} - Retrieve Enriched Bank Statement")
        print(f"{self.RETRIEVE_ENRICHED_STATEMENT_PAGINATION} - Retrieve Enriched Bank Statement with pagination")
        print(f"{self.RETRIEVE_BALANCE} - Retrieve Balance (current day)")
        print(f"{self.INCLUDE_PAYMENT} - Include Payment for billet")
        print(f"{self.SEARCH_PAYMENTS} - Search Payments for billet")
        print(f"{self.INCLUDE_DARF_PAYMENT} - Include DARF Payment")
        print(f"{self.SEARCH_DARF_PAYMENTS} - Search DARF Payments")
        print(f"{self.INCLUDE_PAYMENT_BATCH} - Include Payments in Batch")
        print(f"{self.SEARCH_PAYMENT_BATCH} - Search Payment Batch")
        print(f"{self.CANCEL_SCHEDULING} - Cancel payment scheduling")
        print(f"{self.INCLUDE_PIX_KEY} - Include Pix payment by Key")
        print(f"{self.GET_PIX} - Get Pix payment details")
        print(f"{self.CREATE_WEBHOOK} - Create Webhook")
        print(f"{self.GET_WEBHOOK} - Get Webhook")
        print(f"{self.DELETE_WEBHOOK} - Delete Webhook")
        print(f"{self.RETRIEVE_CALLBACKS} - Retrieve callbacks")
        print(f"{self.RETRIEVE_CALLBACKS_PAGINATION} - Retrieve callbacks with pagination")
        print("0 - Exit")
        choice = input("=> ")
        
        try:
            return int(choice)
        except ValueError:
            print("Invalid option")
            return self.show_menu(environment)
        
    def execute(self, op: int, inter_sdk) -> None:
        """
        Executes a selected banking operation based on the provided option.
        
        Args:
            op (int): The operation code to execute.
            inter_sdk: An instance of the InterSdk for executing banking operations.
        
        Raises:
            SdkException: If an error occurs during the execution of the operation.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        banking_functional_tests = BankingFunctionalTests(inter_sdk)
        
        if op == self.RETRIEVE_STATEMENT:
            banking_functional_tests.test_banking_statement()
        elif op == self.RETRIEVE_STATEMENT_PDF:
            banking_functional_tests.test_banking_statement_pdf()
        elif op == self.RETRIEVE_ENRICHED_STATEMENT:
            banking_functional_tests.test_banking_enriched_statement()
        elif op == self.RETRIEVE_ENRICHED_STATEMENT_PAGINATION:
            banking_functional_tests.test_banking_enriched_statement_page()
        elif op == self.RETRIEVE_BALANCE:
            banking_functional_tests.test_banking_balance()
        elif op == self.INCLUDE_PAYMENT:
            banking_functional_tests.test_banking_include_payment()
        elif op == self.SEARCH_PAYMENTS:
            banking_functional_tests.test_banking_retrieve_payment_list()
        elif op == self.INCLUDE_DARF_PAYMENT:
            banking_functional_tests.test_banking_include_darf_payment()
        elif op == self.SEARCH_DARF_PAYMENTS:
            banking_functional_tests.test_banking_retrieve_darf_payment()
        elif op == self.INCLUDE_PAYMENT_BATCH:
            banking_functional_tests.test_banking_include_payment_batch()
        elif op == self.CANCEL_SCHEDULING:
            banking_functional_tests.test_banking_cancel_payment()
        elif op == self.SEARCH_PAYMENT_BATCH:
            banking_functional_tests.test_banking_retrieve_payment_batch()
        elif op == self.INCLUDE_PIX_KEY:
            banking_functional_tests.test_banking_include_pix()
        elif op == self.GET_PIX:
            banking_functional_tests.test_banking_retrieve_pix()
        elif op == self.CREATE_WEBHOOK:
            banking_functional_tests.test_banking_include_webhook()
        elif op == self.GET_WEBHOOK:
            banking_functional_tests.test_banking_retrieve_webhook()
        elif op == self.DELETE_WEBHOOK:
            banking_functional_tests.test_banking_delete_webhook()
        elif op == self.RETRIEVE_CALLBACKS:
            banking_functional_tests.test_banking_retrieve_callbacks()
        elif op == self.RETRIEVE_CALLBACKS_PAGINATION:
            banking_functional_tests.test_banking_retrieve_callback_paginated()

        print()