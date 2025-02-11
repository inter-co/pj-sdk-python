from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class Receiver:
    """
    The Receiver class represents the recipient of a PIX transaction,
    including their bank details and identification.
    """

    agency_code: Optional[str] = None
    """The bank agency code of the receiver."""

    ispb_code: Optional[str] = None
    """The ISPB code of the receiving bank."""

    cpf_or_cnpj: Optional[str] = None
    """The CPF or CNPJ of the receiver."""

    name: Optional[str] = None
    """The name of the receiver."""

    account_number: Optional[str] = None
    """The account number of the receiver."""

    account_type: Optional[str] = None
    """The type of the receiver's account (e.g., corrente, poupança)."""

    @staticmethod
    def from_dict(data: Dict) -> 'Receiver':
        """
        Create a Receiver instance from a dictionary.

        Args:
            data (dict): A dictionary containing receiver data.

        Returns:
            Receiver: An instance of Receiver.
        """
        return Receiver(
            agency_code=data.get("codAgencia"),
            ispb_code=data.get("codIspb"),
            cpf_or_cnpj=data.get("cpfCnpj"),
            name=data.get("nome"),
            account_number=data.get("nroConta"),
            account_type=data.get("tipoConta")
        )

    def to_dict(self) -> dict:
        """
        Convert the Receiver instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Receiver instance.
        """
        return {
            "codAgencia": self.agency_code,
            "codIspb": self.ispb_code,
            "cpfCnpj": self.cpf_or_cnpj,
            "nome": self.name,
            "nroConta": self.account_number,
            "tipoConta": self.account_type
        }