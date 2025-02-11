from dataclasses import dataclass
from typing import Optional

from inter_sdk_python.pix.enums.ImmediateBillingType import ImmediateBillingType


@dataclass
class IncludeLocationRequest:
    """
    The IncludeLocationRequest class represents a request
    to include location details for immediate billing.

    It contains the type of immediate billing that is associated
    with the location request.
    """

    immediate_billing_type: Optional[ImmediateBillingType] = None
    """The type of immediate billing associated with the location."""

    @staticmethod
    def from_dict(data: dict) -> 'IncludeLocationRequest':
        """
        Create an IncludeLocationRequest instance from a dictionary.

        Args:
            data (dict): A dictionary containing the IncludeLocationRequest data.

        Returns:
            IncludeLocationRequest: An instance of IncludeLocationRequest.
        """
        return IncludeLocationRequest(
            immediate_billing_type=ImmediateBillingType(data["tipoCob"]) if data.get("tipoCob") else None
        )

    def to_dict(self) -> dict:
        """
        Convert the IncludeLocationRequest instance to a dictionary.

        Returns:
            dict: A dictionary representation of the IncludeLocationRequest instance.
        """
        return {
            "tipoCob": self.immediate_billing_type.value if self.immediate_billing_type else None
        }