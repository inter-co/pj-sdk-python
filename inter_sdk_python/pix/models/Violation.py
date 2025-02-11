from dataclasses import dataclass
from typing import Optional

@dataclass
class Violation:
    """
    The Violation class represents a violation related to a
    financial transaction or business rule. It includes details such
    as the reason for the violation, the specific property affected,
    and the value associated with the violation.
    """

    reason: Optional[str] = None
    """The reason for the violation."""

    property: Optional[str] = None
    """The specific property affected by the violation."""

    value: Optional[str] = None
    """The value associated with the violation."""

    @staticmethod
    def from_dict(data: dict) -> 'Violation':
        """
        Create a Violation instance from a dictionary.

        Args:
            data (dict): A dictionary containing the Violation data.

        Returns:
            Violation: An instance of Violation.
        """
        return Violation(
            reason=data.get("razao"),
            property=data.get("propriedade"),
            value=data.get("valor")
        )

    def to_dict(self) -> dict:
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