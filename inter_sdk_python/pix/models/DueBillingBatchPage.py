from dataclasses import dataclass, field
from typing import Optional, List

from inter_sdk_python.pix.models.DueBillingBatch import DueBillingBatch
from inter_sdk_python.pix.models.Parameters import Parameters


@dataclass
class DueBillingBatchPage:
    """
    The DueBillingBatchPage class represents a paginated
    response for due billing batches.

    It includes fields for request parameters and
    a list of batches, allowing for easy access to pagination
    information and additional dynamic fields.
    """

    parameters: Optional[Parameters] = None
    """The parameters associated with the request."""

    batches: List[DueBillingBatch] = field(default_factory=list)
    """A list of due billing batches in this page response."""

    @property
    def total_pages(self) -> int:
        """
        Returns the total number of pages for the billing due response.

        Returns:
            int: The total number of pages, or 0 if parameters or pagination
                 details are not available.
        """
        if self.parameters is None or self.parameters.pagination is None:
            return 0
        return self.parameters.pagination.total_pages

    @staticmethod
    def from_dict(data: dict) -> 'DueBillingBatchPage':
        """
        Create a DueBillingBatchPage instance from a dictionary.

        Args:
            data (dict): A dictionary containing the DueBillingBatchPage data.

        Returns:
            DueBillingBatchPage: An instance of DueBillingBatchPage.
        """
        return DueBillingBatchPage(
            parameters=Parameters.from_dict(data["parametros"]) if data.get("parametros") else None,
            batches=[DueBillingBatch.from_dict(batch) for batch in data.get("lotes", [])]
        )

    def to_dict(self) -> dict:
        """
        Convert the DueBillingBatchPage instance to a dictionary.

        Returns:
            dict: A dictionary representation of the DueBillingBatchPage instance.
        """
        return {
            "parametros": self.parameters.to_dict() if self.parameters else None,
            "lotes": [batch.to_dict() for batch in self.batches]
        }