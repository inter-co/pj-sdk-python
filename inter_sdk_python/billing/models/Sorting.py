from dataclasses import dataclass
from typing import Optional

from inter_sdk_python.billing.enums.OrderBy import OrderBy
from inter_sdk_python.billing.enums.OrderType import OrderType


@dataclass
class Sorting:
    """
    The Sorting class represents the sorting criteria used
    for retrieving billing data.

    It includes fields for specifying the order by which
    the results should be sorted, as well as the type of sorting
    (ascending or descending). This structure is essential for
    organizing the output of billing retrieval processes according
    to user or system preferences.
    """

    order_by: Optional[OrderBy] = None
    """The criterion by which the results should be ordered."""

    sort_type: Optional[OrderType] = None
    """The type of sorting to be applied (ascending/descending)."""

    @staticmethod
    def from_dict(data: dict) -> 'Sorting':
        """
        Create a Sorting instance from a dictionary.

        Args:
            data (dict): A dictionary containing the sorting data.

        Returns:
            Sorting: An instance of Sorting.
        """
        return Sorting(
            order_by=OrderBy(data["ordenarPor"]) if data.get("ordenarPor") else None,
            sort_type=OrderType(data["tipoOrdenacao"]) if data.get("tipoOrdenacao") else None
        )