from dataclasses import dataclass
from typing import Optional

@dataclass
class Receiver:
    """
    The Receiver class represents the details of a recipient
    involved in a transaction. It includes fields for the receiver's
    name, CNPJ (Cadastro Nacional da Pessoa Jurídica), trade name,
    city, state (UF), postal code (CEP), and address (logradouro).
    """

    name: Optional[str] = None
    """The name of the receiver."""

    cnpj: Optional[str] = None
    """The CNPJ (Cadastro Nacional da Pessoa Jurídica) of the receiver."""

    trade_name: Optional[str] = None
    """The trade name of the receiver."""

    city: Optional[str] = None
    """The city where the receiver is located."""

    state: Optional[str] = None
    """The state (UF) where the receiver is located."""

    postal_code: Optional[str] = None
    """The postal code (CEP) of the receiver's address."""

    address: Optional[str] = None
    """The street address (logradouro) of the receiver."""

    @staticmethod
    def from_dict(data: dict) -> 'Receiver':
        """
        Create a Receiver instance from a dictionary.

        Args:
            data (dict): A dictionary containing the Receiver data.

        Returns:
            Receiver: An instance of Receiver.
        """
        return Receiver(
            name=data.get("nome"),
            cnpj=data.get("cnpj"),
            trade_name=data.get("nomeFantasia"),
            city=data.get("cidade"),
            state=data.get("uf"),
            postal_code=data.get("cep"),
            address=data.get("logradouro")
        )

    def to_dict(self) -> dict:
        """
        Convert the Receiver instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Receiver instance.
        """
        return {
            "nome": self.name,
            "cnpj": self.cnpj,
            "nomeFantasia": self.trade_name,
            "cidade": self.city,
            "uf": self.state,
            "cep": self.postal_code,
            "logradouro": self.address
        }