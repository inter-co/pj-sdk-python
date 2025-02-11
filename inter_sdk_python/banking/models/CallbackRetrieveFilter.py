from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class CallbackRetrieveFilter:
    """
    The CallbackRetrieveFilter class represents a filter for retrieving callbacks,
    including transaction code and end-to-end ID.
    """

    transaction_code: Optional[str] = None
    """The transaction code used for filtering callbacks."""

    end_to_end_id: Optional[str] = None
    """The end-to-end identifier used for filtering callbacks."""

    @staticmethod
    def from_dict(data: Dict) -> 'CallbackRetrieveFilter':
        """
        Create a CallbackRetrieveFilter instance from a dictionary.

        Args:
            data (dict): A dictionary containing the filter data.

        Returns:
            CallbackRetrieveFilter: An instance of CallbackRetrieveFilter.
        """
        return CallbackRetrieveFilter(
            transaction_code=data.get("codigoTransacao"),
            end_to_end_id=data.get("endToEnd")
        )

    def to_dict(self) -> dict:
        """
        Convert the CallbackRetrieveFilter instance to a dictionary.

        Returns:
            dict: A dictionary representation of the CallbackRetrieveFilter instance.
        """
        return {
            "codigoTransacao": self.transaction_code,
            "endToEnd": self.end_to_end_id
        }