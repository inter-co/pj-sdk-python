from dataclasses import dataclass
from typing import Optional

@dataclass
class Fees:
    """
    The Fees class represents the details of fees applied
    to a transaction. It includes fields for the modality of the fees
    (indicating the type or category) and the value or percentage
    associated with the fees.
    """

    modality: Optional[int] = None
    """The modality of the fees."""

    value_percentage: Optional[str] = None
    """The value or percentage associated with the fees."""

    @staticmethod
    def from_dict(data: dict) -> 'Fees':
        """
        Create a Fees instance from a dictionary.

        Args:
            data (dict): A dictionary containing the Fees data.

        Returns:
            Fees: An instance of Fees.
        """
        return Fees(
            modality=data.get("modalidade"),
            value_percentage=data.get("valorPerc")
        )

    def to_dict(self) -> dict:
        """
        Convert the Fees instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Fees instance.
        """
        return {
            "modalidade": self.modality,
            "valorPerc": self.value_percentage
        }