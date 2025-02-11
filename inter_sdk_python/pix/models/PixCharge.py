from dataclasses import dataclass, field
from typing import Optional, List

from inter_sdk_python.pix.models.AdditionalInfo import AdditionalInfo
from inter_sdk_python.pix.models.Calendar import Calendar
from inter_sdk_python.pix.models.Debtor import Debtor
from inter_sdk_python.pix.models.Location import Location
from inter_sdk_python.pix.models.PixValue import PixValue


@dataclass
class PixCharge:
    """
    The PixCharge class represents a payment request or transaction
    details. It includes fields for the transaction ID (txid), calendar
    details, debtor information, location, transaction value (PixValue),
    key, payer request, and additional information.
    """

    transaction_id: Optional[str] = None
    """The transaction ID (txid) associated with the PIX charge."""

    calendar: Optional[Calendar] = None
    """The calendar details related to the transaction."""

    debtor: Optional[Debtor] = None
    """Information about the debtor."""

    loc: Optional[Location] = None
    """Location details associated with the PIX charge."""

    location: Optional[str] = None
    """A string representation of the location."""

    value: Optional[PixValue] = None
    """The transaction value represented by an instance of PixValue."""

    key: Optional[str] = None
    """The recipient's key used for the transfer."""

    payer_request: Optional[str] = None
    """The payer's request information as a string."""

    additional_info: List[AdditionalInfo] = field(default_factory=list)
    """Additional information related to the PIX charge as a list."""

    @staticmethod
    def from_dict(data: dict) -> 'PixCharge':
        """
        Create a PixCharge instance from a dictionary.

        Args:
            data (dict): A dictionary containing the PixCharge data.

        Returns:
            PixCharge: An instance of PixCharge.
        """
        return PixCharge(
            transaction_id=data.get("txid"),
            calendar=Calendar.from_dict(data["calendario"]) if data.get("calendario") else None,
            debtor=Debtor.from_dict(data["devedor"]) if data.get("devedor") else None,
            loc=Location.from_dict(data["loc"]) if data.get("loc") else None,
            location=data.get("location"),
            value=PixValue.from_dict(data["valor"]) if data.get("valor") else None,
            key=data.get("chave"),
            payer_request=data.get("solicitacaoPagador"),
            additional_info=[AdditionalInfo.from_dict(info) for info in data.get("infoAdicionais", [])]
        )

    def to_dict(self) -> dict:
        """
        Convert the PixCharge instance to a dictionary.

        Returns:
            dict: A dictionary representation of the PixCharge instance.
        """
        return {
            "txid": self.transaction_id,
            "calendario": self.calendar.to_dict() if self.calendar else None,
            "devedor": self.debtor.to_dict() if self.debtor else None,
            "loc": self.loc.to_dict() if self.loc else None,
            "location": self.location,
            "valor": self.value.to_dict() if self.value else None,
            "chave": self.key,
            "solicitacaoPagador": self.payer_request,
            "infoAdicionais": [info.to_dict() for info in self.additional_info]
        }