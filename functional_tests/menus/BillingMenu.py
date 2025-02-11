from functional_tests.BillingFunctionalTests import BillingFunctionalTests

class BillingMenu:
    ISSUE_BILLING = 1
    RETRIEVE_BILLINGS = 2
    RETRIEVE_BILLING_PAGINATION = 3
    RETRIEVE_BILLING_SUMMARY = 4
    RETRIEVE_DETAILED_BILLING = 5
    RETRIEVE_BILLING_PDF = 6
    CANCEL_BILLING = 7
    CREATE_WEBHOOK = 8
    GET_WEBHOOK = 9
    DELETE_WEBHOOK = 10
    RETRIEVE_CALLBACKS = 11
    RETRIEVE_CALLBACKS_PAGINATION = 12
    
    def show_menu(self,environment: str) -> int:
        """
        Displays a menu for billing operations and returns the user's choice.
        
        Args:
            environment (str): The current environment (e.g. development, production).
        
        Returns:
            int: The option selected by the user.
        """
        print("ENVIRONMENT", environment)
        print(f"{self.ISSUE_BILLING} - Issue Billing")
        print(f"{self.RETRIEVE_BILLINGS} - Retrieve Billings")
        print(f"{self.RETRIEVE_BILLING_PAGINATION} - Retrieve Billing with pagination")
        print(f"{self.RETRIEVE_BILLING_SUMMARY} - Retrieve Billing Summary")
        print(f"{self.RETRIEVE_DETAILED_BILLING} - Retrieve Detailed Billing")
        print(f"{self.RETRIEVE_BILLING_PDF} - Retrieve Billing PDF")
        print(f"{self.CANCEL_BILLING} - Cancel Billing")
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
        Executes a selected billing operation based on the provided option.

        Args:
            op (int): The operation code to execute.
            inter_sdk: An instance of the InterSdk for executing billing operations.

        Raises:
            SdkException: If an error occurs during the execution of the operation.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        billing_functional_tests = BillingFunctionalTests(inter_sdk)
        
        if op == self.ISSUE_BILLING:
            billing_functional_tests.test_billing_issue_billing()
        elif op == self.RETRIEVE_BILLINGS:
            billing_functional_tests.test_billing_retrieve_billing_collection()
        elif op == self.RETRIEVE_BILLING_PAGINATION:
            billing_functional_tests.test_billing_retrieve_billing_collection_page()
        elif op == self.RETRIEVE_BILLING_SUMMARY:
            billing_functional_tests.test_billing_retrieve_billing_summary()
        elif op == self.RETRIEVE_DETAILED_BILLING:
            billing_functional_tests.test_billing_retrieve_billing()
        elif op == self.RETRIEVE_BILLING_PDF:
            billing_functional_tests.test_billing_retrieve_billing_pdf()
        elif op == self.CANCEL_BILLING:
            billing_functional_tests.test_billing_cancel_billing()
        elif op == self.CREATE_WEBHOOK:
            billing_functional_tests.test_billing_include_webhook()
        elif op == self.GET_WEBHOOK:
            billing_functional_tests.test_billing_retrieve_webhook()
        elif op == self.DELETE_WEBHOOK:
            billing_functional_tests.test_billing_delete_webhook()
        elif op == self.RETRIEVE_CALLBACKS:
            billing_functional_tests.test_billing_retrieve_callbacks()
        elif op == self.RETRIEVE_CALLBACKS_PAGINATION:
            billing_functional_tests.test_billing_retrieve_callbacks_page()

        print()