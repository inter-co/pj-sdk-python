from dataclasses import dataclass
from typing import Optional

@dataclass
class Reduction:
    """
    The Reduction class represents the details of a discount
    applicable to a transaction. It includes fields for the modality
    of the discount (indicating the type or category) and the value or
    percentage of the discount applied. This structure is important for
    managing financial discounts within a system.
    """

    modality: Optional[int] = None
    """The modality of the discount."""

    value_percentage: Optional[str] = None
    """The value or percentage of the discount."""

    @staticmethod
    def from_dict(data: dict) -> 'Reduction':
        """
        Create a Reduction instance from a dictionary.

        Args:
            data (dict): A dictionary containing the Reduction data.

        Returns:
            Reduction: An instance of Reduction.
        """
        return Reduction(
            modality=data.get("modalidade"),
            value_percentage=data.get("valorPerc")
        )

    def to_dict(self) -> dict:
        """
        Convert the Reduction instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Reduction instance.
        """
        return {
            "modalidade": self.modality,
            "valorPerc": self.value_percentage
        }