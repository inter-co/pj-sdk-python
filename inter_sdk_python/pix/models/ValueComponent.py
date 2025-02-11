from dataclasses import dataclass
from typing import Optional

from inter_sdk_python.pix.models.ComponentValue import ComponentValue


@dataclass
class ValueComponent:
    """
    The ValueComponent class represents various monetary
    components related to a financial transaction, including the
    original amount, change (troco), discounts, and additional
    charges such as interest (juros) and penalties (multa).
    """

    original: Optional[ComponentValue] = None
    """The original amount of the financial transaction."""

    change: Optional[ComponentValue] = None
    """The change (troco) amount to be returned after the transaction."""

    discount_amount: Optional[ComponentValue] = None
    """The discount amount (abatimento) applied to the transaction."""

    direct_discount: Optional[ComponentValue] = None
    """The direct discount applied to the transaction."""

    interest: Optional[ComponentValue] = None
    """The interest (juros) charged on the transaction."""

    penalty: Optional[ComponentValue] = None
    """The penalty (multa) charged on the transaction."""

    @staticmethod
    def from_dict(data: dict) -> 'ValueComponent':
        """
        Create a ValueComponent instance from a dictionary.

        Args:
            data (dict): A dictionary containing the ValueComponent data.

        Returns:
            ValueComponent: An instance of ValueComponent.
        """
        return ValueComponent(
            original=ComponentValue.from_dict(data["original"]) if data.get("original") else None,
            change=ComponentValue.from_dict(data["troco"]) if data.get("troco") else None,
            discount_amount=ComponentValue.from_dict(data["abatimento"]) if data.get("abatimento") else None,
            direct_discount=ComponentValue.from_dict(data["desconto"]) if data.get("desconto") else None,
            interest=ComponentValue.from_dict(data["juros"]) if data.get("juros") else None,
            penalty=ComponentValue.from_dict(data["multa"]) if data.get("multa") else None
        )

    def to_dict(self) -> dict:
        """
        Convert the ValueComponent instance to a dictionary.

        Returns:
            dict: A dictionary representation of the ValueComponent instance.
        """
        return {
            "original": self.original.to_dict() if self.original else None,
            "troco": self.change.to_dict() if self.change else None,
            "abatimento": self.discount_amount.to_dict() if self.discount_amount else None,
            "desconto": self.direct_discount.to_dict() if self.direct_discount else None,
            "juros": self.interest.to_dict() if self.interest else None,
            "multa": self.penalty.to_dict() if self.penalty else None
        }