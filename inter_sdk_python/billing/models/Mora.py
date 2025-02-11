from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from inter_sdk_python.billing.enums.MoraCode import MoraCode


@dataclass
class Mora:
    """
    The Mora class represents the interest applied to an overdue
    payment.

    It includes details such as the interest code, the percentage rate
    of the interest, and the total amount of the interest. This class is used
    to map data from a JSON structure, allowing the deserialization of
    received information.
    """

    code: Optional[MoraCode] = None
    """The interest code that categorizes the type of interest."""

    rate: Optional[Decimal] = None
    """The percentage rate of the interest."""

    value: Optional[Decimal] = None
    """The total amount of the interest."""

    @staticmethod
    def from_dict(data: dict) -> 'Mora':
        """
        Create a Mora instance from a dictionary.

        Args:
            data (dict): A dictionary containing the mora (interest) data.

        Returns:
            Mora: An instance of Mora.
        """
        return Mora(
            code=MoraCode(data["codigo"]) if data.get("codigo") else None,
            rate=Decimal(data["taxa"]) if data.get("taxa") else None,
            value=Decimal(data["valor"]) if data.get("valor") else None
        )

    def to_dict(self) -> dict:
        """
        Convert the Mora instance to a dictionary.

        Returns:
            dict: A dictionary containing the interest data.
        """
        return {
            "codigo": self.code.name if self.code else None,
            "taxa": float(self.rate) if self.rate is not None else None,
            "valor": float(self.value) if self.value is not None else None
        }
