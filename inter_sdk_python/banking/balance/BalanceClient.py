import json
import logging

from inter_sdk_python.commons.models.Config import Config
from inter_sdk_python.commons.structures.Constants import Constants
from inter_sdk_python.commons.utils.HttpUtils import HttpUtils
from inter_sdk_python.commons.utils.UrlUtils import UrlUtils
from ..models.Balance import Balance

class BalanceClient:

    def retrieve_balance(self, config: Config, balance_date: str) -> Balance:
        """
        Retrieves the bank balance for the specified date.

        Args:
            config (Config): The configuration object containing necessary parameters, such as client ID.
            balance_date (str): The date for which the balance will be retrieved in the appropriate format.

        Returns:
            Balance: A Balance object containing the balance information.

        Raises:
            SdkException: If an error occurs during the balance retrieval or if the response format is incorrect.
        """
        logging.info("BalanceRetrieval banking... config.clientId = %s, balanceDate = %s",
                 config.client_id if config else None, balance_date)
        logging.debug("config: %s", config)

        url = UrlUtils.build_url(config, Constants.URL_BANKING_BALANCE)
        if balance_date:
            url += f"?dataSaldo={balance_date}"

        json_response = HttpUtils.call_get(config, url, Constants.READ_BALANCE_SCOPE, "Error retrieving balance")

        try:
            return Balance.from_dict(json_response)
        except json.JSONDecodeError as io_exception:
            logging.error(Constants.GENERIC_EXCEPTION_MESSAGE, exc_info=io_exception)
            raise