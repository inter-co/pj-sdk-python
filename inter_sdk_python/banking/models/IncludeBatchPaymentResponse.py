from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class IncludeBatchPaymentResponse:
    """
    The IncludeBatchPaymentResponse class represents the response for an include batch payment request,
    including the batch ID, status, custom identifier, and the quantity of payments.
    """

    batch_id: Optional[str] = None
    """The unique identifier for the payment batch."""

    status: Optional[str] = None
    """The current status of the batch payment."""

    my_identifier: Optional[str] = None
    """A custom identifier for the request made by the user."""

    payment_quantity: Optional[int] = None
    """The quantity of payments included in the batch."""

    @staticmethod
    def from_dict(data: Dict) -> 'IncludeBatchPaymentResponse':
        """
        Create an IncludeBatchPaymentResponse instance from a dictionary.

        Args:
            data (dict): A dictionary containing batch payment response data.

        Returns:
            IncludeBatchPaymentResponse: An instance of IncludeBatchPaymentResponse.
        """
        return IncludeBatchPaymentResponse(
            batch_id=data.get("idLote"),
            status=data.get("status"),
            my_identifier=data.get("meuIdentificador"),
            payment_quantity=data.get("qtdePagamentos")
        )

    def to_dict(self) -> dict:
        """
        Convert the IncludeBatchPaymentResponse instance to a dictionary.

        Returns:
            dict: A dictionary representation of the IncludeBatchPaymentResponse instance.
        """
        return {
            "idLote": self.batch_id,
            "status": self.status,
            "meuIdentificador": self.my_identifier,
            "qtdePagamentos": self.payment_quantity
        }