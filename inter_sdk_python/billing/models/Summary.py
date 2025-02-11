from typing import List

from inter_sdk_python.billing.models.SummaryItem import SummaryItem


class Summary(List[SummaryItem]):
    """
    The Summary class represents a collection of SummaryItem objects.

    This class extends the built-in List type, specifically for SummaryItem objects,
    allowing it to behave like a list while providing a clear type hint for its contents.
    """

    @staticmethod
    def from_list(data: List[dict]) -> 'Summary':
        """
        Create a Summary instance from a list of dictionaries.

        Args:
            data (List[dict]): A list of dictionaries, each containing data for a SummaryItem.

        Returns:
            Summary: An instance of Summary containing SummaryItem objects.
        """
        summary = Summary()
        for item_data in data:
            summary.append(SummaryItem.from_dict(item_data))
        return summary