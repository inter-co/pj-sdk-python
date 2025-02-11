from dataclasses import dataclass, field
from typing import Optional, List

from inter_sdk_python.pix.models.AdditionalInfo import AdditionalInfo
from inter_sdk_python.pix.models.Debtor import Debtor
from inter_sdk_python.pix.models.DueBillingCalendar import DueBillingCalendar
from inter_sdk_python.pix.models.DueBillingValue import DueBillingValue
from inter_sdk_python.pix.models.Location import Location
from inter_sdk_python.pix.models.Receiver import Receiver


@dataclass
class GeneratedDueBilling:
    """
    The GeneratedDueBilling class represents a generated
    due billing transaction.

    It includes various fields that describe the billing
    details, such as keys, payer requests, debtor and receiver
    information, billing values, and additional dynamic fields.
    """

    key: Optional[str] = None
    """The unique key associated with the billing transaction."""

    payer_request: Optional[str] = None
    """The request made by the payer for this billing transaction."""

    additional_info: List[AdditionalInfo] = field(default_factory=list)
    """Additional information related to the billing transaction."""

    pix_copy_paste: Optional[str] = None
    """The copy-paste format of the PIX transaction."""

    debtor: Optional[Debtor] = None
    """Information about the debtor of the billing."""

    receiver: Optional[Receiver] = None
    """Information about the receiver of the billing."""

    location: Optional[Location] = None
    """Location details associated with the billing."""

    status: Optional[str] = None
    """The current status of the billing transaction."""

    value: Optional[DueBillingValue] = None
    """The value associated with the billing transaction."""

    calendar: Optional[DueBillingCalendar] = None
    """The billing calendar details related to the transaction."""

    txid: Optional[str] = None
    """The transaction ID associated with the billing."""

    revision: Optional[int] = None
    """The revision number of the billing transaction."""

    @staticmethod
    def from_dict(data: dict) -> 'GeneratedDueBilling':
        """
        Create a GeneratedDueBilling instance from a dictionary.

        Args:
            data (dict): A dictionary containing the GeneratedDueBilling data.

        Returns:
            GeneratedDueBilling: An instance of GeneratedDueBilling.
        """
        return GeneratedDueBilling(
            key=data.get("chave"),
            payer_request=data.get("solicitacaoPagador"),
            additional_info=[AdditionalInfo.from_dict(info) for info in data.get("infoAdicionais", [])],
            pix_copy_paste=data.get("pixCopiaECola"),
            debtor=Debtor.from_dict(data["devedor"]) if data.get("devedor") else None,
            receiver=Receiver.from_dict(data["recebedor"]) if data.get("recebedor") else None,
            location=Location.from_dict(data["loc"]) if data.get("loc") else None,
            status=data.get("status"),
            value=DueBillingValue.from_dict(data["valor"]) if data.get("valor") else None,
            calendar=DueBillingCalendar.from_dict(data["calendario"]) if data.get("calendario") else None,
            txid=data.get("txid"),
            revision=data.get("revisao")
        )

    def to_dict(self) -> dict:
        """
        Convert the GeneratedDueBilling instance to a dictionary.

        Returns:
            dict: A dictionary representation of the GeneratedDueBilling instance.
        """
        return {
            "chave": self.key,
            "solicitacaoPagador": self.payer_request,
            "infoAdicionais": [info.to_dict() for info in self.additional_info],
            "pixCopiaECola": self.pix_copy_paste,
            "devedor": self.debtor.to_dict() if self.debtor else None,
            "recebedor": self.receiver.to_dict() if self.receiver else None,
            "loc": self.location.to_dict() if self.location else None,
            "status": self.status,
            "valor": self.value.to_dict() if self.value else None,
            "calendario": self.calendar.to_dict() if self.calendar else None,
            "txid": self.txid,
            "revisao": self.revision
        }