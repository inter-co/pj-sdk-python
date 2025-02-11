from dataclasses import dataclass
from typing import Optional

@dataclass
class RetrievedPixFilter:
    """
    The RetrievedPixFilter class is used to filter received
    PIX transactions based on various criteria. It includes fields
    for transaction ID (txId), presence of transaction ID, presence
    of return, and identification numbers such as CPF and CNPJ.
    """

    tx_id: Optional[str] = None
    """The transaction ID (txId) for filtering transactions."""

    tx_id_present: Optional[bool] = None
    """Indicates whether a transaction ID is present."""

    devolution_present: Optional[bool] = None
    """Indicates whether a devolution is present."""

    cpf: Optional[str] = None
    """The CPF of the person related to the transaction."""

    cnpj: Optional[str] = None
    """The CNPJ of the entity related to the transaction."""

    @staticmethod
    def from_dict(data: dict) -> 'RetrievedPixFilter':
        """
        Create a RetrievedPixFilter instance from a dictionary.

        Args:
            data (dict): A dictionary containing the RetrievedPixFilter data.

        Returns:
            RetrievedPixFilter: An instance of RetrievedPixFilter.
        """
        return RetrievedPixFilter(
            tx_id=data.get("txId"),
            tx_id_present=data.get("txIdPresente"),
            devolution_present=data.get("devolucaoPresente"),
            cpf=data.get("cpf"),
            cnpj=data.get("cnpj")
        )

    def to_dict(self) -> dict:
        """
        Convert the RetrievedPixFilter instance to a dictionary.

        Returns:
            dict: A dictionary representation of the RetrievedPixFilter instance.
        """
        return {
            "txId": self.tx_id,
            "txIdPresente": self.tx_id_present,
            "devolucaoPresente": self.devolution_present,
            "cpf": self.cpf,
            "cnpj": self.cnpj
        }