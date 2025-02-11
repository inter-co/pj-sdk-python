from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List

from inter_sdk_python.pix.models.DetailedDevolution import DetailedDevolution
from inter_sdk_python.pix.models.ValueComponent import ValueComponent


@dataclass
class Pix:
    """
    The Pix class represents information related to a Pix payment.
    It includes fields such as the unique end-to-end identifier, transaction
    ID (txid), the amount of the payment, the recipient's key used for the
    transfer, the timestamp of the transaction, payer information, and a
    list of detailed refunds associated with this payment.
    """

    end_to_end_id: Optional[str] = None
    """The unique end-to-end identifier for the Pix transaction."""

    txid: Optional[str] = None
    """The transaction ID (txid) associated with the Pix payment."""

    value: Optional[str] = None
    """The amount of the payment in a string format."""

    key: Optional[str] = None
    """The recipient's key used for the transfer."""

    timestamp: Optional[datetime] = None
    """The timestamp of the transaction."""

    payer_info: Optional[str] = None
    """Information about the payer involved in the transaction."""

    refunds: List[DetailedDevolution] = field(default_factory=list)
    """A list of detailed refunds associated with the Pix payment."""

    value_components: Optional[ValueComponent] = None
    """Components of the value associated with the payment."""

    @staticmethod
    def from_dict(data: dict) -> 'Pix':
        """
        Create a Pix instance from a dictionary.

        Args:
            data (dict): A dictionary containing the Pix data.

        Returns:
            Pix: An instance of Pix.
        """
        return Pix(
            end_to_end_id=data.get("endToEndId"),
            txid=data.get("txid"),
            value=data.get("valor"),
            key=data.get("chave"),
            timestamp=datetime.fromisoformat(data["horario"]) if data.get("horario") else None,
            payer_info=data.get("infoPagador"),
            refunds=[DetailedDevolution.from_dict(refund) for refund in data.get("devolucoes", [])],
            value_components=ValueComponent.from_dict(data["componentesValor"]) if data.get("componentesValor") else None
        )

    def to_dict(self) -> dict:
        """
        Convert the Pix instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Pix instance.
        """
        return {
            "endToEndId": self.end_to_end_id,
            "txid": self.txid,
            "valor": self.value,
            "chave": self.key,
            "horario": self.timestamp.isoformat() if self.timestamp else None,
            "infoPagador": self.payer_info,
            "devolucoes": [refund.to_dict() for refund in self.refunds],
            "componentesValor": self.value_components.to_dict() if self.value_components else None
        }