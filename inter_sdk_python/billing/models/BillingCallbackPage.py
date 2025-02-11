from dataclasses import dataclass, field
from typing import Optional, List, Dict

from inter_sdk_python.billing.models.BillingRetrieveCallbackResponse import BillingRetrieveCallbackResponse


@dataclass
class BillingCallbackPage:
    """
    The BillingCallbackPage class represents a paginated response 
    containing billing callback data.
    """

    total_pages: Optional[int] = None
    """The total number of pages available."""

    total_elements: Optional[int] = None
    """The total number of elements available."""

    last_page: Optional[bool] = None
    """Indicates if this is the last page of the results."""

    first_page: Optional[bool] = None
    """Indicates if this is the first page of the results."""

    page_size: Optional[int] = None
    """The size of each page (number of elements per page)."""

    number_of_elements: Optional[int] = None
    """The number of elements currently on this page."""

    callbacks: List[BillingRetrieveCallbackResponse] = field(default_factory=list)
    """A list of billing retrieve callback responses."""

    @property
    def page_number(self) -> int:
        """
        Gets the current page number based on total pages.

        Returns:
            int: The current page number or 0 if total_pages is None.
        """
        return self.total_pages if self.total_pages is not None else 0

    @staticmethod
    def from_dict(data: Dict) -> 'BillingCallbackPage':
        """
        Create a BillingCallbackPage instance from a dictionary.

        Args:
            data (dict): A dictionary containing billing callback page data.

        Returns:
            BillingCallbackPage: An instance of BillingCallbackPage.
        """
        return BillingCallbackPage(
            total_pages=data.get("totalPaginas"),
            total_elements=data.get("totalElementos"),
            last_page=data.get("ultimaPagina"),
            first_page=data.get("primeiraPagina"),
            page_size=data.get("size"),
            number_of_elements=data.get("numberOfElements"),
            callbacks=[BillingRetrieveCallbackResponse.from_dict(item) for item in data.get("data", [])]
        )

    def to_dict(self) -> dict:
        """
        Convert the BillingCallbackPage instance to a dictionary.

        Returns:
            dict: A dictionary representation of the BillingCallbackPage instance.
        """
        return {
            "totalPaginas": self.total_pages,
            "totalElementos": self.total_elements,
            "ultimaPagina": self.last_page,
            "primeiraPagina": self.first_page,
            "size": self.page_size,
            "numberOfElements": self.number_of_elements,
            "data": [callback.to_dict() for callback in self.callbacks]
        }