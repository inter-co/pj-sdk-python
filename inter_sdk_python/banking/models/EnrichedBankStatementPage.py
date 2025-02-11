from dataclasses import dataclass
from typing import List, Optional, Dict

from inter_sdk_python.banking.models.EnrichedTransaction import EnrichedTransaction


@dataclass
class EnrichedBankStatementPage:
    """
    The EnrichedBankStatementPage class represents a paginated response for enriched bank statements,
    including pagination details and a list of transactions.
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
    """The number of transactions in the current page."""

    transactions: Optional[List[EnrichedTransaction]] = None
    """A list of enriched transactions for the current page."""

    @staticmethod
    def from_dict(data: Dict) -> 'EnrichedBankStatementPage':
        """
        Create an EnrichedBankStatementPage instance from a dictionary.

        Args:
            data (dict): A dictionary containing the enriched bank statement page data.

        Returns:
            EnrichedBankStatementPage: An instance of EnrichedBankStatementPage.
        """
        return EnrichedBankStatementPage(
            total_pages=data.get("totalPaginas"),
            total_elements=data.get("totalElementos"),
            last_page=data.get("ultimaPagina"),
            first_page=data.get("primeiraPagina"),
            page_size=data.get("tamanhoPagina"),
            number_of_elements=data.get("numeroDeElementos"),
            transactions=[EnrichedTransaction.from_dict(item) for item in data.get("transacoes", [])]
        )

    def to_dict(self) -> dict:
        """
        Convert the EnrichedBankStatementPage instance to a dictionary.

        Returns:
            dict: A dictionary representation of the EnrichedBankStatementPage instance.
        """
        return {
            "totalPaginas": self.total_pages,
            "totalElementos": self.total_elements,
            "ultimaPagina": self.last_page,
            "primeiraPagina": self.first_page,
            "tamanhoPagina": self.page_size,
            "numeroDeElementos": self.number_of_elements,
            "transacoes": [transaction.to_dict() for transaction in self.transactions] if self.transactions else []
        }

