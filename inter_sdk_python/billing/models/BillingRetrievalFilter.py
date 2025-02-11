from dataclasses import dataclass, field

from inter_sdk_python.billing.models.BaseBillingRetrievalFilter import BaseBillingRetrievalFilter


@dataclass
class BillingRetrievalFilter(BaseBillingRetrievalFilter):
    """
    The BillingRetrievalFilter class extends the base filter
    class for retrieving billing information.

    It includes pagination details, specifically the page
    number and the number of items per page. This structure is used
    to specify filtering criteria when retrieving billing data from a
    paginated source.
    """

    page: int = field(default=0)
    """The current page number for pagination."""

    items_per_page: int = field(default=0)
    """The number of items to display per page."""

    @staticmethod
    def from_dict(data: dict) -> 'BillingRetrievalFilter':
        """
        Create a BillingRetrievalFilter instance from a dictionary.

        Args:
            data (dict): A dictionary containing the billing retrieval filter data.

        Returns:
            BillingRetrievalFilter: An instance of BillingRetrievalFilter.
        """
        base_filter = BaseBillingRetrievalFilter.from_dict(data)
        return BillingRetrievalFilter(
            **base_filter.__dict__,
            page=data.get("pagina", 0),
            items_per_page=data.get("itensPorPagina", 0)
        )