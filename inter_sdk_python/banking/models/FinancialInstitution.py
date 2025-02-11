from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class FinancialInstitution:
    """
    The FinancialInstitution class represents a financial institution with its code,
    name, ISPB, and type.
    """

    code: Optional[str] = None
    """The unique code assigned to the financial institution."""

    name: Optional[str] = None
    """The name of the financial institution."""

    ispb: Optional[str] = None
    """The ISPB (Identificador de Sistema de Pagamentos Brasileiro) associated with the institution."""

    type: Optional[str] = None
    """The type of the financial institution."""

    @staticmethod
    def from_dict(data: Dict) -> 'FinancialInstitution':
        """
        Create a FinancialInstitution instance from a dictionary.

        Args:
            data (dict): A dictionary containing financial institution data.

        Returns:
            FinancialInstitution: An instance of FinancialInstitution.
        """
        return FinancialInstitution(
            code=data.get("code"),
            name=data.get("name"),
            ispb=data.get("ispb"),
            type=data.get("type")
        )

    def to_dict(self) -> dict:
        """
        Convert the FinancialInstitution instance to a dictionary.

        Returns:
            dict: A dictionary representation of the FinancialInstitution instance.
        """
        return {
            "code": self.code,
            "name": self.name,
            "ispb": self.ispb,
            "type": self.type
        }