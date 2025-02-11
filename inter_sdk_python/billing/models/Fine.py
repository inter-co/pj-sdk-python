from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from inter_sdk_python.billing.enums.FineCode import FineCode


@dataclass
class Fine:
    """
    Represents a fine with a specific code, rate, and value.

    This class allows you to define a fine that can have a unique code,
    a specified rate, and a monetary value. It also supports
    additional fields, which can be used to store any extra information
    related to the fine in a flexible manner.

    All fields are serializable to and from JSON format. The class is designed
    to be flexible and can handle dynamic fields that are not strictly defined
    within the class.
    """

    code: Optional[FineCode] = None
    """The code of the fine."""

    rate: Optional[Decimal] = None
    """The rate of the fine."""

    value: Optional[Decimal] = None
    """The value of the fine."""

    @staticmethod
    def from_dict(data: dict) -> 'Fine':
        """
        Create a Fine instance from a dictionary.

        Args:
            data (dict): A dictionary containing the fine data.

        Returns:
            Fine: An instance of Fine.
        """
        return Fine(
            code=FineCode(data["codigo"]) if data.get("codigo") else None,
            rate=Decimal(data["taxa"]) if data.get("taxa") else None,
            value=Decimal(data["valor"]) if data.get("valor") else None
        )

    def to_dict(self) -> dict:
        """
        Convert the Fine instance to a dictionary.

        Returns:
            dict: A dictionary containing the fine data.
        """
        return {
            "codigo": self.code.name if self.code else None,
            "taxa": float(self.rate) if self.rate is not None else None,
            "valor": float(self.value) if self.value is not None else None
        }