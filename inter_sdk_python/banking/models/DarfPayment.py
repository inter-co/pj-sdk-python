import json
from dataclasses import dataclass
from typing import Optional, Dict


@dataclass
class DarfPayment:
    """
    The DarfPayment class represents a payment for the DARF (Documento de Arrecadação de Receitas Federais),
    including various details related to the payment.
    """
    cnpj_or_cpf: Optional[str] = None
    """The CNPJ or CPF associated with the payment."""
    revenue_code: Optional[str] = None
    """The revenue code related to the payment."""
    due_date: Optional[str] = None
    """The due date for the payment."""
    description: Optional[str] = None
    """A description of the payment."""
    enterprise_name: Optional[str] = None
    """The name of the enterprise making the payment."""
    enterprise_phone: Optional[str] = None
    """The contact phone number of the enterprise."""
    assessment_period: Optional[str] = None
    """The assessment period for the revenue being paid."""
    payment_date: Optional[str] = None
    """The date when the payment was made."""
    inclusion_date: Optional[str] = None
    """The date when the payment was included in the system."""
    value: Optional[str] = None
    """The value of the payment."""
    total_value: Optional[str] = None
    """The total value to be paid including fines and interest."""
    fine_amount: Optional[str] = None
    """The amount of any fines applied to the payment."""
    interest_amount: Optional[str] = None
    """The amount of any interest applied to the payment."""
    reference: Optional[str] = None
    """Any reference number related to the payment."""
    darf_type: Optional[str] = None
    """The type of DARF payment."""
    type: Optional[str] = None
    """The specific type of related payment."""
    principal_value: Optional[str] = None
    """The principal amount being paid."""
    @staticmethod
    def from_dict(data: Dict) -> 'DarfPayment':
        """
        Create a DarfPayment instance from a dictionary.
        Args:
            data (dict): A dictionary containing the DARF payment data.
        Returns:
            DarfPayment: An instance of DarfPayment.
        """
        return DarfPayment(
            cnpj_or_cpf=data.get("cnpjCpf"),
            revenue_code=data.get("codigoReceita"),
            due_date=data.get("dataVencimento"),
            description=data.get("descricao"),
            enterprise_name=data.get("nomeEmpresa"),
            enterprise_phone=data.get("telefoneEmpresa"),
            assessment_period=data.get("periodoApuracao"),
            payment_date=data.get("dataPagamento"),
            inclusion_date=data.get("dataInclusao"),
            value=data.get("valor"),
            total_value=data.get("valorTotal"),
            fine_amount=data.get("valorMulta"),
            interest_amount=data.get("valorJuros"),
            reference=data.get("referencia"),
            darf_type=data.get("tipoDarf"),
            type=data.get("tipo"),
            principal_value=data.get("valorPrincipal")
        )
    def to_dict(self) -> dict:
            """
            Convert the DarfPayment instance to a dictionary.
            Returns:
                dict: A dictionary representation of the DarfPayment instance.
            """
            return {
                "cnpjCpf": self.cnpj_or_cpf,
                "codigoReceita": self.revenue_code,
                "dataVencimento": self.due_date,
                "descricao": self.description,
                "nomeEmpresa": self.enterprise_name,
                "telefoneEmpresa": self.enterprise_phone,
                "periodoApuracao": self.assessment_period,
                "dataPagamento": self.payment_date,
                "dataInclusao": self.inclusion_date,
                "valor": self.value,
                "valorTotal": self.total_value,
                "valorMulta": self.fine_amount,
                "valorJuros": self.interest_amount,
                "referencia": self.reference,
                "tipoDarf": self.darf_type,
                "tipo": self.type,
                "valorPrincipal": self.principal_value
        }
    def to_json(self) -> str:
        """
        Convert the DarfPayment instance to a JSON string.
        Returns:
            str: A JSON string representation of the DarfPayment instance.
        """
        return json.dumps(self.to_dict(), ensure_ascii=False)