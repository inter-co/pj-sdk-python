import json
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, Dict

from inter_sdk_python.billing.models.Discount import Discount
from inter_sdk_python.billing.models.Fine import Fine
from inter_sdk_python.billing.models.Message import Message
from inter_sdk_python.billing.models.Mora import Mora
from inter_sdk_python.billing.models.Person import Person


@dataclass
class BillingIssueRequest:
    """
    The BillingIssueRequest class represents a request to issue a billing,
    including details such as nominal value, due date, payer information,
    and optional attributes like discounts, fines, and messages.
    """
    your_number: Optional[str] = None
    """The unique identifier for the billing request."""
    nominal_value: Optional[Decimal] = None
    """The nominal value of the billing."""
    due_date: Optional[str] = None
    """The due date for the payment."""
    scheduled_days: Optional[int] = None
    """The number of scheduled days for the billing."""
    payer: Optional[Person] = None
    """The person who is the payer of the billing."""
    discount: Optional[Discount] = None
    """Optional discounts applicable to the billing."""
    fine: Optional[Fine] = None
    """Optional fines applicable for late payment."""
    mora: Optional[Mora] = None
    """Optional mora details for overdue payments."""
    message: Optional[Message] = None
    """Optional message associated with the billing."""
    final_beneficiary: Optional[Person] = None
    """The final beneficiary of the billing."""
    receiving_method: Optional[str] = None
    """The method of receiving payment described in a string."""

    @staticmethod
    def from_dict(data: Dict) -> 'BillingIssueRequest':
        """
        Create a BillingIssueRequest instance from a dictionary.
        Args:
            data (dict): A dictionary containing billing issue request data.
        Returns:
            BillingIssueRequest: An instance of BillingIssueRequest.
        """
        return BillingIssueRequest(
            your_number=data.get("seuNumero"),
            nominal_value=Decimal(data["valorNominal"]) if data.get("valorNominal") is not None else None,
            due_date=data.get("dataVencimento"),
            scheduled_days=data.get("numDiasAgenda"),
            payer=Person.from_dict(data["pagador"]) if data.get("pagador") else None,
            discount=Discount.from_dict(data["desconto"]) if data.get("desconto") else None,
            fine=Fine.from_dict(data["multa"]) if data.get("multa") else None,
            mora=Mora.from_dict(data["mora"]) if data.get("mora") else None,
            message=Message.from_dict(data["mensagem"]) if data.get("mensagem") else None,
            final_beneficiary=Person.from_dict(data["beneficiarioFinal"]) if data.get("beneficiarioFinal") else None,
            receiving_method=data.get("formasRecebimento")
        )
    def to_dict(self) -> dict:
        """
        Convert the BillingIssueRequest instance to a dictionary.
        Returns:
            dict: A dictionary representation of the BillingIssueRequest instance.
        """
        return {
            "seuNumero": self.your_number,
            "valorNominal": str(self.nominal_value) if self.nominal_value else None,
            "dataVencimento": self.due_date,
            "numDiasAgenda": self.scheduled_days,
            "pagador": self.payer.to_dict() if self.payer else None,
            "desconto": self.discount.to_dict() if self.discount else None,
            "multa": self.fine.to_dict() if self.fine else None,
            "mora": self.mora.to_dict() if self.mora else None,
            "mensagem": self.message.to_dict() if self.message else None,
            "beneficiarioFinal": self.final_beneficiary.to_dict() if self.final_beneficiary else None,
            "formasRecebimento": self.receiving_method
        }

    def to_json(self) -> str:
            """
            Convert the BillingIssueRequest instance to a JSON string.
            Returns:
                str: A JSON string representation of the BillingIssueRequest instance.
            """
            return json.dumps(self.to_dict(), ensure_ascii=False)