from dataclasses import dataclass
from typing import Optional

from inter_sdk_python.billing.enums.PersonType import PersonType


@dataclass
class Person:
    """
    The Person class represents an individual's or company's information,
    including identification details, contact information, and address.

    It is used to map data from a JSON structure, enabling the
    deserialization of received information. This class encapsulates essential
    attributes necessary for identifying and contacting a person or entity.
    """

    cpf_cnpj: Optional[str] = None
    """The CPF or CNPJ number of the person or entity."""

    person_type: Optional[PersonType] = None
    """The type of person, either individual or company."""

    name: Optional[str] = None
    """The name of the person or company."""

    address: Optional[str] = None
    """The address of the person or company."""

    number: Optional[str] = None
    """The number of the address."""

    complement: Optional[str] = None
    """Additional complement information for the address."""

    neighborhood: Optional[str] = None
    """The neighborhood where the person or company is located."""

    city: Optional[str] = None
    """The city of residence of the person or company."""

    state: Optional[str] = None
    """The state where the person or company is located."""

    zip_code: Optional[str] = None
    """The postal code for the address."""

    email: Optional[str] = None
    """The email address of the person or company."""

    area_code: Optional[str] = None
    """The area code for the telephone number."""

    phone: Optional[str] = None
    """The telephone number of the person or company."""

    @staticmethod
    def from_dict(data: dict) -> 'Person':
        """
        Create a Person instance from a dictionary.

        Args:
            data (dict): A dictionary containing the person data.

        Returns:
            Person: An instance of Person.
        """
        return Person(
            cpf_cnpj=data.get("cpfCnpj"),
            person_type=PersonType(data["tipoPessoa"]) if data.get("tipoPessoa") else None,
            name=data.get("nome"),
            address=data.get("endereco"),
            number=data.get("numero"),
            complement=data.get("complemento"),
            neighborhood=data.get("bairro"),
            city=data.get("cidade"),
            state=data.get("uf"),
            zip_code=data.get("cep"),
            email=data.get("email"),
            area_code=data.get("ddd"),
            phone=data.get("telefone")
        )

    def to_dict(self) -> dict:
        """
        Convert the Person instance to a dictionary.

        Returns:
            dict: A dictionary containing the person data.
        """
        return {
            "cpfCnpj": self.cpf_cnpj,
            "tipoPessoa": self.person_type.value if self.person_type else None,
            "nome": self.name,
            "endereco": self.address,
            "numero": self.number,
            "complemento": self.complement,
            "bairro": self.neighborhood,
            "cidade": self.city,
            "uf": self.state,
            "cep": self.zip_code,
            "email": self.email,
            "ddd": self.area_code,
            "telefone": self.phone
        }
