from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class SummaryItem:
    """
    The SummaryItem class represents a summary item in a billing context.

    It includes fields to capture the status of the item, the
    quantity of items, and the monetary value associated with it.
    This structure is useful for summarizing detailed billing information.
    """

    situation: Optional[str] = None
    """The status of the summary item."""

    quantity: Optional[int] = None
    """The quantity of items in the summary."""

    value: Optional[Decimal] = None
    """The monetary value associated with the summary item."""

    @staticmethod
    def from_dict(data: dict) -> 'SummaryItem':
        """
        Create a SummaryItem instance from a dictionary.

        Args:
            data (dict): A dictionary containing the summary item data.

        Returns:
            SummaryItem: An instance of SummaryItem.
        """
        return SummaryItem(
            situation=data.get("situacao"),
            quantity=data.get("quantidade"),
            value=Decimal(data["valor"]) if data.get("valor") is not None else None
        )

    def to_dict(self) -> dict:
        """
        Convert the SummaryItem instance to a dictionary.

        Returns:
            dict: A dictionary containing the summary item data.
        """
        return {
            "situacao": self.situation,
            "quantidade": self.quantity,
            "valor": float(self.value) if self.value is not None else None
        }