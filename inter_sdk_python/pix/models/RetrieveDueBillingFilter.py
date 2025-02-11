from dataclasses import dataclass
from typing import Optional

from inter_sdk_python.pix.enums.BillingStatus import BillingStatus


@dataclass
class RetrieveDueBillingFilter:
    """
    The RetrieveDueBillingFilter class is used to filter billing
    records based on various criteria. It includes fields for
    CPF, CNPJ, presence of location, and billing status.
    Additionally, it supports custom fields through a map for
    additional attributes.
    """

    cpf: Optional[str] = None
    """The CPF (Cadastro de Pessoas Físicas) number for filtering."""

    cnpj: Optional[str] = None
    """The CNPJ (Cadastro Nacional da Pessoa Jurídica) number for filtering."""

    location_present: Optional[bool] = None
    """Indicates whether a location is present."""

    status: Optional[BillingStatus] = None
    """The billing status for filtering records."""

    @staticmethod
    def from_dict(data: dict) -> 'RetrieveDueBillingFilter':
        """
        Create a RetrieveDueBillingFilter instance from a dictionary.

        Args:
            data (dict): A dictionary containing the RetrieveDueBillingFilter data.

        Returns:
            RetrieveDueBillingFilter: An instance of RetrieveDueBillingFilter.
        """
        return RetrieveDueBillingFilter(
            cpf=data.get("cpf"),
            cnpj=data.get("cnpj"),
            location_present=data.get("locationPresente"),
            status=BillingStatus(data["status"]) if data.get("status") else None
        )

    def to_dict(self) -> dict:
        """
        Convert the RetrieveDueBillingFilter instance to a dictionary.

        Returns:
            dict: A dictionary representation of the RetrieveDueBillingFilter instance.
        """
        return {
            "cpf": self.cpf,
            "cnpj": self.cnpj,
            "locationPresente": self.location_present,
            "status": self.status.value if self.status else None
        }