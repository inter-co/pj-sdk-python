from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class IncludeDarfPaymentResponse:
    """
    The IncludeDarfPaymentResponse class represents the response for including a DARF payment,
    including approval details, authentication, payment date, return type, and request code.
    """

    approver_quantity: Optional[str] = None
    """The quantity of approvers required for the DARF payment."""

    authentication: Optional[str] = None
    """An authentication token or information for the payment request."""

    payment_date: Optional[str] = None
    """The date when the payment is scheduled or was processed."""

    return_type: Optional[str] = None
    """The type of return expected from the payment process."""

    request_code: Optional[str] = None
    """The unique code associated with the payment request."""

    @staticmethod
    def from_dict(data: Dict) -> 'IncludeDarfPaymentResponse':
        """
        Create an IncludeDarfPaymentResponse instance from a dictionary.

        Args:
            data (dict): A dictionary containing DARF payment response data.

        Returns:
            IncludeDarfPaymentResponse: An instance of IncludeDarfPaymentResponse.
        """
        return IncludeDarfPaymentResponse(
            approver_quantity=data.get("quantidadeAprovadores"),
            authentication=data.get("autenticacao"),
            payment_date=data.get("dataPagamento"),
            return_type=data.get("tipoRetorno"),
            request_code=data.get("codigoSolicitacao")
        )

    def to_dict(self) -> dict:
        """
        Convert the IncludeDarfPaymentResponse instance to a dictionary.

        Returns:
            dict: A dictionary representation of the IncludeDarfPaymentResponse instance.
        """
        return {
            "quantidadeAprovadores": self.approver_quantity,
            "autenticacao": self.authentication,
            "dataPagamento": self.payment_date,
            "tipoRetorno": self.return_type,
            "codigoSolicitacao": self.request_code
        }