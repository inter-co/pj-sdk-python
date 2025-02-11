from dataclasses import dataclass, field
from typing import Optional, List

from inter_sdk_python.billing.models.RetrievedBilling import RetrievedBilling


@dataclass
class BillingPage:
    """
    The BillingPage class represents a paginated response containing a
    collection of retrieved billings.

    It includes details about the total number of pages, total elements,
    and information indicating whether it is the first or last page. Additionally, it
    holds a list of retrieved billing information. This structure supports pagination
    in the billing retrieval processes.
    """

    total_pages: Optional[int] = None
    """The total number of pages available."""

    total_elements: Optional[int] = None
    """The total number of elements (billings) available."""

    last_page: Optional[bool] = None
    """Indicates whether this is the last page of results."""

    first_page: Optional[bool] = None
    """Indicates whether this is the first page of results."""

    page_size: Optional[int] = None
    """The size of the page, indicating how many elements are displayed per page."""

    number_of_elements: Optional[int] = None
    """The number of elements on the current page."""

    billings: List[RetrievedBilling] = field(default_factory=list)
    """A list of retrieved billing information."""

    @property
    def page_number(self) -> int:
        """Returns the quantity of pages available."""
        return self.total_pages if self.total_pages is not None else 0

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
            total_pages=data.get("totalPaginas"),
            total_elements=data.get("totalElementos"),
            last_page=data.get("ultimaPagina"),
            first_page=data.get("primeiraPagina"),
            page_size=data.get("tamanhoPagina"),
            number_of_elements=data.get("numeroDeElementos"),
            billings=[RetrievedBilling.from_dict(item) for item in data.get("cobrancas", [])]
        )

    def to_dict(self) -> dict:
        """
        Convert the BillingPage instance to a dictionary.

        Returns:
            dict: A dictionary containing the billing page data.
        """
        return {
            "totalPaginas": self.total_pages,
            "totalElementos": self.total_elements,
            "ultimaPagina": self.last_page,
            "primeiraPagina": self.first_page,
            "tamanhoPagina": self.page_size,
            "numeroDeElementos": self.number_of_elements,
            "cobrancas": [billing.to_dict() for billing in self.billings]
        }