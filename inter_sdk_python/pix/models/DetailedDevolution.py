from dataclasses import dataclass
from typing import Optional

from inter_sdk_python.pix.enums.DevolutionNature import DevolutionNature
from inter_sdk_python.pix.models.CobMoment import CobMoment


@dataclass
class DetailedDevolution:
    """
    The DetailedDevolution class represents detailed information about a
    refund process.

    It includes fields such as the refund ID, the return
    transaction ID (rtrId), the amount of the refund, the current status,
    and the reason for the refund. Additionally, it supports the inclusion
    of any extra fields through a map for dynamic attributes that may not be
    predefined. This structure is essential for managing and processing
    refund-related information in billing systems.
    """

    id: Optional[str] = None
    """The unique identifier for the refund."""

    rtr_id: Optional[str] = None
    """The return transaction ID linked to the refund."""

    value: Optional[str] = None
    """The monetary value of the refund."""

    status: Optional[str] = None
    """The current status of the refund process."""

    reason: Optional[str] = None
    """The reason for initiating the refund."""

    nature: Optional[DevolutionNature] = None
    """The nature of the devolution."""

    description: Optional[str] = None
    """A description providing additional context about the refund."""

    moment: Optional[CobMoment] = None
    """The moment the refund process occurred."""

    @staticmethod
    def from_dict(data: dict) -> 'DetailedDevolution':
        """
        Create a DetailedDevolution instance from a dictionary.

        Args:
            data (dict): A dictionary containing the DetailedDevolution data.

        Returns:
            DetailedDevolution: An instance of DetailedDevolution.
        """
        return DetailedDevolution(
            id=data.get("id"),
            rtr_id=data.get("rtrId"),
            value=data.get("valor"),
            status=data.get("status"),
            reason=data.get("motivo"),
            nature=DevolutionNature(data["natureza"]) if data.get("natureza") else None,
            description=data.get("descricao"),
            moment=CobMoment.from_dict(data["horario"]) if data.get("horario") else None
        )

    def to_dict(self) -> dict:
        """
        Convert the DetailedDevolution instance to a dictionary.

        Returns:
            dict: A dictionary representation of the DetailedDevolution instance.
        """
        return {
            "id": self.id,
            "rtrId": self.rtr_id,
            "valor": self.value,
            "status": self.status,
            "motivo": self.reason,
            "natureza": self.nature.value if self.nature else None,
            "descricao": self.description,
            "horario": self.moment.to_dict() if self.moment else None
        }