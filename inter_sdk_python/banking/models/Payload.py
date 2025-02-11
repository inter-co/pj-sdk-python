from dataclasses import dataclass, field
from typing import Optional, List, Dict

from inter_sdk_python.banking.models.CallbackError import CallbackError
from inter_sdk_python.banking.models.Receiver import Receiver


@dataclass
class Payload:
    """
    The Payload class represents the details of a payment payload,
    including transaction info, beneficiary details, and any associated errors.
    """

    transaction_code: Optional[str] = None
    """The unique code for the transaction."""

    digitable_line: Optional[str] = None
    """The digitable line associated with the payment."""

    movement_date_time: Optional[str] = None
    """The date and time of the movement."""

    request_date_time: Optional[str] = None
    """The date and time when the request was made."""

    beneficiary_name: Optional[str] = None
    """The name of the beneficiary for the payment."""

    scheduled_amount: Optional[str] = None
    """The scheduled amount for the payment."""

    paid_value: Optional[str] = None
    """The actual value that was paid."""

    end_to_end_id: Optional[str] = None
    """The unique identifier for the end-to-end transaction."""

    receiver: Optional[Receiver] = None
    """The receiver information for the payment."""

    status: Optional[str] = None
    """The current status of the transaction."""

    movement_type: Optional[str] = None
    """The type of movement (e.g., debit, credit)."""

    amount: Optional[str] = None
    """The amount associated with the transaction."""

    errors: List[CallbackError] = field(default_factory=list)
    """A list of callback errors related to the transaction."""

    payment_date: Optional[str] = None
    """The date when the payment was processed."""

    @staticmethod
    def from_dict(data: Dict) -> 'Payload':
        """
        Create a Payload instance from a dictionary.

        Args:
            data (dict): A dictionary containing payment payload data.

        Returns:
            Payload: An instance of Payload.
        """
        return Payload(
            transaction_code=data.get("codigoTransacao"),
            digitable_line=data.get("linhaDigitavel"),
            movement_date_time=data.get("dataHoraMovimento"),
            request_date_time=data.get("dataHoraSolicitacao"),
            beneficiary_name=data.get("nomeBeneficiario"),
            scheduled_amount=data.get("valorAgendado"),
            paid_value=data.get("valorPago"),
            end_to_end_id=data.get("endToEnd"),
            receiver=Receiver.from_dict(data["recebedor"]) if data.get("recebedor") else None,
            status=data.get("status"),
            movement_type=data.get("tipoMovimentacao"),
            amount=data.get("valor"),
            errors=[CallbackError.from_dict(error) for error in data.get("erros", [])],
            payment_date=data.get("dataPagamento")
        )

    def to_dict(self) -> dict:
        """
        Convert the Payload instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Payload instance.
        """
        return {
            "codigoTransacao": self.transaction_code,
            "linhaDigitavel": self.digitable_line,
            "dataHoraMovimento": self.movement_date_time,
            "dataHoraSolicitacao": self.request_date_time,
            "nomeBeneficiario": self.beneficiary_name,
            "valorAgendado": self.scheduled_amount,
            "valorPago": self.paid_value,
            "endToEnd": self.end_to_end_id,
            "recebedor": self.receiver.to_dict() if self.receiver else None,
            "status": self.status,
            "tipoMovimentacao": self.movement_type,
            "valor": self.amount,
            "erros": [error.to_dict() for error in self.errors],
            "dataPagamento": self.payment_date
        }