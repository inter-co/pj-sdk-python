from dataclasses import dataclass, field
from typing import List, Optional

from inter_sdk_python.pix.models.DetailedImmediatePixBilling import DetailedImmediatePixBilling
from inter_sdk_python.pix.models.Parameters import Parameters


@dataclass
class BillingPage:
    """
    The BillingPage class represents a paginated response
    containing detailed billing information, specifically for
    immediate PIX transactions.

    It includes parameters for pagination, a list of
    billing entries, and supports additional custom fields through
    a map. This structure is essential for organizing responses and
    providing a user-friendly way to navigate through billing data.
    """

    parameters: Optional[Parameters] = None
    """The parameters associated with the billing response."""

    billings: List[DetailedImmediatePixBilling] = field(default_factory=list)
    """A list of detailed billing entries for immediate PIX transactions."""

    @property
    def total_pages(self) -> int:
        """
        Returns the total number of pages for the billing response.

        Returns:
            int: The total number of pages, or 0 if parameters or pagination are not set.
        """
        if self.parameters is None or self.parameters.pagination is None:
            return 0
        return self.parameters.pagination.total_pages

    @staticmethod
    def from_dict(data: dict) -> 'BillingPage':
        """
        Create a BillingPage instance from a dictionary.

        Args:
            data (dict): A dictionary containing the billing page data.

        Returns:
            BillingPage: An instance of BillingPage.
        """
        return BillingPage(
            parameters=Parameters.from_dict(data["parametros"]) if data.get("parametros") else None,
            billings=[DetailedImmediatePixBilling.from_dict(item) for item in data.get("cobs", [])]
        )

    def to_dict(self) -> dict:
        """
        Convert the BillingPage instance to a dictionary.

        Returns:
            dict: A dictionary representation of the BillingPage instance.
        """
        return {
            "parametros": self.parameters.to_dict() if self.parameters else None,
            "cobs": [billing.to_dict() for billing in self.billings]
        }