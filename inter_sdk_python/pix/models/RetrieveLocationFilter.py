from dataclasses import dataclass
from typing import Optional

from inter_sdk_python.pix.enums.ImmediateBillingType import ImmediateBillingType


@dataclass
class RetrieveLocationFilter:
    """
    The RetrieveLocationFilter class is used to filter location
    requests based on certain criteria, including the presence of
    transaction ID and the type of immediate billing.
    """

    tx_id_present: Optional[bool] = None
    """Indicates whether a transaction ID is present."""

    billing_type: Optional[ImmediateBillingType] = None
    """The type of immediate billing for filtering location requests."""

    @staticmethod
    def from_dict(data: dict) -> 'RetrieveLocationFilter':
        """
        Create a RetrieveLocationFilter instance from a dictionary.

        Args:
            data (dict): A dictionary containing the RetrieveLocationFilter data.

        Returns:
            RetrieveLocationFilter: An instance of RetrieveLocationFilter.
        """
        return RetrieveLocationFilter(
            tx_id_present=data.get("txIdPresente"),
            billing_type=ImmediateBillingType(data["tipoCob"]) if data.get("tipoCob") else None
        )

    def to_dict(self) -> dict:
        """
        Convert the RetrieveLocationFilter instance to a dictionary.

        Returns:
            dict: A dictionary representation of the RetrieveLocationFilter instance.
        """
        return {
            "txIdPresente": self.tx_id_present,
            "tipoCob": self.billing_type.value if self.billing_type else None
        }