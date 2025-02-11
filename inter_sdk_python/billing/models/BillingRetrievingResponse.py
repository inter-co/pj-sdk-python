from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, List

from inter_sdk_python.billing.enums.BillingSituation import BillingSituation
from inter_sdk_python.billing.enums.BillingType import BillingType
from inter_sdk_python.billing.enums.ReceivingOrigin import ReceivingOrigin
from inter_sdk_python.billing.models.Discount import Discount
from inter_sdk_python.billing.models.Fine import Fine
from inter_sdk_python.billing.models.Mora import Mora
from inter_sdk_python.billing.models.Person import Person


@dataclass
class BillingRetrievingResponse:
    """
    The BillingRetrievingResponse class represents the response received
    when retrieving billing information.

    It contains various details including the request code, issue number,
    issue and due dates, nominal value, billing type, billing situation, total amount
    received, discounts, fines, interest, and payer information.
    """

    request_code: Optional[str] = None
    """The request code associated with the billing retrieval."""

    your_number: Optional[str] = None
    """A custom identifier for the billing statement."""

    issue_date: Optional[str] = None
    """The date when the billing was issued."""

    due_date: Optional[str] = None
    """The due date for the payment."""

    nominal_value: Optional[Decimal] = None
    """The nominal value of the billing statement."""

    billing_type: Optional[BillingType] = None
    """The type of billing being retrieved."""

    situation: Optional[BillingSituation] = None
    """The current situation of the billing."""

    situation_date: Optional[str] = None
    """The date associated with the current situation of the billing."""

    total_amount_received: Optional[str] = None
    """The total amount received for the billing."""

    receiving_origin: Optional[ReceivingOrigin] = None
    """The origin of the payment reception."""

    cancellation_reason: Optional[str] = None
    """The reason for cancellation, if applicable."""

    archived: Optional[bool] = None
    """Indicates whether the billing statement has been archived."""

    discounts: List[Discount] = field(default_factory=list)
    """A list of applicable discounts on the billing statement."""

    fine: Optional[Fine] = None
    """The fine applicable for late payments."""

    interest: Optional[Mora] = None
    """The interest applicable for late payments."""

    payer: Optional[Person] = None
    """The payer's information."""

    @staticmethod
    def from_dict(data: dict) -> 'BillingRetrievingResponse':
        """
        Create a BillingRetrievingResponse instance from a dictionary.

        Args:
            data (dict): A dictionary containing the billing retrieving response data.

        Returns:
            BillingRetrievingResponse: An instance of BillingRetrievingResponse.
        """
        return BillingRetrievingResponse(
            request_code=data.get("codigoSolicitacao"),
            your_number=data.get("seuNumero"),
            issue_date=data.get("dataEmissao"),
            due_date=data.get("dataVencimento"),
            nominal_value=Decimal(data["valorNominal"]) if data.get("valorNominal") else None,
            billing_type=BillingType(data["tipoCobranca"]) if data.get("tipoCobranca") else None,
            situation=BillingSituation(data["situacao"]) if data.get("situacao") else None,
            situation_date=data.get("dataSituacao"),
            total_amount_received=data.get("valorTotalRecebido"),
            receiving_origin=ReceivingOrigin(data["origemRecebimento"]) if data.get("origemRecebimento") else None,
            cancellation_reason=data.get("motivoCancelamento"),
            archived=data.get("arquivada"),
            discounts=[Discount.from_dict(d) for d in data.get("descontos", [])],
            fine=Fine.from_dict(data["multa"]) if data.get("multa") else None,
            interest=Mora.from_dict(data["mora"]) if data.get("mora") else None,
            payer=Person.from_dict(data["pagador"]) if data.get("pagador") else None
        )

    def to_dict(self) -> dict:
        """
        Convert the BillingRetrievingResponse instance to a dictionary.
        Returns:
            dict: A dictionary containing the billing retrieving response data.
        """
        return {
            "codigoSolicitacao": self.request_code,
            "seuNumero": self.your_number,
            "dataEmissao": self.issue_date,
            "dataVencimento": self.due_date,
            "valorNominal": float(self.nominal_value) if self.nominal_value is not None else None,
            "tipoCobranca": self.billing_type.name if self.billing_type else None,
            "situacao": self.situation.name if self.situation else None,
            "dataSituacao": self.situation_date,
            "valorTotalRecebido": self.total_amount_received,
            "origemRecebimento": self.receiving_origin.name if self.receiving_origin else None,
            "motivoCancelamento": self.cancellation_reason,
            "arquivada": self.archived,
            "descontos": [discount.to_dict() for discount in self.discounts],
            "multa": self.fine.to_dict() if self.fine else None,
            "mora": self.interest.to_dict() if self.interest else None,
            "pagador": self.payer.to_dict() if self.payer else None
        }