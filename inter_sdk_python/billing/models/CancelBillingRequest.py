import json
from dataclasses import dataclass
from typing import Optional


@dataclass
class CancelBillingRequest:
    """
    The CancelBillingRequest class represents a request to cancel a billing.

    This class includes the reason for cancellation and allows for the
    inclusion of additional fields that may be required by the specific use case.
    """

    cancellation_reason: Optional[str] = None
    """The reason for canceling the billing."""

    @staticmethod
    def from_dict(data: dict) -> 'CancelBillingRequest':
        """
        Create a CancelBillingRequest instance from a dictionary.

        Args:
            data (dict): A dictionary containing the cancel billing request data.

        Returns:
            CancelBillingRequest: An instance of CancelBillingRequest.
        """
        return CancelBillingRequest(
            cancellation_reason=data.get("cancellation_reason")
        )
    
    def to_dict(self) -> dict:
        """
        Convert the CancelBillingRequest instance to a dictionary.

        Returns:
            dict: A dictionary representation of the CancelBillingRequest instance.
        """
        return {
            "motivoCancelamento": self.cancellation_reason
        }

    def to_json(self) -> str:
        """
        Convert the CancelBillingRequest instance to a JSON string.

        Returns:
            str: A JSON string representation of the CancelBillingRequest instance.
        """
        return json.dumps(self.to_dict())