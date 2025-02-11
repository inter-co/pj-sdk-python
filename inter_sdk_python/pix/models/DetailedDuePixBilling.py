from dataclasses import dataclass, field
from typing import Optional, List

from inter_sdk_python.pix.enums.BillingStatus import BillingStatus
from inter_sdk_python.pix.models.DueBilling import DueBilling
from inter_sdk_python.pix.models.Pix import Pix
from inter_sdk_python.pix.models.Receiver import Receiver


@dataclass
class DetailedDuePixBilling(DueBilling):
    """
    The DetailedDuePixBilling class extends the DueBilling
    class and provides detailed information about a billing transaction
    that is due.

    It includes fields for the PIX (copy and paste)
    information, receiver details, billing status, revision number,
    and a list of PIX transactions associated with the billing.
    """

    pix_copy_and_paste: Optional[str] = None
    """The PIX copy and paste information."""

    receiver: Optional[Receiver] = None
    """The details of the receiver for the billing transaction."""

    status: Optional[BillingStatus] = None
    """The current status of the billing transaction."""

    revision: Optional[int] = None
    """The revision number for the billing transaction."""

    pix_transactions: List[Pix] = field(default_factory=list)
    """A list of PIX transactions associated with the billing."""

    @staticmethod
    def from_dict(data: dict) -> 'DetailedDuePixBilling':
        """
        Create a DetailedDuePixBilling instance from a dictionary.

        Args:
            data (dict): A dictionary containing the DetailedDuePixBilling data.

        Returns:
            DetailedDuePixBilling: An instance of DetailedDuePixBilling.
        """
        due_billing = DueBilling.from_dict(data)
        return DetailedDuePixBilling(
            **due_billing.__dict__,
            pix_copy_and_paste=data.get("pixCopiaECola"),
            receiver=Receiver.from_dict(data["recebedor"]) if data.get("recebedor") else None,
            status=BillingStatus(data["status"]) if data.get("status") else None,
            revision=data.get("revisao"),
            pix_transactions=[Pix.from_dict(pix) for pix in data.get("pix", [])]
        )

    def to_dict(self) -> dict:
        """
        Convert the DetailedDuePixBilling instance to a dictionary.

        Returns:
            dict: A dictionary representation of the DetailedDuePixBilling instance.
        """
        due_billing_dict = super().to_dict()
        due_billing_dict.update({
            "pixCopiaECola": self.pix_copy_and_paste,
            "recebedor": self.receiver.to_dict() if self.receiver else None,
            "status": self.status.value if self.status else None,
            "revisao": self.revision,
            "pix": [pix.to_dict() for pix in self.pix_transactions]
        })
        return due_billing_dict