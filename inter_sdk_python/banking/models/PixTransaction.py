from dataclasses import dataclass, field
from typing import Optional, List, Dict

from inter_sdk_python.banking.enums.PixStatus import PixStatus
from inter_sdk_python.banking.models.PixTransactionError import PixTransactionError
from inter_sdk_python.banking.models.Receiver import Receiver


@dataclass
class PixTransaction:
    """
    The PixTransaction class represents a PIX transaction,
    including details such as account information, receiver, errors, 
    transaction status, and timestamps.
    """

    account: Optional[str] = None
    """The account associated with the PIX transaction."""

    receiver: Optional[Receiver] = None
    """The receiver of the PIX transaction."""

    errors: List[PixTransactionError] = field(default_factory=list)
    """A list of errors related to the PIX transaction."""

    end_to_end: Optional[str] = None
    """The end-to-end identifier for the transaction."""

    value: Optional[int] = None
    """The value of the PIX transaction."""

    status: Optional[PixStatus] = None
    """The status of the PIX transaction, represented as a PixStatus enum."""

    movement_date_time: Optional[str] = None
    """The date and time of the transaction movement."""

    request_date_time: Optional[str] = None
    """The date and time when the request was made."""

    key: Optional[str] = None
    """The key used in the PIX transaction."""

    request_code: Optional[str] = None
    """The unique code for the PIX transaction request."""

    @staticmethod
    def from_dict(data: Dict) -> 'PixTransaction':
        """
        Create a PixTransaction instance from a dictionary.

        Args:
            data (dict): A dictionary containing PIX transaction data.

        Returns:
            PixTransaction: An instance of PixTransaction.
        """
        return PixTransaction(
            account=data.get("contaCorrente"),
            receiver=Receiver.from_dict(data["recebedor"]) if data.get("recebedor") else None,
            errors=[PixTransactionError.from_dict(error) for error in data.get("erros", [])],
            end_to_end=data.get("endToEnd"),
            value=data.get("valor"),
            status=PixStatus(data["status"]) if data.get("status") is not None else None,
            movement_date_time=data.get("dataHoraMovimento"),
            request_date_time=data.get("dataHoraSolicitacao"),
            key=data.get("chave"),
            request_code=data.get("codigoSolicitacao")
        )

    def to_dict(self) -> dict:
        """
        Convert the PixTransaction instance to a dictionary.

        Returns:
            dict: A dictionary representation of the PixTransaction instance.
        """
        return {
            "contaCorrente": self.account,
            "recebedor": self.receiver.to_dict() if self.receiver else None,
            "erros": [error.to_dict() for error in self.errors],
            "endToEnd": self.end_to_end,
            "valor": self.value,
            "status": self.status.value if self.status else None,
            "dataHoraMovimento": self.movement_date_time,
            "dataHoraSolicitacao": self.request_date_time,
            "chave": self.key,
            "codigoSolicitacao": self.request_code
        }