from dataclasses import dataclass, field
from typing import Optional, List

from inter_sdk_python.pix.models.DevolutionRequestBody import DevolutionRequestBody
from inter_sdk_python.pix.models.ValueComponent import ValueComponent


@dataclass
class ItemPayload:
    """
    The ItemPayload class represents the payload for a transaction item,
    containing various attributes such as the key, value components,
    devolution requests, transaction IDs, timestamps, and payer information.
    """

    key: Optional[str] = None
    """The unique key associated with the transaction item."""

    value_components: Optional[ValueComponent] = None
    """The components of the value associated with the transaction item."""

    devolutions: List[DevolutionRequestBody] = field(default_factory=list)
    """A list of devolution requests related to the transaction item."""

    end_to_end_id: Optional[str] = None
    """The end-to-end identifier for the transaction."""

    timestamp: Optional[str] = None
    """The timestamp of the transaction item."""

    payer_info: Optional[str] = None
    """Information about the payer involved in the transaction."""

    txid: Optional[str] = None
    """The transaction ID associated with the item."""

    value: Optional[str] = None
    """The value associated with the transaction item."""

    @staticmethod
    def from_dict(data: dict) -> 'ItemPayload':
        """
        Create an ItemPayload instance from a dictionary.

        Args:
            data (dict): A dictionary containing the ItemPayload data.

        Returns:
            ItemPayload: An instance of ItemPayload.
        """
        return ItemPayload(
            key=data.get("chave"),
            value_components=ValueComponent.from_dict(data["componentesValor"]) if data.get("componentesValor") else None,
            devolutions=[DevolutionRequestBody.from_dict(dev) for dev in data.get("devolucoes", [])],
            end_to_end_id=data.get("endToEndId"),
            timestamp=data.get("horario"),
            payer_info=data.get("infoPagador"),
            txid=data.get("txid"),
            value=data.get("valor")
        )

    def to_dict(self) -> dict:
        """
        Convert the ItemPayload instance to a dictionary.

        Returns:
            dict: A dictionary representation of the ItemPayload instance.
        """
        return {
            "chave": self.key,
            "componentesValor": self.value_components.to_dict() if self.value_components else None,
            "devolucoes": [dev.to_dict() for dev in self.devolutions],
            "endToEndId": self.end_to_end_id,
            "horario": self.timestamp,
            "infoPagador": self.payer_info,
            "txid": self.txid,
            "valor": self.value
        }