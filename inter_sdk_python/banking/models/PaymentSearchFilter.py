from dataclasses import dataclass
from typing import Optional, Dict

from inter_sdk_python.banking.enums.PaymentDateType import PaymentDateType


@dataclass
class PaymentSearchFilter:
    """
    The PaymentSearchFilter class represents the filter criteria for searching payments,
    including barcode, transaction code, and date filtering type.
    """

    barcode: Optional[str] = None
    """The barcode or digitable line for the payment search."""

    transaction_code: Optional[str] = None
    """The unique transaction code for the payment."""

    filter_date_by: Optional[str] = None
    """The type of date to filter by, represented as a PaymentDateType enum."""

    @staticmethod
    def from_dict(data: Dict) -> 'PaymentSearchFilter':
        """
        Create a PaymentSearchFilter instance from a dictionary.

        Args:
            data (dict): A dictionary containing payment search filter data.

        Returns:
            PaymentSearchFilter: An instance of PaymentSearchFilter.
        """
        return PaymentSearchFilter(
            barcode=data.get("codBarraLinhaDigitavel"),
            transaction_code=data.get("codigoTransacao"),
            filter_date_by=PaymentDateType(data["filtrarDataPor"]) if data.get("filtrarDataPor") is not None else None
        )

    def to_dict(self) -> dict:
        """
        Convert the PaymentSearchFilter instance to a dictionary.

        Returns:
            dict: A dictionary representation of the PaymentSearchFilter instance.
        """
        return {
            "codBarraLinhaDigitavel": self.barcode,
            "codigoTransacao": self.transaction_code,
            "filtrarDataPor": self.filter_date_by if self.filter_date_by else None
        }