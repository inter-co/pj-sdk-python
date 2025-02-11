from enum import Enum

class DevolutionNature(Enum):
    """
    The DevolutionNature enum represents the nature of a PIX devolution.

    ORIGINAL: Original devolution (return of the original transaction)
    RETIRADA: Withdrawal (cancellation or reversal of a transaction)
    """

    ORIGINAL = "ORIGINAL"
    RETIRADA = "RETIRADA"

    @classmethod
    def from_string(cls, value: str) -> 'DevolutionNature':
        """
        Create a DevolutionNature instance from a string value.

        Args:
            value (str): The string representation of the DevolutionNature.

        Returns:
            DevolutionNature: The corresponding DevolutionNature enum value.

        Raises:
            ValueError: If the input string doesn't match any DevolutionNature value.
        """
        try:
            return cls(value.upper())
        except ValueError:
            raise ValueError(f"'{value}' is not a valid DevolutionNature value")