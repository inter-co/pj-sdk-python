from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class IncludePaymentResponse:
    """
    The IncludePaymentResponse class represents the response for including a payment,
    including approver details, payment status, transaction code, title, and message.
    """

    number_of_approvers: Optional[int] = None
    """The number of approvers required for the payment."""

    payment_status: Optional[str] = None
    """The current status of the payment."""

    transaction_code: Optional[str] = None
    """The unique code assigned to the transaction."""

    title: Optional[str] = None
    """The title associated with the payment."""

    message: Optional[str] = None
    """A message detailing the result of the payment request."""

    @staticmethod
    def from_dict(data: Dict) -> 'IncludePaymentResponse':
        """
        Create an IncludePaymentResponse instance from a dictionary.

        Args:
            data (dict): A dictionary containing payment response data.

        Returns:
            IncludePaymentResponse: An instance of IncludePaymentResponse.
        """
        return IncludePaymentResponse(
            number_of_approvers=data.get("quantidadeAprovadores"),
            payment_status=data.get("statusPagamento"),
            transaction_code=data.get("codigoTransacao"),
            title=data.get("titulo"),
            message=data.get("mensagem")
        )

    def to_dict(self) -> dict:
        """
        Convert the IncludePaymentResponse instance to a dictionary.

        Returns:
            dict: A dictionary representation of the IncludePaymentResponse instance.
        """
        return {
            "quantidadeAprovadores": self.number_of_approvers,
            "statusPagamento": self.payment_status,
            "codigoTransacao": self.transaction_code,
            "titulo": self.title,
            "mensagem": self.message
        }