from dataclasses import dataclass
from typing import Optional

from inter_sdk_python.billing.models.BillingBilletRetrievingResponse import BillingBilletRetrievingResponse
from inter_sdk_python.billing.models.BillingPixRetrievingResponse import BillingPixRetrievingResponse
from inter_sdk_python.billing.models.BillingRetrievingResponse import BillingRetrievingResponse


@dataclass
class RetrievedBilling:
    """
    The RetrievedBilling class represents the response containing different
    formats of a retrieved billing.

    It includes references to the billing information, the associated
    billing slip (billet), and the Pix payment details. This class is used to
    consolidate data from multiple retrieval responses, allowing for easy access
    to all relevant billing formats in a single structure.
    """

    billing: Optional[BillingRetrievingResponse] = None
    """The detailed billing information."""

    slip: Optional[BillingBilletRetrievingResponse] = None
    """The billing slip associated with the payment."""

    pix: Optional[BillingPixRetrievingResponse] = None
    """The Pix payment details associated with the billing."""

    @staticmethod
    def from_dict(data: dict) -> 'RetrievedBilling':
        """
        Create a RetrievedBilling instance from a dictionary.

        Args:
            data (dict): A dictionary containing the retrieved billing data.

        Returns:
            RetrievedBilling: An instance of RetrievedBilling.
        """
        return RetrievedBilling(
            billing=BillingRetrievingResponse.from_dict(data["cobranca"]) if data.get("cobranca") else None,
            slip=BillingBilletRetrievingResponse.from_dict(data["boleto"]) if data.get("boleto") else None,
            pix=BillingPixRetrievingResponse.from_dict(data["pix"]) if data.get("pix") else None
        )

    def to_dict(self) -> dict:
        """
        Convert the RetrievedBilling instance to a dictionary.

        Returns:
            dict: A dictionary containing the retrieved billing data.
        """
        return {
            "cobranca": self.billing.to_dict() if self.billing else None,
            "boleto": self.slip.to_dict() if self.slip else None,
            "pix": self.pix.to_dict() if self.pix else None
        }