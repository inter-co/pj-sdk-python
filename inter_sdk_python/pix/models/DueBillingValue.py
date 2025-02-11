from dataclasses import dataclass
from typing import Optional

from inter_sdk_python.pix.models.Discount import Discount
from inter_sdk_python.pix.models.Fees import Fees
from inter_sdk_python.pix.models.Fine import Fine
from inter_sdk_python.pix.models.Reduction import Reduction


@dataclass
class DueBillingValue:
    """
    The DueBillingValue class represents the structure of a billing
    value in a transaction.

    It includes fields for the original value, fines (Fine),
    fees (Fees), reductions (Reduction), and discounts (Discount).
    This structure allows for a comprehensive representation of all
    financial aspects related to the billing transaction.
    """

    original_value: Optional[str] = None
    """The original value of the billing transaction."""

    penalty: Optional[Fine] = None
    """The penalty associated with the billing transaction."""

    interest: Optional[Fees] = None
    """The fees associated with the billing transaction."""

    reduction: Optional[Reduction] = None
    """The reduction applied to the billing transaction."""

    discount: Optional[Discount] = None
    """The discount applied to the billing transaction."""

    @staticmethod
    def from_dict(data: dict) -> 'DueBillingValue':
        """
        Create a DueBillingValue instance from a dictionary.

        Args:
            data (dict): A dictionary containing the DueBillingValue data.

        Returns:
            DueBillingValue: An instance of DueBillingValue.
        """
        return DueBillingValue(
            original_value=data.get("original"),
            penalty=Fine.from_dict(data["multa"]) if data.get("multa") else None,
            interest=Fees.from_dict(data["juros"]) if data.get("juros") else None,
            reduction=Reduction.from_dict(data["abatimento"]) if data.get("abatimento") else None,
            discount=Discount.from_dict(data["desconto"]) if data.get("desconto") else None
        )

    def to_dict(self) -> dict:
        """
        Convert the DueBillingValue instance to a dictionary.

        Returns:
            dict: A dictionary representation of the DueBillingValue instance.
        """
        return {
            "original": self.original_value,
            "multa": self.penalty.to_dict() if self.penalty else None,
            "juros": self.interest.to_dict() if self.interest else None,
            "abatimento": self.reduction.to_dict() if self.reduction else None,
            "desconto": self.discount.to_dict() if self.discount else None
        }