from dataclasses import dataclass, field
from typing import Optional, List

from inter_sdk_python.pix.models.Parameters import Parameters
from inter_sdk_python.pix.models.Pix import Pix


@dataclass
class PixPage:
    """
    The PixPage class represents a paginated response containing
    a list of PIX transactions. It includes parameters for pagination,
    and a list of PIX entries.
    """

    parameters: Optional[Parameters] = None
    """Parameters related to the pagination and filtering of the PIX transactions."""

    pix_list: List[Pix] = field(default_factory=list)
    """A list of PIX transactions."""

    @property
    def total_pages(self) -> int:
        """
        Returns the total number of pages for the PIX response.

        Returns:
            int: The total number of pages, or 0 if parameters or pagination
                 details are not available.
        """
        if self.parameters is None or self.parameters.pagination is None:
            return 0
        return self.parameters.pagination.total_pages

    @staticmethod
    def from_dict(data: dict) -> 'PixPage':
        """
        Create a PixPage instance from a dictionary.

        Args:
            data (dict): A dictionary containing the PixPage data.

        Returns:
            PixPage: An instance of PixPage.
        """
        return PixPage(
            parameters=Parameters.from_dict(data["parametros"]) if data.get("parametros") else None,
            pix_list=[Pix.from_dict(pix) for pix in data.get("pix", [])]
        )

    def to_dict(self) -> dict:
        """
        Convert the PixPage instance to a dictionary.

        Returns:
            dict: A dictionary representation of the PixPage instance.
        """
        return {
            "parametros": self.parameters.to_dict() if self.parameters else None,
            "pix": [pix.to_dict() for pix in self.pix_list]
        }