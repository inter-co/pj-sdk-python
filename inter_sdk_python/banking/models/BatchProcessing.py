from dataclasses import dataclass
from typing import List, Optional, Dict, Union

from inter_sdk_python.banking.models.Batch import BilletBatch, DarfPaymentBatch


@dataclass
class BatchProcessing:
    """
    The BatchProcessing class represents the details of a batch payment processing,
    including bank account information, creation date, payment details, and status.
    """

    bank_account: Optional[str] = None
    """The bank account associated with the batch processing."""

    creation_date: Optional[str] = None
    """The date when the batch was created."""

    payments: Optional[List[Union[BilletBatch, DarfPaymentBatch]]] = None
    """A list of payments included in the batch processing."""

    batch_id: Optional[str] = None
    """The unique identifier for the batch."""

    status: Optional[str] = None
    """The current status of the batch processing."""

    my_identifier: Optional[str] = None
    """A unique identifier for the batch processing."""

    payment_quantity: Optional[int] = None
    """The quantity of payments included in the batch."""

    @staticmethod
    def from_dict(data: Dict) -> 'BatchProcessing':
        """
        Create a BatchProcessing instance from a dictionary.

        Args:
            data (dict): A dictionary containing the batch processing data.

        Returns:
            BatchProcessing: An instance of BatchProcessing.
        """
        payments = []
        if data.get("pagamentos") is not None:
            for item in data.get("pagamentos", []):
                if item.get("tipoPagamento") == "DARF":
                    payments.append(DarfPaymentBatch.from_dict(item))
                elif item.get("tipoPagamento") == "BOLETO":
                    payments.append(BilletBatch.from_dict(item))

        return BatchProcessing(
            bank_account=data.get("contaCorrente"),
            creation_date=data.get("dataCriacao"),
            payments=payments,
            batch_id=data.get("idLote"),
            status=data.get("status"),
            my_identifier=data.get("meuIdentificador"),
            payment_quantity=data.get("qtdePagamentos")
        )

    def to_dict(self) -> dict:
        """
        Convert the BatchProcessing instance to a dictionary.

        Returns:
            dict: A dictionary representation of the BatchProcessing instance.
        """
        dict_payments = []
        if self.payments is not None:
            for item in self.payments:
                if item.payment_type == "DARF":
                    dict_payments.append(item.darf_to_dict())
                elif item.get("tipoPagamento") == "BOLETO":
                    dict_payments.append(item.billet_to_dict())

        return {
            "contaCorrente": self.bank_account,
            "dataCriacao": self.creation_date,
            "pagamentos": dict_payments,
            "idLote": self.batch_id,
            "status": self.status,
            "meuIdentificador": self.my_identifier,
            "qtdePagamentos": self.payment_quantity
        }