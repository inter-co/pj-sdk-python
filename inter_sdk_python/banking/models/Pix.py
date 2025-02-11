import json
from dataclasses import dataclass
from typing import Optional, Dict

from inter_sdk_python.banking.models.Recipient import Recipient


@dataclass
class Pix:
    """
    The Pix class represents a PIX payment transaction,
    including details such as amount, payment date, description, and recipient.
    """

    amount: Optional[str] = None
    """The amount of the PIX transaction."""

    payment_date: Optional[str] = None
    """The date when the payment is made."""

    description: Optional[str] = None
    """A description of the PIX transaction."""

    recipient: Optional[Recipient] = None
    """The recipient of the PIX payment."""

    @staticmethod
    def from_dict(data: Dict) -> 'Pix':
        """
        Create a Pix instance from a dictionary.

        Args:
            data (dict): A dictionary containing PIX payment data.

        Returns:
            Pix: An instance of Pix.
        """
        return Pix(
            amount=data.get("valor"),
            payment_date=data.get("dataPagamento"),
            description=data.get("descricao"),
            recipient=Recipient.from_dict(data["destinatario"]) if data.get("destinatario") else None
        )

    def to_dict(self) -> dict:
        """
        Convert the Pix instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Pix instance.
        """
        return {
            "valor": self.amount,
            "dataPagamento": self.payment_date,
            "descricao": self.description,
            "destinatario": self.recipient.to_dict() if self.recipient else None
        }

    def to_json(self) -> str:
        """
        Convert the Pix instance to a JSON string.

        Returns:
            str: A JSON string representation of the Pix instance.
        """
        return json.dumps(self.to_dict(), ensure_ascii=False)