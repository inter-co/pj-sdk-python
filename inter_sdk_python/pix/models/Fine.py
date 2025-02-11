from dataclasses import dataclass
from typing import Optional

@dataclass
class Fine:
    """
    The Fine class represents the details of a penalty or
    fine imposed on a transaction. It includes fields for the modality
    of the fine (indicating the type or category) and the value or percentage
    to be applied.
    """

    modality: Optional[int] = None
    """The modality of the fine."""

    value_percentage: Optional[str] = None
    """The value or percentage associated with the fine."""

    @staticmethod
    def from_dict(data: dict) -> 'Fine':
        """
        Create a Fine instance from a dictionary.

        Args:
            data (dict): A dictionary containing the Fine data.

        Returns:
            Fine: An instance of Fine.
        """
        return Fine(
            modality=data.get("modalidade"),
            value_percentage=data.get("valorPerc")
        )

    def to_dict(self) -> dict:
        """
        Convert the Fine instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Fine instance.
        """
        return {
            "modalidade": self.modality,
            "valorPerc": self.value_percentage
        }