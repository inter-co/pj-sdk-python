from dataclasses import dataclass
from typing import Optional, Dict

from inter_sdk_python.billing.enums.BillingDateType import BillingDateType
from inter_sdk_python.billing.enums.BillingSituation import BillingSituation
from inter_sdk_python.billing.enums.BillingType import BillingType


@dataclass
class BaseBillingRetrievalFilter:
    """
    The BaseBillingRetrievalFilter class represents the filter criteria 
    for retrieving billing information, including various parameters.
    """

    filter_date_by: Optional[BillingDateType] = None
    """The date type to filter by, represented as a BillingDateType enum."""

    situation: Optional[BillingSituation] = None
    """The status of the billing, represented as a BillingSituation enum."""

    payer: Optional[str] = None
    """The name of the payer."""

    payer_cpf_cnpj: Optional[str] = None
    """The CPF or CNPJ of the payer."""

    your_number: Optional[str] = None
    """A unique number associated with the billing."""

    billing_type: Optional[BillingType] = None
    """The type of billing, represented as a BillingType enum."""

    @staticmethod
    def from_dict(data: Dict) -> 'BaseBillingRetrievalFilter':
        """
        Create a BaseBillingRetrievalFilter instance from a dictionary.

        Args:
            data (dict): A dictionary containing billing retrieval filter data.

        Returns:
            BaseBillingRetrievalFilter: An instance of BaseBillingRetrievalFilter.
        """
        return BaseBillingRetrievalFilter(
            filter_date_by=BillingDateType(data["filtrarDataPor"]) if data.get("filtrarDataPor") else None,
            situation=BillingSituation(data["situacao"]) if data.get("situacao") else None,
            payer=data.get("pessoaPagadora"),
            payer_cpf_cnpj=data.get("cpfCnpjPessoaPagadora"),
            your_number=data.get("seuNumero"),
            billing_type=BillingType(data["tipoCobranca"]) if data.get("tipoCobranca") else None
        )

    def to_dict(self) -> dict:
        """
        Convert the BaseBillingRetrievalFilter instance to a dictionary.

        Returns:
            dict: A dictionary representation of the BaseBillingRetrievalFilter instance.
        """
        return {
            "filtrarDataPor": self.filter_date_by.value if self.filter_date_by else None,
            "situacao": self.situation.value if self.situation else None,
            "pessoaPagadora": self.payer,
            "cpfCnpjPessoaPagadora": self.payer_cpf_cnpj,
            "seuNumero": self.your_number,
            "tipoCobranca": self.billing_type.value if self.billing_type else None
        }