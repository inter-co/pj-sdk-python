import json
from dataclasses import dataclass, field
from typing import Optional, List

from inter_sdk_python.pix.models.DueBilling import DueBilling


@dataclass
class IncludeDueBillingBatchRequest:
    """
    The IncludeDueBillingBatchRequest class represents a request
    to include a batch of due billings.

    It consists of a description for the batch and a list
    of due billings to be included in the request.
    """

    description: Optional[str] = None
    """A description for the batch of due billings."""

    due_billings: List[DueBilling] = field(default_factory=list)
    """A list of due billings to be included in the batch request."""

    @staticmethod
    def from_dict(data: dict) -> 'IncludeDueBillingBatchRequest':
        """
        Create an IncludeDueBillingBatchRequest instance from a dictionary.

        Args:
            data (dict): A dictionary containing the IncludeDueBillingBatchRequest data.

        Returns:
            IncludeDueBillingBatchRequest: An instance of IncludeDueBillingBatchRequest.
        """
        return IncludeDueBillingBatchRequest(
            description=data.get("descricao"),
            due_billings=[DueBilling.from_dict(billing) for billing in data.get("cobsv", [])]
        )

    def to_dict(self) -> dict:
        """
        Convert the IncludeDueBillingBatchRequest instance to a dictionary.

        Returns:
            dict: A dictionary representation of the IncludeDueBillingBatchRequest instance.
        """
        return {
            "descricao": self.description,
            "cobsv": [billing.to_dict() for billing in self.due_billings]
        }
    
    def to_json(self) -> str:
        """
        Convert the IncludeDueBillingBatchRequest instance to a JSON string.
        Returns:
            str: A JSON string representation of the IncludeDueBillingBatchRequest instance.
        """
        return json.dumps(self.to_dict(), ensure_ascii=False)