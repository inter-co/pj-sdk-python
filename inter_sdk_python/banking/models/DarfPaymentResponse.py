from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, Dict


@dataclass
class DarfPaymentResponse:
    """
    The DarfPaymentResponse class represents the response for a DARF payment request,
    including various details about the payment, status, and amounts.
    """
    request_code: Optional[str] = None
    """The request code associated with the payment."""
    darf_type: Optional[str] = None
    """The type of DARF payment."""
    amount: Optional[Decimal] = None
    """The amount of the payment."""
    fine_amount: Optional[Decimal] = None
    """The amount of any fines applied to the payment."""
    interest_amount: Optional[Decimal] = None
    """The amount of any interest applied to the payment."""
    total_amount: Optional[Decimal] = None
    """The total amount to be paid, including any fines and interest."""
    type: Optional[str] = None
    """The specific type of payment."""
    assessment_period: Optional[str] = None
    """The assessment period for the revenue being paid."""
    payment_date: Optional[str] = None
    """The date the payment was made."""
    reference: Optional[str] = None
    """Any reference number related to the payment."""
    due_date: Optional[str] = None
    """The due date for the payment."""
    revenue_code: Optional[str] = None
    """The revenue code related to the payment."""
    payment_status: Optional[str] = None
    """The current status of the payment."""
    inclusion_date: Optional[str] = None
    """The date when the payment was included in the system."""
    cnpj_cpf: Optional[str] = None
    """The CNPJ or CPF associated with the payment."""
    necessary_approvals: Optional[int] = None
    """The number of approvals necessary for the payment."""
    realized_approvals: Optional[int] = None
    """The number of approvals that have been realized."""
    @staticmethod
    def from_dict(data: Dict) -> 'DarfPaymentResponse':
        """
        Create a DarfPaymentResponse instance from a dictionary.
        Args:
            data (dict): A dictionary containing the DARF payment response data.
        Returns:
            DarfPaymentResponse: An instance of DarfPaymentResponse.
        """
        return DarfPaymentResponse(
            request_code=data.get("codigoSolicitacao"),
            darf_type=data.get("tipoDarf"),
            amount=Decimal(data["valor"]) if data.get("valor") is not None else None,
            fine_amount=Decimal(data["valorMulta"]) if data.get("valorMulta") is not None else None,
            interest_amount=Decimal(data["valorJuros"]) if data.get("valorJuros") is not None else None,
            total_amount=Decimal(data["valorTotal"]) if data.get("valorTotal") is not None else None,
            type=data.get("tipo"),
            assessment_period=data.get("periodoApuracao"),
            payment_date=data.get("dataPagamento"),
            reference=data.get("referencia"),
            due_date=data.get("dataVencimento"),
            revenue_code=data.get("codigoReceita"),
            payment_status=data.get("statusPagamento"),
            inclusion_date=data.get("dataInclusao"),
            cnpj_cpf=data.get("cnpjCpf"),
            necessary_approvals=data.get("aprovacoesNecessarias"),
            realized_approvals=data.get("aprovacoesRealizadas")
        )
    def to_dict(self) -> dict:
        """
        Convert the DarfPaymentResponse instance to a dictionary.
        Returns:
            dict: A dictionary representation of the DarfPaymentResponse instance.
        """
        return {
            "codigoSolicitacao": self.request_code,
            "tipoDarf": self.darf_type,
            "valor": float(self.amount) if self.amount is not None else None,
            "valorMulta": float(self.fine_amount) if self.fine_amount is not None else None,
            "valorJuros": float(self.interest_amount) if self.interest_amount is not None else None,
            "valorTotal": float(self.total_amount) if self.total_amount is not None else None,
            "tipo": self.type,
            "periodoApuracao": self.assessment_period,
            "dataPagamento": self.payment_date,
            "referencia": self.reference,
            "dataVencimento": self.due_date,
            "codigoReceita": self.revenue_code,
            "statusPagamento": self.payment_status,
            "dataInclusao": self.inclusion_date,
            "cnpjCpf": self.cnpj_cpf,
            "aprovacoesNecessarias": self.necessary_approvals,
            "aprovacoesRealizadas": self.realized_approvals
        }