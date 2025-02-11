from enum import Enum

class OperationType(Enum):
    """
    The OperationType enum represents the types of financial operations.

    D: Represents a debit operation.
    C: Represents a credit operation.
    """

    D = "D"
    C = "C"

    @classmethod
    def from_string(cls, value: str) -> 'OperationType':
        """
        Create an OperationType instance from a string value.

        Args:
            value (str): The string representation of the OperationType.

        Returns:
            OperationType: The corresponding OperationType enum value.

        Raises:
            ValueError: If the input string doesn't match any OperationType value.
        """
        try:
            return cls(value.upper())
        except ValueError:
            raise ValueError(f"'{value}' is not a valid OperationType value")

    @property
    def description(self) -> str:
        """
        Get a human-readable description of the operation type.

        Returns:
            str: A description of the operation type.
        """
        return "Debit" if self == OperationType.D else "Credit"