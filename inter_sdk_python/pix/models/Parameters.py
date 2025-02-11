from dataclasses import dataclass
from typing import Optional

from inter_sdk_python.pix.models.Pagination import Pagination


@dataclass
class Parameters:
    """
    The Parameters class represents a collection of parameters
    including pagination details. It supports additional custom fields
    via a map of additional attributes.
    """

    begin: Optional[str] = None
    """The start date for the parameters."""

    end: Optional[str] = None
    """The end date for the parameters."""

    cpf: Optional[str] = None
    """The CPF (Cadastro de Pessoa Física) for filtering."""

    cnpj: Optional[str] = None
    """The CNPJ (Cadastro Nacional da Pessoa Jurídica) for filtering."""

    location_present: Optional[bool] = None
    """Indicates whether the location is present in the parameters."""

    status: Optional[str] = None
    """The status for filtering the parameters."""

    pagination: Optional[Pagination] = None
    """Pagination details associated with the parameters."""

    cob_type: Optional[str] = None
    """The type of billing associated with the parameters."""

    @staticmethod
    def from_dict(data: dict) -> 'Parameters':
        """
        Create a Parameters instance from a dictionary.

        Args:
            data (dict): A dictionary containing the Parameters data.

        Returns:
            Parameters: An instance of Parameters.
        """
        return Parameters(
            begin=data.get("inicio"),
            end=data.get("fim"),
            cpf=data.get("cpf"),
            cnpj=data.get("cnpj"),
            location_present=data.get("locationPresente"),
            status=data.get("status"),
            pagination=Pagination.from_dict(data["paginacao"]) if data.get("paginacao") else None,
            cob_type=data.get("tipoCob")
        )

    def to_dict(self) -> dict:
        """
        Convert the Parameters instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Parameters instance.
        """
        return {
            "inicio": self.begin,
            "fim": self.end,
            "cpf": self.cpf,
            "cnpj": self.cnpj,
            "locationPresente": self.location_present,
            "status": self.status,
            "paginacao": self.pagination.to_dict() if self.pagination else None,
            "tipoCob": self.cob_type
        }