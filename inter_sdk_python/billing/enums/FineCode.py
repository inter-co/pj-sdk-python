from enum import Enum

class FineCode(Enum):
    """
    The FineCode enum represents the different types of fines
    that can be applied to a billing.

    NAOTEMMULTA: Indicates that no fine is applied.
    VALORFIXO: Indicates a fixed amount fine.
    PERCENTUAL: Indicates a percentage-based fine.
    """

    NAOTEMMULTA = "NAOTEMMULTA"
    VALORFIXO = "VALORFIXO"
    PERCENTUAL = "PERCENTUAL"

    @classmethod
    def from_string(cls, value: str) -> 'FineCode':
        """
        Create a FineCode instance from a string value.

        Args:
            value (str): The string representation of the FineCode.

        Returns:
            FineCode: The corresponding FineCode enum value.

        Raises:
            ValueError: If the input string doesn't match any FineCode.
        """
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"'{value}' is not a valid FineCode")