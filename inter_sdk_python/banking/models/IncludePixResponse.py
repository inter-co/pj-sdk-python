from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class IncludePixResponse:
    """
    The IncludePixResponse class represents the response for including a PIX payment,
    including details like return type, end-to-end ID, request code, payment date, scheduling code, 
    operation date, and payment hour.
    """

    return_type: Optional[str] = None
    """The type of return expected from the PIX payment process."""

    end_to_end_id: Optional[str] = None
    """The unique identifier for the PIX transaction from end to end."""

    request_code: Optional[str] = None
    """The unique request code associated with the PIX payment."""

    payment_date: Optional[str] = None
    """The date when the payment is processed."""

    scheduling_code: Optional[str] = None
    """The code associated with the scheduling of the payment."""

    operation_date: Optional[str] = None
    """The date when the operation occurs."""

    payment_hour: Optional[str] = None
    """The hour at which the payment is processed."""

    @staticmethod
    def from_dict(data: Dict) -> 'IncludePixResponse':
        """
        Create an IncludePixResponse instance from a dictionary.

        Args:
            data (dict): A dictionary containing PIX payment response data.

        Returns:
            IncludePixResponse: An instance of IncludePixResponse.
        """
        return IncludePixResponse(
            return_type=data.get("tipoRetorno"),
            end_to_end_id=data.get("endToEndId"),
            request_code=data.get("codigoSolicitacao"),
            payment_date=data.get("dataPagamento"),
            scheduling_code=data.get("codigoAgendamento"),
            operation_date=data.get("dataOperacao"),
            payment_hour=data.get("horaPagamento")
        )

    def to_dict(self) -> dict:
        """
        Convert the IncludePixResponse instance to a dictionary.

        Returns:
            dict: A dictionary representation of the IncludePixResponse instance.
        """
        return {
            "tipoRetorno": self.return_type,
            "endToEndId": self.end_to_end_id,
            "codigoSolicitacao": self.request_code,
            "dataPagamento": self.payment_date,
            "codigoAgendamento": self.scheduling_code,
            "dataOperacao": self.operation_date,
            "horaPagamento": self.payment_hour
        }