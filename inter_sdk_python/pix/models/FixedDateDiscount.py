from dataclasses import dataclass
from typing import Optional

@dataclass
class FixedDateDiscount:
    """
    The FixedDateDiscount class represents a discount
    that applies to a specific date. It includes fields for
    the percentage value of the discount and the associated date.
    This structure is useful for managing fixed-date discounts
    within a financial or sales system.
    """

    value_percentage: Optional[str] = None
    """The percentage value of the discount."""

    date: Optional[str] = None
    """The associated date for the discount."""

    @staticmethod
    def from_dict(data: dict) -> 'FixedDateDiscount':
        """
        Create a FixedDateDiscount instance from a dictionary.

        Args:
            data (dict): A dictionary containing the FixedDateDiscount data.

        Returns:
            FixedDateDiscount: An instance of FixedDateDiscount.
        """
        return FixedDateDiscount(
            value_percentage=data.get("valorPerc"),
            date=data.get("data")
        )

    def to_dict(self) -> dict:
        """
        Convert the FixedDateDiscount instance to a dictionary.

        Returns:
            dict: A dictionary representation of the FixedDateDiscount instance.
        """
        return {
            "valorPerc": self.value_percentage,
            "data": self.date
        }