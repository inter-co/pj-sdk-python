from dataclasses import dataclass, field
from typing import Optional, List

from inter_sdk_python.pix.models.DetailedDuePixBilling import DetailedDuePixBilling
from inter_sdk_python.pix.models.Parameters import Parameters


@dataclass
class DueBillingPage:
    """
    The DueBillingPage class represents a paginated response
    containing detailed billing information that is due for payment.
    
    It includes parameters for pagination, a list of detailed
    due billings, and supports additional custom fields through a map.
    """

    parameters: Optional[Parameters] = None
    """The parameters associated with the request for due billings."""

    due_billings: List[DetailedDuePixBilling] = field(default_factory=list)
    """A list of detailed due billings in this page response."""

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
    def from_dict(data: dict) -> 'DueBillingPage':
        """
        Create a DueBillingPage instance from a dictionary.

        Args:
            data (dict): A dictionary containing the DueBillingPage data.

        Returns:
            DueBillingPage: An instance of DueBillingPage.
        """
        return DueBillingPage(
            parameters=Parameters.from_dict(data["parametros"]) if data.get("parametros") else None,
            due_billings=[DetailedDuePixBilling.from_dict(billing) for billing in data.get("cobs", [])]
        )

    def to_dict(self) -> dict:
        """
        Convert the DueBillingPage instance to a dictionary.

        Returns:
            dict: A dictionary representation of the DueBillingPage instance.
        """
        return {
            "parametros": self.parameters.to_dict() if self.parameters else None,
            "cobs": [billing.to_dict() for billing in self.due_billings]
        }