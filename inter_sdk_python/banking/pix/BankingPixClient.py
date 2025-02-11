import logging

from inter_sdk_python.banking.models.IncludePixResponse import IncludePixResponse
from inter_sdk_python.banking.models.Pix import Pix
from inter_sdk_python.banking.models.RetrievePixResponse import RetrievePixResponse
from inter_sdk_python.commons.models.Config import Config
from inter_sdk_python.commons.structures.Constants import Constants
from inter_sdk_python.commons.utils.HttpUtils import HttpUtils
from inter_sdk_python.commons.utils.UrlUtils import UrlUtils


class BankingPixClient:
    def include_pix(self, config: Config, pix: Pix) -> IncludePixResponse:
        """
        Includes a new PIX payment request in the banking system.

        Args:
            config (Config): The configuration object containing client information.
            pix (Pix): The Pix object containing details of the PIX payment to be included.

        Returns:
            IncludePixResponse: An object containing the response from the banking system 
                                after including the PIX payment request.

        Raises:
            SdkException: If there is an error during the inclusion process, such as
                           network issues or API response errors.
        """
        logging.info("IncludePix {} {}".format(config.client_id, pix.description))
        url = UrlUtils.build_url(config, Constants.URL_BANKING_PAYMENT_PIX)
        
        try:
            json_request =pix.to_json()
            json_response = HttpUtils.call_post(config, url, Constants.PIX_PAYMENT_WRITE_SCOPE, "Error including pix", json_request)
            return IncludePixResponse.from_dict(json_response)
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise

    def retrieve_pix(self, config: Config, request_code: str) -> RetrievePixResponse:
        """
        Retrieves the details of a PIX payment request based on the given request code.

        Args:
            config (Config): The configuration object containing client information.
            request_code (str): The unique code of the PIX payment request to retrieve.

        Returns:
            RetrievePixResponse: An object containing the details of the requested PIX payment.

        Raises:
            SdkException: If there is an error during the retrieval process, such as
                           network issues or API response errors.
        """
        logging.info("RetrievePix {} {}".format(config.client_id, request_code))
        url = f"{UrlUtils.build_url(config, Constants.URL_BANKING_PAYMENT_PIX)}/{request_code}"
        
        json_response = HttpUtils.call_get(config, url, Constants.PIX_PAYMENT_READ_SCOPE, "Error retrieving pix")
        
        try:
            return RetrievePixResponse.from_dict(json_response)
        except Exception as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise