from dataclasses import dataclass, field
from typing import Optional, List, Dict

from inter_sdk_python.banking.models.PixHistoryEntity import PixHistoryEntity
from inter_sdk_python.banking.models.PixTransaction import PixTransaction


@dataclass
class RetrievePixResponse:
    """
    The RetrievePixResponse class represents the response 
    received when retrieving a PIX transaction and its history.
    """

    pix_transaction: Optional[PixTransaction] = None
    """The PIX transaction details."""

    history: List[PixHistoryEntity] = field(default_factory=list)
    """A list of historical entries related to the PIX transaction."""

    @staticmethod
    def from_dict(data: Dict) -> 'RetrievePixResponse':
        """
        Create a RetrievePixResponse instance from a dictionary.

        Args:
            data (dict): A dictionary containing PIX response data.

        Returns:
            RetrievePixResponse: An instance of RetrievePixResponse.
        """
        return RetrievePixResponse(
            pix_transaction=PixTransaction.from_dict(data["transacaoPix"]) if data.get("transacaoPix") else None,
            history=[PixHistoryEntity.from_dict(item) for item in data.get("historico", [])]
        )

    def to_dict(self) -> dict:
        """
        Convert the RetrievePixResponse instance to a dictionary.

        Returns:
            dict: A dictionary representation of the RetrievePixResponse instance.
        """
        return {
            "transacaoPix": self.pix_transaction.to_dict() if self.pix_transaction else None,
            "historico": [item.to_dict() for item in self.history]
        }