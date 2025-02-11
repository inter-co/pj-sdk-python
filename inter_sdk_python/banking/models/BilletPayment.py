import json
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, Dict


@dataclass
class BilletPayment:
    """
    The BilletPayment class represents the details of a boleto payment,
    including payment amount, dates, and beneficiary information.
    """

    barcode: Optional[str] = None
    """The barcode or printed line of the boleto."""

    amount_to_pay: Optional[Decimal] = None
    """The amount to be paid for the boleto."""

    payment_date: Optional[str] = None
    """The date when the payment is made."""

    due_date: Optional[str] = None
    """The due date for the boleto payment."""

    beneficiary_document: Optional[str] = None
    """The CPF or CNPJ of the beneficiary."""

    @staticmethod
    def from_dict(data: Dict) -> 'BilletPayment':
        """
        Create a BilletPayment instance from a dictionary.

        Args:
            data (dict): A dictionary containing the billet payment data.

        Returns:
            BilletPayment: An instance of BilletPayment.
        """
        return BilletPayment(
            barcode=data.get("codBarraLinhaDigitavel"),
            amount_to_pay=Decimal(data["valorPagar"]) if data.get("valorPagar") is not None else None,
            payment_date=data.get("dataPagamento"),
            due_date=data.get("dataVencimento"),
            beneficiary_document=data.get("cpfCnpjBeneficiario")
        )

    def to_dict(self) -> dict:
        """
        Convert the BilletPayment instance to a dictionary.

        Returns:
            dict: A dictionary representation of the BilletPayment instance.
        """
        return {
            "codBarraLinhaDigitavel": self.barcode,
            "valorPagar": float(self.amount_to_pay) if self.amount_to_pay is not None else None,
            "dataPagamento": self.payment_date,
            "dataVencimento": self.due_date,
            "cpfCnpjBeneficiario": self.beneficiary_document
        }

    def to_json(self) -> str:
        """
        Convert the BilletPayment instance to a JSON string.

        Returns:
            str: A JSON string representation of the BilletPayment instance.
        """
        return json.dumps(self.to_dict(), ensure_ascii=False)