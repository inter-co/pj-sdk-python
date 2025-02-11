from functional_tests.menus.BankingMenu import BankingMenu
from functional_tests.menus.BillingMenu import BillingMenu
from functional_tests.menus.PixMenu import PixMenu
from functional_tests.utils.FuncTestUtils import FuncTestUtils
from inter_sdk_python.InterSdk import InterSdk
from inter_sdk_python.commons.exceptions.InvalidEnvironmentException import InvalidEnvironmentException

def main() -> None:
    """
    Main function to execute the menu-based interaction for the SDK.

    Raises:
        SdkException: If an error occurs during SDK operations.
    """
    environment = FuncTestUtils.get_string("Environment (PRODUCTION, SANDBOX)")
    
    validate_environment(environment)
    inter_sdk = get_inter_sdk_data(environment)

    while (op := menu(environment)) != 0:
        try:
            if op == 1:
                billing_menu = BillingMenu()
                while (op := billing_menu.show_menu(environment)) != 0:
                    billing_menu.execute(op, inter_sdk)
            elif op == 2:
                banking_menu = BankingMenu()
                while (op := banking_menu.show_menu(environment)) != 0:
                    banking_menu.execute(op, inter_sdk)
            elif op == 3:
                pix_menu = PixMenu()
                while (op := pix_menu.show_menu(environment)) != 0:
                    pix_menu.execute(op, inter_sdk)
        except Exception as e:
            print("An error occurred:")
            error = getattr(e, 'error', None)

            title_detail = None
            message_detail = None
            violations = None

            if error is not None:
                if hasattr(error, 'title'):
                    title_detail = error.title if error.title else "Error processing the request"
                if hasattr(error, 'detail'):
                    message_detail = error.detail if error.detail else "An error occurred during the request processing"
                if hasattr(error, 'violations'):
                    violations = error.violations

            print(title_detail)
            print(message_detail)
            print(violations)

def validate_environment(environment: str) -> None:
    """
    Validates the given environment string.

    Args:
        environment (str): The environment to validate.

    Raises:
        InvalidEnvironmentException: If the environment is not valid.
    """
    environments = ["PRODUCTION", "SANDBOX", "UAT"]

    if environment.upper() not in environments:
        raise InvalidEnvironmentException()

def get_inter_sdk_data(environment: str) -> InterSdk:
    """
    Retrieves InterSdk data based on the provided environment.

    Args:
        environment (str): The environment for the integration.

    Returns:
        InterSdk: An instance of InterSdk configured with provided credentials.
    
    Raises:
        SdkException: If an error occurs during SDK operation.
    """
    client_id = FuncTestUtils.get_string("Integration clientId")
    client_secret = FuncTestUtils.get_string("Integration clientSecret")
    certificate = FuncTestUtils.get_string("Path of the file with the pfx certificate (ex: src/main/java/inter/certificates/production.pfx)")
    password = FuncTestUtils.get_string("Password of the file with the pfx certificate")
    account = FuncTestUtils.get_string("Account")

    inter_sdk = InterSdk(environment, client_id, client_secret, certificate, password)
    inter_sdk.set_account(account)

    inter_sdk.set_rate_limit_control(True)
    return inter_sdk

def menu(environment: str) -> int:
    """
    Displays the main menu for the API options and returns the user's choice.

    Args:
        environment (str): The current environment (e.g. PRODUCTION, SANDBOX).

    Returns:
        int: The option selected by the user.
    """
    print("ENVIRONMENT", environment)
    print("1 - API Billing")
    print("2 - API Banking")
    print("3 - API Pix")
    print("0 - Exit")
    choice = input("=> ")
    
    try:
        return int(choice)
    except ValueError:
        print("Invalid option")
        return menu(environment)

if __name__ == "__main__":
    main()