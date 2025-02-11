from dataclasses import dataclass
from typing import Optional

@dataclass
class AdditionalInfo:
    """
    The AdditionalInfo class represents extra information
    that can be associated with a transaction or entity.

    It includes fields for the name and value of the
    additional information, allowing enhanced details to be captured
    within the transaction context.
    """

    name: Optional[str] = None
    """The name of the additional information."""

    value: Optional[str] = None
    """The value of the additional information."""

    @staticmethod
    def from_dict(data: dict) -> 'AdditionalInfo':
        """
        Create an AdditionalInfo instance from a dictionary.

        Args:
            data (dict): A dictionary containing the additional information data.

        Returns:
            AdditionalInfo: An instance of AdditionalInfo.
        """
        return AdditionalInfo(
            name=data.get("nome"),
            value=data.get("valor")
        )

    def to_dict(self) -> dict:
        """
        Convert the AdditionalInfo instance to a dictionary.

        Returns:
            dict: A dictionary representation of the AdditionalInfo instance.
        """
        return {
            "nome": self.name,
            "valor": self.value
        }