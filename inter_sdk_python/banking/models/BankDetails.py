from dataclasses import dataclass
from typing import Optional, Dict

from inter_sdk_python.banking.enums.AccountType import AccountType
from inter_sdk_python.banking.models.FinancialInstitution import FinancialInstitution


@dataclass
class BankDetails:
    """
    The BankDetails class contains information about bank account details,
    including account type, agency, CPF/CNPJ, and associated financial institution.
    """

    _type_: str = "BANK_DETAILS"
    """The type of the bank details."""

    account: Optional[str] = None
    """The bank account number."""

    account_type: Optional[AccountType] = None
    """The type of bank account (savings, checking, etc.)."""

    cpf_cnpj: Optional[str] = None
    """The CPF or CNPJ associated with the account."""

    agency: Optional[str] = None
    """The bank agency number."""

    name: Optional[str] = None
    """The name of the account holder."""

    financial_institution: Optional[FinancialInstitution] = None
    """The financial institution associated with the account."""

    @staticmethod
    def from_dict(data: Dict) -> 'BankDetails':
        """
        Create a BankDetails instance from a dictionary.

        Args:
            data (dict): A dictionary containing the bank details data.

        Returns:
            BankDetails: An instance of BankDetails.
        """
        return BankDetails(
            account=data.get("contaCorrente"),
            account_type=AccountType[data["tipoConta"]] if "tipoConta" in data else None,
            cpf_cnpj=data.get("cpfCnpj"),
            agency=data.get("agencia"),
            name=data.get("nome"),
            financial_institution=FinancialInstitution.from_dict(data["instituicaoFinanceira"]) if "instituicaoFinanceira" in data else None
        )

    def to_dict(self) -> dict:
        """
        Convert the BankDetails instance to a dictionary.

        Returns:
            dict: A dictionary representation of the BankDetails instance.
        """
        return {
            "contaCorrente": self.account,
            "tipoConta": self.account_type.name if self.account_type else None,
            "cpfCnpj": self.cpf_cnpj,
            "agencia": self.agency,
            "nome": self.name,
            "instituicaoFinanceira": self.financial_institution.to_dict() if self.financial_institution else None
        }