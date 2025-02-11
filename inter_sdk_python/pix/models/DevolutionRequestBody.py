from dataclasses import dataclass
from typing import Optional

from inter_sdk_python.pix.enums.DevolutionNature import DevolutionNature


@dataclass
class DevolutionRequestBody:
    """
    The DevolutionRequestBody class represents the body
    of a request for a devolution (refund) operation.

    It includes the refund amount, nature of the devolution,
    and a description to provide context for the refund request.
    """

    value: Optional[str] = None
    """The amount to be refunded."""

    nature: Optional[DevolutionNature] = None
    """The nature of the devolution."""

    description: Optional[str] = None
    """A description of the devolution request."""

    @staticmethod
    def from_dict(data: dict) -> 'DevolutionRequestBody':
        """
        Create a DevolutionRequestBody instance from a dictionary.

        Args:
            data (dict): A dictionary containing the DevolutionRequestBody data.

        Returns:
            DevolutionRequestBody: An instance of DevolutionRequestBody.
        """
        return DevolutionRequestBody(
            value=data.get("valor"),
            nature=DevolutionNature(data["natureza"]) if data.get("natureza") else None,
            description=data.get("descricao")
        )

    def to_dict(self) -> dict:
        """
        Convert the DevolutionRequestBody instance to a dictionary.

        Returns:
            dict: A dictionary representation of the DevolutionRequestBody instance.
        """
        return {
            "valor": self.value,
            "natureza": self.nature.name if self.nature else None,
            "descricao": self.description
        }