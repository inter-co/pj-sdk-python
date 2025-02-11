from dataclasses import dataclass
from typing import Optional

@dataclass
class CallbackRetrieveFilter:
    """
    The CallbackRetrieveFilter class is used to filter callback requests
    based on specific criteria, such as the transaction ID (txid).

    This class provides a structured way to specify filters
    when retrieving callback data, allowing for efficient searches based
    on transaction identifiers.
    """

    txid: Optional[str] = None
    """The transaction ID to filter callback requests."""

    @staticmethod
    def from_dict(data: dict) -> 'CallbackRetrieveFilter':
        """
        Create a CallbackRetrieveFilter instance from a dictionary.

        Args:
            data (dict): A dictionary containing the filter data.

        Returns:
            CallbackRetrieveFilter: An instance of CallbackRetrieveFilter.
        """
        return CallbackRetrieveFilter(
            txid=data.get("txid")
        )

    def to_dict(self) -> dict:
        """
        Convert the CallbackRetrieveFilter instance to a dictionary.

        Returns:
            dict: A dictionary representation of the CallbackRetrieveFilter instance.
        """
        return {
            "txid": self.txid
        }