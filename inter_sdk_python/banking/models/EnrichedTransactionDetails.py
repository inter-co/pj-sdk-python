from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class EnrichedTransactionDetails:
    """
    The EnrichedTransactionDetails class represents additional details related to a transaction,
    including the type of detail provided.
    """

    detail_type: Optional[str] = None
    """The type of detail associated with the transaction."""

    @staticmethod
    def from_dict(data: Dict) -> 'EnrichedTransactionDetails':
        """
        Create an EnrichedTransactionDetails instance from a dictionary.

        Args:
            data (dict): A dictionary containing the enriched transaction details data.

        Returns:
            EnrichedTransactionDetails: An instance of EnrichedTransactionDetails.
        """
        return EnrichedTransactionDetails(
            detail_type=data.get("tipoDetalhe")
        )

    def to_dict(self) -> dict:
        """
        Convert the EnrichedTransactionDetails instance to a dictionary.

        Returns:
            dict: A dictionary representation of the EnrichedTransactionDetails instance.
        """
        return {
            "tipoDetalhe": self.detail_type
        }