from dataclasses import dataclass
from typing import Optional

@dataclass
class Debtor:
    """
    The Debtor class represents information about a debtor in
    a billing system.

    It includes fields such as CPF (Brazilian individual
    taxpayer identification number), CNPJ (Brazilian corporate taxpayer
    identification number), name, email, city, state (UF), postal code (CEP),
    and address (logradouro).
    """

    cpf: Optional[str] = None
    """The CPF of the debtor."""

    cnpj: Optional[str] = None
    """The CNPJ of the debtor."""

    name: Optional[str] = None
    """The name of the debtor."""

    email: Optional[str] = None
    """The email address of the debtor."""

    city: Optional[str] = None
    """The city where the debtor resides."""

    state: Optional[str] = None
    """The state (UF) where the debtor resides."""

    postal_code: Optional[str] = None
    """The postal code (CEP) of the debtor's address."""

    address: Optional[str] = None
    """The address of the debtor."""

    @staticmethod
    def from_dict(data: dict) -> 'Debtor':
        """
        Create a Debtor instance from a dictionary.

        Args:
            data (dict): A dictionary containing the Debtor data.

        Returns:
            Debtor: An instance of Debtor.
        """
        return Debtor(
            cpf=data.get("cpf"),
            cnpj=data.get("cnpj"),
            name=data.get("nome"),
            email=data.get("email"),
            city=data.get("cidade"),
            state=data.get("uf"),
            postal_code=data.get("cep"),
            address=data.get("logradouro")
        )

    def to_dict(self) -> dict:
        """
        Convert the Debtor instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Debtor instance.
        """
        return {
            "cpf": self.cpf,
            "cnpj": self.cnpj,
            "nome": self.name,
            "email": self.email,
            "cidade": self.city,
            "uf": self.state,
            "cep": self.postal_code,
            "logradouro": self.address
        }