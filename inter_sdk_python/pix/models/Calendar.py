from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Calendar:
    """
    The Calendar class represents the details of a calendar entry
    related to a transaction.

    It includes fields for the expiration period and created
    date, allowing for effective management of transaction timelines.
    """

    expiration: Optional[int] = None
    """The expiration period for the transaction."""

    creation_date: Optional[datetime] = None
    """The date when the transaction was created."""

    @staticmethod
    def from_dict(data: dict) -> 'Calendar':
        """
        Create a Calendar instance from a dictionary.

        Args:
            data (dict): A dictionary containing the calendar data.

        Returns:
            Calendar: An instance of Calendar.
        """
        return Calendar(
            expiration=data.get("expiracao"),
            creation_date=datetime.fromisoformat(data["criacao"]) if data.get("criacao") else None
        )

    def to_dict(self) -> dict:
        """
        Convert the Calendar instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Calendar instance.
        """
        return {
            "expiracao": self.expiration,
            "criacao": self.creation_date.isoformat() if self.creation_date else None
        }