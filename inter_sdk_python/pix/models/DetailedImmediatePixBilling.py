from dataclasses import dataclass, field
from typing import Optional, List

from inter_sdk_python.pix.models.AdditionalInfo import AdditionalInfo
from inter_sdk_python.pix.models.Calendar import Calendar
from inter_sdk_python.pix.models.Debtor import Debtor
from inter_sdk_python.pix.models.Location import Location
from inter_sdk_python.pix.models.Pix import Pix
from inter_sdk_python.pix.models.PixValue import PixValue


@dataclass
class DetailedImmediatePixBilling:
    """
    The DetailedImmediatePixBilling class extends the basic charge details by
    adding additional fields specific to a detailed view of a PIX charge.

    It includes the location of the transaction, the current status,
    a copy-paste (copia e cola) representation of the PIX transaction,
    a revision number, and a list of PIX transactions. This structure
    provides comprehensive details necessary for tracking and managing
    specific charge instances within the PIX system.
    """

    debtor: Optional[Debtor] = None
    """The debtor associated with the PIX charge."""

    value: Optional[PixValue] = None
    """The value of the PIX charge."""

    key: Optional[str] = None
    """The key associated with the PIX transaction."""

    calendar: Optional[Calendar] = None
    """The calendar information related to the PIX charge."""

    txid: Optional[str] = None
    """The transaction ID related to the PIX charge."""

    status: Optional[str] = None
    """The current status of the PIX charge."""

    pix_copy_and_paste: Optional[str] = None
    """The PIX copy and paste information."""

    revision: Optional[int] = None
    """The revision number for the PIX charge."""

    pix_transactions: List[Pix] = field(default_factory=list)
    """A list of PIX transactions associated with the charge."""

    transaction_id: Optional[str] = None
    """The transaction ID (txid) associated with the PIX charge."""

    loc: Optional[Location] = None
    """Location details associated with the PIX charge."""

    location: Optional[str] = None
    """A string representation of the location."""

    payer_request: Optional[str] = None
    """The payer's request information as a string."""

    additional_info: List[AdditionalInfo] = field(default_factory=list)
    """Additional information related to the PIX charge as a list."""

    @staticmethod
    def from_dict(data: dict) -> 'DetailedImmediatePixBilling':
        """
        Create a DetailedImmediatePixBilling instance from a dictionary.

        Args:
            data (dict): A dictionary containing the DetailedImmediatePixBilling data.

        Returns:
            DetailedImmediatePixBilling: An instance of DetailedImmediatePixBilling.
        """
        return DetailedImmediatePixBilling(
            debtor=Debtor.from_dict(data["devedor"]) if data.get("devedor") else None,
            value=PixValue.from_dict(data["valor"]) if data.get("valor") else None,
            key=data.get("chave"),
            calendar=Calendar.from_dict(data["calendario"]) if data.get("calendario") else None,
            txid=data.get("txid"),
            status=data.get("status"),
            pix_copy_and_paste=data.get("pixCopiaECola"),
            revision=data.get("revisao"),
            pix_transactions=[Pix.from_dict(pix) for pix in data.get("pix", [])],
            transaction_id=data.get("transactionId"),
            loc=Location.from_dict(data["loc"]) if data.get("loc") else None,
            location=data.get("localizacao"),
            payer_request=data.get("pedidoPayer"),
            additional_info = [AdditionalInfo.from_dict(info) for info in data.get("informacoesAdicionais", [])]
        )

    def to_dict(self) -> dict:
        """
        Convert the DetailedImmediatePixBilling instance to a dictionary.

        Returns:
            dict: A dictionary representation of the DetailedImmediatePixBilling instance.
        """
        return {
            "devedor": self.debtor.to_dict() if self.debtor else None,
            "valor": self.value.to_dict() if self.value else None,
            "chave": self.key,
            "calendario": self.calendar.to_dict() if self.calendar else None,
            "txid": self.txid,
            "status": self.status,
            "pixCopiaECola": self.pix_copy_and_paste,
            "revisao": self.revision,
            "pix": [pix.to_dict() for pix in self.pix_transactions],
            "transactionId": self.transaction_id,
            "loc": self.loc.to_dict() if self.loc else None,
            "localizacao": self.location,
            "pedidoPayer": self.payer_request,
            "informacoesAdicionais": [info.to_dict() for info in self.additional_info]
        }