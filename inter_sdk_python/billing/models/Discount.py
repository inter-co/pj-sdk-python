from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from inter_sdk_python.banking.enums.DiscountCode import DiscountCode


@dataclass
class Discount:
    """
    The Discount class represents a discount applied to a specific
    transaction.

    It includes details such as the discount code, the number of days
    for which it is valid, the percentage rate of the discount, and the total
    amount of the discount.
    """

    code: Optional[DiscountCode] = None
    """The discount code that categorizes the type of discount."""

    number_of_days: Optional[int] = None
    """The number of days the discount is valid."""

    rate: Optional[Decimal] = None
    """The percentage rate of the discount."""

    value: Optional[Decimal] = None
    """The total amount of the discount."""

    @staticmethod
    def from_dict(data: dict) -> 'Discount':
        """
        Create a Discount instance from a dictionary.

        Args:
            data (dict): A dictionary containing the discount data.

        Returns:
            Discount: An instance of Discount.
        """
        return Discount(
            code=DiscountCode(data["codigo"]) if data.get("codigo") else None,
            number_of_days=data.get("quantidadeDias"),
            rate=Decimal(data["taxa"]) if data.get("taxa") else None,
            value=Decimal(data["valor"]) if data.get("valor") else None
        )

    def to_dict(self) -> dict:
        """
        Convert the Discount instance to a dictionary.

        Returns:
            dict: A dictionary containing the discount data.
        """
        return {
            "codigo": self.code.value if self.code else None,
            "quantidadeDias": self.number_of_days,
            "taxa": float(self.rate) if self.rate is not None else None,
            "valor": float(self.value) if self.value is not None else None
        }