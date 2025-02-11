from dataclasses import dataclass
from typing import Dict


@dataclass
class Violation:
    """
    The Violation class represents a violation that occurred
    during processing, providing details about the reason for the
    violation, the property involved, and the value that was
    rejected or erroneous.
    """

    reason: str
    """The reason for the violation."""

    property: str
    """The property involved in the violation."""

    value: str
    """The value that was rejected or erroneous."""

    @staticmethod
    def from_dict(data: Dict) -> 'Violation':
        """
        Create a Violation instance from a dictionary.

        Args:
            data (dict): A dictionary containing violation data.

        Returns:
            Violation: An instance of Violation.
        """
        return Violation(
            reason=data.get("razao"),
            property=data.get("propriedade"),
            value=data.get("valor")
        )

    def to_dict(self) -> Dict:
        """
        Convert the Violation instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Violation instance.
        """
        return {
            "razao": self.reason,
            "propriedade": self.property,
            "valor": self.value
        }