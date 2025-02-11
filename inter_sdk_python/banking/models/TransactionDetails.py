from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class TransactionDetails:
    """
    The TransactionDetails class represents the details of a financial
    transaction, including the type of detail.
    """

    detail_type: Optional[str] = None
    """The type of detail associated with the transaction."""

    @staticmethod
    def from_dict(data: Dict) -> 'TransactionDetails':
        """
        Create a TransactionDetails instance from a dictionary.

        Args:
            data (dict): A dictionary containing transaction detail data.

        Returns:
            TransactionDetails: An instance of TransactionDetails.
        """
        return TransactionDetails(
            detail_type=data.get("tipoDetalhe")
        )

    def to_dict(self) -> dict:
        """
        Convert the TransactionDetails instance to a dictionary.

        Returns:
            dict: A dictionary representation of the TransactionDetails instance.
        """
        return {
            "tipoDetalhe": self.detail_type
        }