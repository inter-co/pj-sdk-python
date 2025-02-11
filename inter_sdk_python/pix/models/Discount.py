from dataclasses import dataclass, field
from typing import Optional, List

from inter_sdk_python.pix.models.FixedDateDiscount import FixedDateDiscount


@dataclass
class Discount:
    """
    The Discount class represents the details of a discount
    applicable to a transaction.

    It includes fields for the modality of the discount,
    the percentage value, and a list of fixed date discounts that
    may apply.
    """

    modality: Optional[int] = None
    """The modality of the discount."""

    value_percentage: Optional[str] = None
    """The percentage value of the discount."""

    fixed_date_discounts: List[FixedDateDiscount] = field(default_factory=list)
    """A list of fixed date discounts that may apply."""

    @staticmethod
    def from_dict(data: dict) -> 'Discount':
        """
        Create a Discount instance from a dictionary.

        Args:
            data (dict): A dictionary containing the Discount data.

        Returns:
            Discount: An instance of Discount.
        """
        return Discount(
            modality=data.get("modalidade"),
            value_percentage=data.get("valorPerc"),
            fixed_date_discounts=[FixedDateDiscount.from_dict(discount) for discount in data.get("descontoDataFixa", [])]
        )

    def to_dict(self) -> dict:
        """
        Convert the Discount instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Discount instance.
        """
        return {
            "modalidade": self.modality,
            "valorPerc": self.value_percentage,
            "descontoDataFixa": [discount.to_dict() for discount in self.fixed_date_discounts]
        }