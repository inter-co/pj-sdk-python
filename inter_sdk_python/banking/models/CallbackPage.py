from dataclasses import dataclass
from typing import List, Optional, Dict

from inter_sdk_python.banking.models.RetrieveCallbackResponse import RetrieveCallbackResponse


@dataclass
class CallbackPage:
    """
    The CallbackPage class represents a paginated response for callback data,
    including pagination information and the list of responses.
    """

    total_pages: Optional[int] = None
    """The total number of pages available."""

    total_elements: Optional[int] = None
    """The total number of elements in the response."""

    last_page: Optional[bool] = None
    """Indicates if this is the last page of results."""

    first_page: Optional[bool] = None
    """Indicates if this is the first page of results."""

    page_size: Optional[int] = None
    """The size of each page (number of elements per page)."""

    number_of_elements: Optional[int] = None
    """The number of elements in the current page."""

    data: Optional[List[RetrieveCallbackResponse]] = None
    """A list of callback responses for the current page."""

    @property
    def number_of_pages(self) -> int:
        """
        Calculate the number of pages.

        Returns:
            int: The number of pages, or 0 if not specified.
        """
        return self.total_pages if self.total_pages is not None else 0

    @staticmethod
    def from_dict(data: Dict) -> 'CallbackPage':
        """
        Create a CallbackPage instance from a dictionary.

        Args:
            data (dict): A dictionary containing the callback page data.

        Returns:
            CallbackPage: An instance of CallbackPage.
        """
        return CallbackPage(
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
        Convert the CallbackPage instance to a dictionary.

        Returns:
            dict: A dictionary representation of the CallbackPage instance.
        """
        return {
            "totalPaginas": self.total_pages,
            "totalElementos": self.total_elements,
            "ultimaPagina": self.last_page,
            "primeiraPagina": self.first_page,
            "tamanhoPagina": self.page_size,
            "numeroDeElementos": self.number_of_elements,
            "data": [response.to_dict() for response in self.data] if self.data else []
        }