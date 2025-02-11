from dataclasses import dataclass, field
from typing import Optional, List

from inter_sdk_python.pix.models.RetrieveCallbackResponse import RetrieveCallbackResponse


@dataclass
class PixCallbackPage:
    """
    The PixCallbackPage class represents a paginated response
    of callbacks, containing information about the total number
    of pages, total elements, flags indicating if it's the
    first or last page, page size and number of elements in the
    current page, along with the actual list of callback responses.

    This structure is essential for managing and navigating
    through large sets of callback data effectively.
    """

    total_pages: Optional[int] = None
    """The total number of pages available for callback responses."""

    total_elements: Optional[int] = None
    """The total number of elements across all pages."""

    last_page: Optional[bool] = None
    """A flag indicating if the current page is the last one."""

    first_page: Optional[bool] = None
    """A flag indicating if the current page is the first one."""

    page_size: Optional[int] = None
    """The size of each page in terms of the number of elements."""

    number_of_elements: Optional[int] = None
    """The number of elements present on the current page."""

    data: List[RetrieveCallbackResponse] = field(default_factory=list)
    """The actual list of callback responses for the current page."""

    @property
    def page_number(self) -> int:
        """
        Returns the total number of pages for the callback response.

        Returns:
            int: The total number of pages or 0 if no pages are specified.
        """
        return self.total_pages if self.total_pages is not None else 0

    @staticmethod
    def from_dict(data: dict) -> 'PixCallbackPage':
        """
        Create a PixCallbackPage instance from a dictionary.

        Args:
            data (dict): A dictionary containing the PixCallbackPage data.

        Returns:
            PixCallbackPage: An instance of PixCallbackPage.
        """
        return PixCallbackPage(
            total_pages=data.get("totalPaginas"),
            total_elements=data.get("totalElementos"),
            last_page=data.get("ultimaPagina"),
            first_page=data.get("primeiraPagina"),
            page_size=data.get("tamanhoPagina"),
            number_of_elements=data.get("numeroDeElementos"),
            data=[RetrieveCallbackResponse.from_dict(item) for item in data.get("data", [])] if data.get("data") else None
        )

    def to_dict(self) -> dict:
        """
        Convert the PixCallbackPage instance to a dictionary.

        Returns:
            dict: A dictionary representation of the PixCallbackPage instance.
        """
        return {
            "totalPaginas": self.total_pages,
            "totalElementos": self.total_elements,
            "ultimaPagina": self.last_page,
            "primeiraPagina": self.first_page,
            "tamanhoPagina": self.page_size,
            "numeroDeElementos": self.number_of_elements,
            "data": [item.to_dict() for item in self.data]
        }