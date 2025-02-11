import json
from dataclasses import dataclass, field
from typing import Optional, List

from inter_sdk_python.pix.models.AdditionalInfo import AdditionalInfo
from inter_sdk_python.pix.models.Debtor import Debtor
from inter_sdk_python.pix.models.DueBillingCalendar import DueBillingCalendar
from inter_sdk_python.pix.models.DueBillingValue import DueBillingValue
from inter_sdk_python.pix.models.Location import Location


@dataclass
class DueBilling:
    """
    The DueBilling class represents the details of a billing
    transaction that is due for payment.

    It includes fields for a unique key, payer's request,
    additional information, debtor details, location, due billing
    value, due billing calendar, and transaction ID (txid). It also
    supports additional custom fields through a map of additional
    attributes.
    """

    key: Optional[str] = None
    """The unique key for the billing transaction."""

    payer_request: Optional[str] = None
    """The payer's request associated with the transaction."""

    additional_info: List[AdditionalInfo] = field(default_factory=list)
    """Additional information relevant to the billing transaction."""

    debtor: Optional[Debtor] = None
    """The debtor associated with the billing transaction."""

    location: Optional[Location] = None
    """The location relevant to the billing transaction."""

    value: Optional[DueBillingValue] = None
    """The due billing value for the transaction."""

    calendar: Optional[DueBillingCalendar] = None
    """The calendar associated with the billing."""

    txid: Optional[str] = None
    """The transaction ID associated with the billing."""

    @staticmethod
    def from_dict(data: dict) -> 'DueBilling':
        """
        Create a DueBilling instance from a dictionary.

        Args:
            data (dict): A dictionary containing the DueBilling data.

        Returns:
            DueBilling: An instance of DueBilling.
        """
        return DueBilling(
            key=data.get("chave"),
            payer_request=data.get("solicitacaoPagador"),
            additional_info=[AdditionalInfo.from_dict(info) for info in data.get("infoAdicionais", [])],
            debtor=Debtor.from_dict(data["devedor"]) if data.get("devedor") else None,
            location=Location.from_dict(data["loc"]) if data.get("loc") else None,
            value=DueBillingValue.from_dict(data["valor"]) if data.get("valor") else None,
            calendar=DueBillingCalendar.from_dict(data["calendario"]) if data.get("calendario") else None,
            txid=data.get("txid")
        )

    def to_dict(self) -> dict:
        """
        Convert the DueBilling instance to a dictionary.

        Returns:
            dict: A dictionary representation of the DueBilling instance.
        """
        return {
            "chave": self.key,
            "solicitacaoPagador": self.payer_request,
            "infoAdicionais": [info.to_dict() for info in self.additional_info],
            "devedor": self.debtor.to_dict() if self.debtor else None,
            "loc": self.location.to_dict() if self.location else None,
            "valor": self.value.to_dict() if self.value else None,
            "calendario": self.calendar.to_dict() if self.calendar else None,
            "txid": self.txid
        }
    
    def to_json(self) -> str:
        """
        Convert the DueBilling instance to a JSON string.
        Returns:
            str: A JSON string representation of the DueBilling instance.
        """
        return json.dumps(self.to_dict(), ensure_ascii=False)