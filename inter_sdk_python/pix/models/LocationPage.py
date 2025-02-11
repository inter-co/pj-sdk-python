from dataclasses import dataclass, field
from typing import Optional, List

from inter_sdk_python.pix.models.Location import Location
from inter_sdk_python.pix.models.Parameters import Parameters


@dataclass
class LocationPage:
    """
    The LocationPage class represents a paginated response
    containing a list of locations. It includes parameters for
    pagination, a list of locations, and supports additional
    custom fields through a map.
    """

    parameters: Optional[Parameters] = None
    """Parameters related to the response."""

    locations: List[Location] = field(default_factory=list)
    """A list of locations included in the response."""

    @property
    def total_pages(self) -> int:
        """
        Returns the total number of pages for the locations response.

        Returns:
            int: The total number of pages, or 0 if parameters or pagination
                 details are not available.
        """
        if self.parameters is None or self.parameters.pagination is None:
            return 0
        return self.parameters.pagination.total_pages

    @staticmethod
    def from_dict(data: dict) -> 'LocationPage':
        """
        Create a LocationPage instance from a dictionary.

        Args:
            data (dict): A dictionary containing the LocationPage data.

        Returns:
            LocationPage: An instance of LocationPage.
        """
        return LocationPage(
            parameters=Parameters.from_dict(data["parametros"]) if data.get("parametros") else None,
            locations=[Location.from_dict(loc) for loc in data.get("loc", [])]
        )

    def to_dict(self) -> dict:
        """
        Convert the LocationPage instance to a dictionary.

        Returns:
            dict: A dictionary representation of the LocationPage instance.
        """
        return {
            "parametros": self.parameters.to_dict() if self.parameters else None,
            "loc": [loc.to_dict() for loc in self.locations]
        }