from dataclasses import dataclass
from typing import Optional, Dict

from inter_sdk_python.banking.enums.PixStatus import PixStatus


@dataclass
class PixHistoryEntity:
    """
    The PixHistoryEntity class represents a historical entry 
    for a PIX transaction, including its status and event date/time.
    """

    status: Optional[PixStatus] = None
    """The status of the PIX transaction, represented as a PixStatus enum."""

    event_date_time: Optional[str] = None
    """The date and time when the event occurred."""

    @staticmethod
    def from_dict(data: Dict) -> 'PixHistoryEntity':
        """
        Create a PixHistoryEntity instance from a dictionary.

        Args:
            data (dict): A dictionary containing PIX history data.

        Returns:
            PixHistoryEntity: An instance of PixHistoryEntity.
        """
        return PixHistoryEntity(
            status=PixStatus(data["status"]) if data.get("status") is not None else None,
            event_date_time=data.get("dataHoraEvento")
        )

    def to_dict(self) -> dict:
        """
        Convert the PixHistoryEntity instance to a dictionary.

        Returns:
            dict: A dictionary representation of the PixHistoryEntity instance.
        """
        return {
            "status": self.status.value if self.status else None,
            "dataHoraEvento": self.event_date_time
        }