from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class CobMoment:
    """
    The CobMoment class represents the moments associated
    with a charge, specifically the request and liquidation dates.

    This class provides a structure for holding important
    timestamps related to the charging process.
    """

    request: Optional[datetime] = None
    """The date and time when the charge request was made."""

    liquidation: Optional[datetime] = None
    """The date and time when the charge was liquidated."""

    @staticmethod
    def from_dict(data: dict) -> 'CobMoment':
        """
        Create a CobMoment instance from a dictionary.

        Args:
            data (dict): A dictionary containing the CobMoment data.

        Returns:
            CobMoment: An instance of CobMoment.
        """
        return CobMoment(
            request=datetime.fromisoformat(data["solicitacao"]) if data.get("solicitacao") else None,
            liquidation=datetime.fromisoformat(data["liquidacao"]) if data.get("liquidacao") else None
        )

    def to_dict(self) -> dict:
        """
        Convert the CobMoment instance to a dictionary.

        Returns:
            dict: A dictionary representation of the CobMoment instance.
        """
        return {
            "solicitacao": self.request.isoformat() if self.request else None,
            "liquidacao": self.liquidation.isoformat() if self.liquidation else None
        }