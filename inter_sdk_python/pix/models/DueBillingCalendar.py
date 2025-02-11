from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class DueBillingCalendar:
    """
    The DueBillingCalendar class represents the calendar details
    related to a billing transaction.

    It includes fields for the creation date, validity period
    after expiration, and the due date. This structure is essential for
    managing the timing and validity of billing processes.
    """

    creation_date: Optional[datetime] = None
    """The creation date of the billing entry."""

    validity_after_expiration: Optional[int] = None
    """The validity period after the due date."""

    due_date: Optional[str] = None
    """The due date for the billing transaction."""

    @staticmethod
    def from_dict(data: dict) -> 'DueBillingCalendar':
        """
        Create a DueBillingCalendar instance from a dictionary.

        Args:
            data (dict): A dictionary containing the DueBillingCalendar data.

        Returns:
            DueBillingCalendar: An instance of DueBillingCalendar.
        """
        return DueBillingCalendar(
            creation_date=datetime.fromisoformat(data["criacao"]) if data.get("criacao") else None,
            validity_after_expiration=data.get("validadeAposVencimento"),
            due_date=data.get("dataDeVencimento")
        )

    def to_dict(self) -> dict:
        """
        Convert the DueBillingCalendar instance to a dictionary.

        Returns:
            dict: A dictionary representation of the DueBillingCalendar instance.
        """
        return {
            "criacao": self.creation_date.isoformat() if self.creation_date else None,
            "validadeAposVencimento": self.validity_after_expiration,
            "dataDeVencimento": self.due_date
        }