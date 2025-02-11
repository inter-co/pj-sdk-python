import os
from datetime import datetime, timedelta
from typing import List

from inter_sdk_python.banking.BankingSdk import BankingSdk
from inter_sdk_python.billing.BillingSdk import BillingSdk
from inter_sdk_python.commons.enums.EnvironmentEnum import EnvironmentEnum
from inter_sdk_python.commons.exceptions.CertificateExpiredException import CertificateExpiredException
from inter_sdk_python.commons.exceptions.CertificateNotFoundException import CertificateNotFoundException
from inter_sdk_python.commons.models.Config import Config
from inter_sdk_python.commons.structures.Constants import Constants
from inter_sdk_python.commons.utils.SslUtils import SslUtils
from inter_sdk_python.pix.PixSdk import PixSdk


def format_error_message(exception):
    if hasattr(exception, 'error'):
        error_info = exception.error
        return f"{error_info.title}: {error_info.detail}. Consult: {error_info.timestamp}"
    return str(exception)


class InterSdk:
    VERSION = "inter-sdk-python v1.0.0"
    warnings = []
    def __init__(self, environment: str, client_id: str, client_secret: str, certificate: str, certificate_password: str):
        """
        SDK for accessing Inter's PJ APIs.

        Args:
            environment (str): Environment configuration.
            client_id (str): Application identifier.
            client_secret (str): Application secret.
            certificate (str): Certificate file, e.g., certs/inter.pfx.
            certificate_password (str): Certificate password.
        
        Raises:
            SdkException: If an error occurs during initialization.
        """
        self.config = Config(
            client_id=client_id,
            client_secret=client_secret,
            certificate=certificate,
            password=certificate_password,
            environment=EnvironmentEnum[environment],
            account=None
        )

        self.banking_sdk = None
        self.billing_sdk = None
        self.pix_sdk = None

        try:
            private_key, certificate = SslUtils.convert_pfx_to_pem(self.config.certificate, self.config.password)
            expire_soon, days_to_expire = SslUtils.is_certificate_expiring_soon(certificate, Constants.DAYS_TO_EXPIRE)
        except (CertificateExpiredException, CertificateNotFoundException) as e:
            message = format_error_message(e)
            raise RuntimeError(message) from e
        except Exception as e:
            raise e

        if expire_soon is True:
            self.warnings.append(f"Certificate nearing expiration. Less than {Constants.DAYS_TO_EXPIRE} days left. Expires on {days_to_expire}.")

        self.config.key, self.config.crt = SslUtils.get_cert_key_name(private_key, certificate)

        # Create logs directory if it doesn't exist
        if not os.path.exists("logs"):
            os.makedirs("logs")

        tomorrow = f"logs/inter-sdk-{(datetime.now() + timedelta(days=1)).strftime('%a')}.log"
        if os.path.exists(tomorrow):
            os.remove(tomorrow)

        print(self.VERSION)
        
        self.warnings: List[str] = []

    def banking(self) -> BankingSdk:
        """
        Sdk for API banking.

        Returns:
            BankingSdk: The banking SDK instance.
        """
        if self.banking_sdk is None:
            self.banking_sdk = BankingSdk(self.config)
        return self.banking_sdk

    def billing(self) -> BillingSdk:
        """
        Sdk for API billing.

        Returns:
            BillingSdk: The billing SDK instance.
        """
        if self.billing_sdk is None:
            self.billing_sdk = BillingSdk(self.config)
        return self.billing_sdk

    def pix(self) -> PixSdk:
        """
        Sdk for API pix.

        Returns:
            PixSdk: The pix SDK instance.
        """
        if self.pix_sdk is None:
            self.pix_sdk = PixSdk(self.config)
        return self.pix_sdk
    
    def warning_list(self) -> List[str]:
        """
        Returns the list of warnings from the last operation.

        Returns:
            List[str]: List of warnings, may be empty.
        """
        return self.warnings

    def set_debug(self, debug: bool) -> None:
        """
        Configures the debug mode. In debug mode, the request and response data will be logged.
        
        Args:
            debug (bool): Indicates if debug mode should be enabled.
        """
        self.config.debug = debug

    def set_rate_limit_control(self, control: bool) -> None:
        """
        Indicates whether it will perform automatic rate limit control.

        Args:
            control (bool): Indicates if the SDK will perform automatic control - default is True.
        """
        self.config.rate_limit_control = control

    def set_account(self, account: str) -> None:
        """
        Selects the current account. Necessary only if the application is configured with multiple accounts.

        Args:
            account (str): Current account number.
        """
        self.config.account = account

    def get_account(self) -> str:
        """
        Returns the selected checking account.

        Returns:
            str: Selected checking account.
        """
        return self.config.account
