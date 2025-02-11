from dataclasses import dataclass
from typing import Optional, Dict

from inter_sdk_python.banking.enums.DarfPaymentDateType import DarfPaymentDateType


@dataclass
class DarfPaymentSearchFilter:
    """
    The DarfPaymentSearchFilter class represents the search filter for DARF payments,
    including request code, revenue code, and date filtering options.
    """

    request_code: Optional[str] = None
    """The request code for the payment search."""

    revenue_code: Optional[str] = None
    """The revenue code related to the payment search."""

    filter_date_by: Optional[str] = None
    """The criteria for filtering by date, represented as a DarfPaymentDateType enum."""

    @staticmethod
    def from_dict(data: Dict) -> 'DarfPaymentSearchFilter':
        """
        Create a DarfPaymentSearchFilter instance from a dictionary.

        Args:
            data (dict): A dictionary containing the DARF payment search filter data.

        Returns:
            DarfPaymentSearchFilter: An instance of DarfPaymentSearchFilter.
        """
        return DarfPaymentSearchFilter(
            request_code=data.get("codigoSolicitacao"),
            revenue_code=data.get("codigoReceita"),
            filter_date_by=DarfPaymentDateType(data["filtrarDataPor"]) if data.get("filtrarDataPor") is not None else None
        )

    def to_dict(self) -> dict:
        """
        Convert the DarfPaymentSearchFilter instance to a dictionary.

        Returns:
            dict: A dictionary representation of the DarfPaymentSearchFilter instance.
        """
        return {
            "codigoSolicitacao": self.request_code,
            "codigoReceita": self.revenue_code,
            "filtrarDataPor": self.filter_date_by if self.filter_date_by else None
        }