from functional_tests.PixFunctionalTests import PixFunctionalTests

class PixMenu:
    CREATE_IMMEDIATE_BILLING = 1
    CREATE_IMMEDIATE_BILLING_TXID = 2
    REVIEW_IMMEDIATE_BILLING = 3
    RETRIEVE_IMMEDIATE_BILLING = 4
    RETRIEVE_IMMEDIATE_BILLINGS = 5
    RETRIEVE_IMMEDIATE_BILLINGS_PAGINATION = 6
    CREATE_DUE_BILLING = 7
    REVIEW_DUE_BILLING = 8
    RETRIEVE_DUE_BILLING = 9
    RETRIEVE_DUE_BILLINGS = 10
    RETRIEVE_DUE_BILLINGS_PAGINATION = 11
    CREATE_LOCATION = 12
    RETRIEVE_LOCATION = 13
    UNLINK_LOCATION = 14
    RETRIEVE_REGISTERED_LOCATIONS = 15
    RETRIEVE_REGISTERED_LOCATIONS_PAGINATION = 16
    RETRIEVE_PIX = 17
    RETRIEVE_RECEIVED_PIX = 18
    RETRIEVE_RECEIVED_PIX_PAGINATION = 19
    REQUEST_PIX_DEVOLUTION = 20
    RETRIEVE_PIX_DEVOLUTION = 21
    RETRIEVE_DUE_BILLING_BATCH = 22
    RETRIEVE_DUE_BILLING_BATCH_PAGINATION = 23
    RETRIEVE_DUE_BILLING_BATCHES = 24
    RETRIEVE_DUE_BILLING_BATCH_SUMMARY = 25
    RETRIEVE_DUE_BILLING_BATCH_SITUATION = 26
    CREATE_DUE_BILLING_BATCH = 27
    REVIEW_DUE_BILLING_BATCH = 28
    CREATE_WEBHOOK = 29
    GET_WEBHOOK = 30
    DELETE_WEBHOOK = 31
    RETRIEVE_CALLBACKS = 32
    RETRIEVE_CALLBACKS_PAGINATION = 33


    def show_menu(self, environment: str) -> int:
        """
        Displays a menu for various billing operations and returns the user's choice.

        Args:
            environment (str): The current environment (e.g. development, production).

        Returns:
            int: The option selected by the user.
        """
        print("ENVIRONMENT", environment)
        print(f"{self.CREATE_IMMEDIATE_BILLING} - Create Immediate Billing")
        print(f"{self.CREATE_IMMEDIATE_BILLING_TXID} - Create Immediate Billing TxId")
        print(f"{self.REVIEW_IMMEDIATE_BILLING} - Review Immediate Billing")
        print(f"{self.RETRIEVE_IMMEDIATE_BILLING} - Retrieve Immediate Billing by TxId")
        print(f"{self.RETRIEVE_IMMEDIATE_BILLINGS} - Retrieve Immediate Billings")
        print(f"{self.RETRIEVE_IMMEDIATE_BILLINGS_PAGINATION} - Retrieve Immediate Billings with pagination")
        print(f"{self.CREATE_DUE_BILLING} - Create Due Billing")
        print(f"{self.REVIEW_DUE_BILLING} - Review Due Billing")
        print(f"{self.RETRIEVE_DUE_BILLING} - Retrieve Due Billing by TxId")
        print(f"{self.RETRIEVE_DUE_BILLINGS} - Retrieve Due Billings")
        print(f"{self.RETRIEVE_DUE_BILLINGS_PAGINATION} - Retrieve Due Billings with pagination")
        print(f"{self.CREATE_LOCATION} - Create Location")
        print(f"{self.RETRIEVE_LOCATION} - Retrieve Location")
        print(f"{self.UNLINK_LOCATION} - Unlink Location")
        print(f"{self.RETRIEVE_REGISTERED_LOCATIONS} - Retrieve Registered Locations")
        print(f"{self.RETRIEVE_REGISTERED_LOCATIONS_PAGINATION} - Retrieve Registered Locations with pagination")
        print(f"{self.RETRIEVE_PIX} - Retrieve Pix by e2eId")
        print(f"{self.RETRIEVE_RECEIVED_PIX} - Retrieve Received Pix")
        print(f"{self.RETRIEVE_RECEIVED_PIX_PAGINATION} - Retrieve Received Pix with pagination")
        print(f"{self.REQUEST_PIX_DEVOLUTION} - Request Devolution")
        print(f"{self.RETRIEVE_PIX_DEVOLUTION} - Retrieve Devolution")
        print(f"{self.RETRIEVE_DUE_BILLING_BATCH} - Retrieve Due Billing Batch")
        print(f"{self.RETRIEVE_DUE_BILLING_BATCH_PAGINATION} - Retrieve Due Billing Batch - Pagination")
        print(f"{self.RETRIEVE_DUE_BILLING_BATCHES} - Retrieve Due Billing Batches")
        print(f"{self.RETRIEVE_DUE_BILLING_BATCH_SUMMARY} - Retrieve Due Billing Batch - Summary")
        print(f"{self.RETRIEVE_DUE_BILLING_BATCH_SITUATION} - Retrieve Due Billing Batch - Situation")
        print(f"{self.CREATE_DUE_BILLING_BATCH} - Create Due Billing Batch")
        print(f"{self.REVIEW_DUE_BILLING_BATCH} - Review Due Billing Batch")
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
        Executes a selected Pix operation based on the provided option.
        Args:
            op (int): The operation code to execute.
            inter_sdk: An instance of the InterSdk for executing Pix operations.
        Raises:
            SdkException: If an error occurs during the execution of the operation.
            JsonProcessingException: If an error occurs during JSON processing.
        """
        pix_functional_tests = PixFunctionalTests(inter_sdk)
        if op == self.CREATE_IMMEDIATE_BILLING:
            pix_functional_tests.test_pix_include_immediate_billing()
        elif op == self.REVIEW_IMMEDIATE_BILLING:
            pix_functional_tests.test_pix_review_immediate_billing()
        elif op == self.RETRIEVE_IMMEDIATE_BILLING:
            pix_functional_tests.test_pix_retrieve_immediate_billing()
        elif op == self.CREATE_IMMEDIATE_BILLING_TXID:
            pix_functional_tests.test_pix_include_immediate_billing_tx_id()
        elif op == self.RETRIEVE_IMMEDIATE_BILLINGS:
            pix_functional_tests.test_pix_retrieve_immediate_billing_collection()
        elif op == self.RETRIEVE_IMMEDIATE_BILLINGS_PAGINATION:
            pix_functional_tests.test_pix_retrieve_immediate_billing_collection_page()
        elif op == self.CREATE_DUE_BILLING:
            pix_functional_tests.test_pix_include_due_billing()
        elif op == self.REVIEW_DUE_BILLING:
            pix_functional_tests.test_pix_review_due_billing()
        elif op == self.RETRIEVE_DUE_BILLING:
            pix_functional_tests.test_pix_retrieve_due_billing()
        elif op == self.RETRIEVE_DUE_BILLINGS:
            pix_functional_tests.test_pix_retrieve_due_billing_collection()
        elif op == self.RETRIEVE_DUE_BILLINGS_PAGINATION:
            pix_functional_tests.test_pix_retrieve_due_billing_collection_page()
        elif op == self.CREATE_LOCATION:
            pix_functional_tests.test_pix_include_location()
        elif op == self.RETRIEVE_REGISTERED_LOCATIONS:
            pix_functional_tests.test_pix_retrieve_location_list()
        elif op == self.RETRIEVE_REGISTERED_LOCATIONS_PAGINATION:
            pix_functional_tests.test_pix_retrieve_location_list_page()
        elif op == self.RETRIEVE_LOCATION:
            pix_functional_tests.test_pix_retrieve_location()
        elif op == self.UNLINK_LOCATION:
            pix_functional_tests.test_pix_unlink_location()
        elif op == self.RETRIEVE_PIX:
            pix_functional_tests.test_pix_retrieve_pix()
        elif op == self.RETRIEVE_RECEIVED_PIX:
            pix_functional_tests.test_pix_retrieve_pix_list()
        elif op == self.RETRIEVE_RECEIVED_PIX_PAGINATION:
            pix_functional_tests.test_pix_retrieve_pix_list_page()
        elif op == self.REQUEST_PIX_DEVOLUTION:
            pix_functional_tests.test_pix_request_devolution()
        elif op == self.RETRIEVE_PIX_DEVOLUTION:
            pix_functional_tests.test_pix_retrieve_devolution()
        elif op == self.RETRIEVE_DUE_BILLING_BATCH:
            pix_functional_tests.test_pix_retrieve_due_billing_batch()
        elif op == self.RETRIEVE_DUE_BILLING_BATCH_PAGINATION:
            pix_functional_tests.test_pix_retrieve_due_billing_batch_collection_page()
        elif op == self.RETRIEVE_DUE_BILLING_BATCHES:
            pix_functional_tests.test_pix_retrieve_due_billing_batch_collection()
        elif op == self.RETRIEVE_DUE_BILLING_BATCH_SUMMARY:
            pix_functional_tests.test_pix_retrieve_due_billing_batch_summary()
        elif op == self.RETRIEVE_DUE_BILLING_BATCH_SITUATION:
            pix_functional_tests.test_pix_retrieve_due_billing_batch_by_situation()
        elif op == self.CREATE_DUE_BILLING_BATCH:
            pix_functional_tests.test_pix_include_due_billing_batch()
        elif op == self.REVIEW_DUE_BILLING_BATCH:
            pix_functional_tests.test_pix_review_due_billing_batch()
        elif op == self.CREATE_WEBHOOK:
            pix_functional_tests.test_billing_include_webhook()
        elif op == self.GET_WEBHOOK:
            pix_functional_tests.test_billing_retrieve_webhook()
        elif op == self.DELETE_WEBHOOK:
            pix_functional_tests.test_billing_delete_webhook()
        elif op == self.RETRIEVE_CALLBACKS:
            pix_functional_tests.test_billing_retrieve_callbacks()
        elif op == self.RETRIEVE_CALLBACKS_PAGINATION:
            pix_functional_tests.test_billing_retrieve_callbacks_page()
        print()