from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from inter_sdk_python.pix.enums.ImmediateBillingType import ImmediateBillingType


@dataclass
class Location:
    """
    The Location class represents information about a payment location
    in a billing system. It includes fields such as the type of billing
    (CobType), a unique identifier for the location, the actual location
    value, and the creation date of the location entry. Additionally, it
    allows for the inclusion of any extra fields through a map for dynamic
    attributes that may not be predefined. This structure is essential for
    managing payment locations in the context of financial transactions.
    """

    billing_type: Optional[ImmediateBillingType] = None
    """The type of billing associated with the location."""

    id: Optional[int] = None
    """The unique identifier for the location."""

    location: Optional[str] = None
    """The actual location value."""

    creation_date: Optional[datetime] = None
    """The creation date of the location entry."""

    txid: Optional[str] = None
    """The transaction ID associated with the location."""

    @staticmethod
    def from_dict(data: dict) -> 'Location':
        """
        Create a Location instance from a dictionary.

        Args:
            data (dict): A dictionary containing the Location data.

        Returns:
            Location: An instance of Location.
        """
        return Location(
            billing_type=ImmediateBillingType(data["tipoCob"]) if data.get("tipoCob") else None,
            id=data.get("id"),
            location=data.get("location"),
            creation_date=datetime.fromisoformat(data["criacao"]) if data.get("criacao") else None,
            txid=data.get("txid")
        )

    def to_dict(self) -> dict:
        """
        Convert the Location instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Location instance.
        """
        return {
            "tipoCob": self.billing_type.value if self.billing_type else None,
            "id": self.id,
            "location": self.location,
            "criacao": self.creation_date.isoformat() if self.creation_date else None,
            "txid": self.txid
        }