import json
from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Dict, Union


@dataclass
class DarfPaymentBatch:
    payment_type: str = field(default="DARF", init=False)
    detail: Optional[str] = None
    transaction_id: Optional[str] = None
    status: Optional[str] = None
    cnpj_or_cpf: Optional[str] = None
    revenue_code: Optional[str] = None
    due_date: Optional[str] = None
    description: Optional[str] = None
    enterprise_name: Optional[str] = None
    enterprise_phone: Optional[str] = None
    assessment_period: Optional[str] = None
    payment_date: Optional[str] = None
    inclusion_date: Optional[str] = None
    value: Optional[Decimal] = None
    total_value: Optional[Decimal] = None
    fine_amount: Optional[Decimal] = None
    interest_amount: Optional[Decimal] = None
    reference: Optional[str] = None
    darf_type: Optional[str] = None
    type: Optional[str] = None
    principal_value: Optional[Decimal] = None

    @staticmethod
    def from_dict(data: Dict) -> 'DarfPaymentBatch':
        return DarfPaymentBatch(
            detail=data.get("detalhe"),
            transaction_id=data.get("idTransacao"),
            status=data.get("status"),
            cnpj_or_cpf=data.get("cnpjCpf"),
            revenue_code=data.get("codigoReceita"),
            due_date=data.get("dataVencimento"),
            description=data.get("descricao"),
            enterprise_name=data.get("nomeEmpresa"),
            enterprise_phone=data.get("telefoneEmpresa"),
            assessment_period=data.get("periodoApuracao"),
            payment_date=data.get("dataPagamento"),
            inclusion_date=data.get("dataInclusao"),
            value=Decimal(data.get("valor", 0)),
            total_value=Decimal(data.get("valorTotal", 0)),
            fine_amount=Decimal(data.get("valorMulta", 0)),
            interest_amount=Decimal(data.get("valorJuros", 0)),
            reference=data.get("referencia"),
            darf_type=data.get("tipoDarf"),
            type=data.get("tipo"),
            principal_value=Decimal(data.get("valorPrincipal", 0))
        )

    def darf_to_dict(self) -> dict:
        return {
            "tipoPagamento": self.payment_type,
            "detalhe": self.detail,
            "idTransacao": self.transaction_id,
            "status": self.status,
            "cnpjCpf": self.cnpj_or_cpf,
            "codigoReceita": self.revenue_code,
            "dataVencimento": self.due_date,
            "descricao": self.description,
            "nomeEmpresa": self.enterprise_name,
            "telefoneEmpresa": self.enterprise_phone,
            "periodoApuracao": self.assessment_period,
            "dataPagamento": self.payment_date,
            "dataInclusao": self.inclusion_date,
            "valor": float(self.value) if self.value is not None else None,
            "valorTotal": float(self.total_value) if self.total_value is not None else None,
            "valorMulta": float(self.fine_amount) if self.fine_amount is not None else None,
            "valorJuros": float(self.interest_amount) if self.interest_amount is not None else None,
            "referencia": self.reference,
            "tipoDarf": self.darf_type,
            "tipo": self.type,
            "valorPrincipal": float(self.principal_value) if self.principal_value is not None else None,
        }

@dataclass
class BilletBatch:
    payment_type: str = field(default="BOLETO", init=False)
    detail: Optional[str] = None
    transaction_id: Optional[str] = None
    status: Optional[str] = None
    barcode: Optional[str] = None
    amount_to_pay: Optional[Decimal] = None
    payment_date: Optional[str] = None
    due_date: Optional[str] = None
    beneficiary_document: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict) -> 'BilletBatch':
        return BilletBatch(
            detail=data.get("detalhe"),
            transaction_id=data.get("idTransacao"),
            status=data.get("status"),
            barcode=data.get("codBarraLinhaDigitavel"),
            amount_to_pay=Decimal(data.get("valorPagar", 0)),
            payment_date=data.get("dataPagamento"),
            due_date=data.get("dataVencimento"),
            beneficiary_document=data.get("cpfCnpjBeneficiario")
        )

    def billet_to_dict(self) -> dict:
        return {
            "tipoPagamento": self.payment_type,
            "detalhe": self.detail,
            "idTransacao": self.transaction_id,
            "status": self.status,
            "codBarraLinhaDigitavel": self.barcode,
            "valorPagar": float(self.amount_to_pay) if self.amount_to_pay is not None else None,
            "dataPagamento": self.payment_date,
            "dataVencimento": self.due_date,
            "cpfCnpjBeneficiario": self.beneficiary_document
        }

@dataclass
class Batch:
    my_identifier: Optional[str] = field(default=None)
    payments: Optional[List[Union[BilletBatch, DarfPaymentBatch]]] = field(default=None)

    @staticmethod
    def from_dict(data: Dict) -> 'Batch':
        payments = []
        for item in data.get("pagamentos", []):
            if item.get("tipoPagamento") == "DARF":
                payments.append(DarfPaymentBatch.from_dict(item))
            elif item.get("tipoPagamento") == "BOLETO":
                payments.append(BilletBatch.from_dict(item))
        return Batch(
            my_identifier=data.get("meuIdentificador"),
            payments=payments
        )

    def to_dict(self) -> dict:
        concatenated_payments = []
        if self.payments:
            for payment in self.payments:
                if isinstance(payment, DarfPaymentBatch):
                    concatenated_payments.append(payment.darf_to_dict())
                elif isinstance(payment, BilletBatch):
                    concatenated_payments.append(payment.billet_to_dict())
        return {
            "meuIdentificador": self.my_identifier,
            "pagamentos": concatenated_payments
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False)