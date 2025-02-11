from dataclasses import dataclass
from typing import Optional

@dataclass
class BillingRetrieveCallbacksFilter:
    """
    The BillingRetrieveCallbacksFilter class represents the filter criteria
    used for searching callbacks.

    It contains a field for the request code that can be utilized to
    uniquely identify and retrieve specific callback records. This structure is
    essential for facilitating searches in callback retrieval processes.
    """

    request_code: Optional[str] = None
    """The request code for identifying specific callback records."""

    @staticmethod
    def from_dict(data: dict) -> 'BillingRetrieveCallbacksFilter':
        """
        Create a BillingRetrieveCallbacksFilter instance from a dictionary.

        Args:
            data (dict): A dictionary containing the filter data.

        Returns:
            BillingRetrieveCallbacksFilter: An instance of BillingRetrieveCallbacksFilter.
        """
        return BillingRetrieveCallbacksFilter(
            request_code=data.get("codigoSolicitacao")
        )