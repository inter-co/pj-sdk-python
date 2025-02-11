from dataclasses import dataclass

@dataclass
class Pagination:
    """
    The Pagination class represents the pagination details
    for a collection of items, including the current page, items
    per page, total number of pages, and total number of items.
    It also supports additional custom fields via a map of
    additional attributes.
    """

    current_page: int = 0
    """The current page number in the paginated response."""

    items_per_page: int = 0
    """The number of items per page in the paginated response."""

    total_pages: int = 0
    """The total number of pages available in the collection."""

    total_items: int = 0
    """The total number of items in the collection."""

    @staticmethod
    def from_dict(data: dict) -> 'Pagination':
        """
        Create a Pagination instance from a dictionary.

        Args:
            data (dict): A dictionary containing the Pagination data.

        Returns:
            Pagination: An instance of Pagination.
        """
        return Pagination(
            current_page=data.get("paginaAtual", 0),
            items_per_page=data.get("itensPorPagina", 0),
            total_pages=data.get("quantidadeDePaginas", 0),
            total_items=data.get("quantidadeTotalDeItens", 0)
        )

    def to_dict(self) -> dict:
        """
        Convert the Pagination instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Pagination instance.
        """
        return {
            "paginaAtual": self.current_page,
            "itensPorPagina": self.items_per_page,
            "quantidadeDePaginas": self.total_pages,
            "quantidadeTotalDeItens": self.total_items
        }