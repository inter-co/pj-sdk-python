from dataclasses import dataclass, field
from typing import List

from inter_sdk_python.pix.models.ItemPayload import ItemPayload


@dataclass
class PixPayload:
    """
    The PixPayload class represents a container for a list of
    transaction items related to PIX (Payment Instantâneo).
    It holds multiple item payloads.
    """

    pix_items: List[ItemPayload] = field(default_factory=list)
    """A list of transaction items related to PIX."""

    @staticmethod
    def from_dict(data: dict) -> 'PixPayload':
        """
        Create a PixPayload instance from a dictionary.

        Args:
            data (dict): A dictionary containing the PixPayload data.

        Returns:
            PixPayload: An instance of PixPayload.
        """
        return PixPayload(
            pix_items=[ItemPayload.from_dict(item) for item in data]
        )

    def to_dict(self) -> dict:
        """
        Convert the PixPayload instance to a dictionary.

        Returns:
            dict: A dictionary representation of the PixPayload instance.
        """
        return {
            "pix": [item.to_dict() for item in self.pix_items]
        }