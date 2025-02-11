from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, Dict


@dataclass
class Payment:
    """
    The Payment class represents the details of a payment transaction,
    including amounts, dates, beneficiary information, and approval status.
    """
    transaction_code: Optional[str] = None
    """The unique code associated with the transaction."""
    barcode: Optional[str] = None
    """The barcode of the payment."""
    type: Optional[str] = None
    """The type of the payment transaction."""
    entered_due_date: Optional[str] = None
    """The due date entered by the user."""
    title_due_date: Optional[str] = None
    """The due date associated with the title."""
    inclusion_date: Optional[str] = None
    """The date when the payment was included."""
    payment_date: Optional[str] = None
    """The date when the payment was processed."""
    amount_paid: Optional[Decimal] = None
    """The amount that has been paid."""
    nominal_amount: Optional[Decimal] = None
    """The nominal amount of the payment."""
    payment_status: Optional[str] = None
    """The current status of the payment."""
    required_approvals: Optional[int] = None
    """The number of approvals required for the payment."""
    completed_approvals: Optional[int] = None
    """The number of approvals that have been completed."""
    beneficiary_cpf_cnpj: Optional[str] = None
    """The CPF or CNPJ of the beneficiary."""
    beneficiary_name: Optional[str] = None
    """The name of the beneficiary."""
    authentication: Optional[str] = None
    """Authentication information related to the payment."""
    @staticmethod
    def from_dict(data: Dict) -> 'Payment':
        """
        Create a Payment instance from a dictionary.
        Args:
            data (dict): A dictionary containing payment data.
        Returns:
            Payment: An instance of Payment.
        """
        return Payment(
            transaction_code=data.get("codigoTransacao"),
            barcode=data.get("codigoBarra"),
            type=data.get("tipo"),
            entered_due_date=data.get("dataVencimentoDigitada"),
            title_due_date=data.get("dataVencimentoTitulo"),
            inclusion_date=data.get("dataInclusao"),
            payment_date=data.get("dataPagamento"),
            amount_paid=Decimal(data["valorPago"]) if data.get("valorPago") is not None else None,
            nominal_amount=Decimal(data["valorNominal"]) if data.get("valorNominal") is not None else None,
            payment_status=data.get("statusPagamento"),
            required_approvals=data.get("aprovacoesNecessarias"),
            completed_approvals=data.get("aprovacoesRealizadas"),
            beneficiary_cpf_cnpj=data.get("cpfCnpjBeneficiario"),
            beneficiary_name=data.get("nomeBeneficiario"),
            authentication=data.get("autenticacao")
        )
    def to_dict(self) -> dict:
        """
        Convert the Payment instance to a dictionary.
        Returns:
            dict: A dictionary representation of the Payment instance.
        """
        return {
            "codigoTransacao": self.transaction_code,
            "codigoBarra": self.barcode,
            "tipo": self.type,
            "dataVencimentoDigitada": self.entered_due_date,
            "dataVencimentoTitulo": self.title_due_date,
            "dataInclusao": self.inclusion_date,
            "dataPagamento": self.payment_date,
            "valorPago": str(self.amount_paid) if self.amount_paid is not None else None,
            "valorNominal": str(self.nominal_amount) if self.nominal_amount is not None else None,
            "statusPagamento": self.payment_status,
            "aprovacoesNecessarias": self.required_approvals,
            "aprovacoesRealizadas": self.completed_approvals,
            "cpfCnpjBeneficiario": self.beneficiary_cpf_cnpj,
            "nomeBeneficiario": self.beneficiary_name,
            "autenticacao": self.authentication
        }