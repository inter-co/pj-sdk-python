from enum import Enum

class BillingType(Enum):
    """
    The BillingType enum represents the different types of billing
    that can be applied.

    SIMPLES: Represents a simple, one-time billing.
    PARCELADO: Represents a billing that is paid in installments.
    RECORRENTE: Represents a recurring billing that repeats at regular intervals.
    """

    SIMPLES = "SIMPLES"
    PARCELADO = "PARCELADO"
    RECORRENTE = "RECORRENTE"

    @classmethod
    def from_string(cls, value: str) -> 'BillingType':
        """
        Create a BillingType instance from a string value.

        Args:
            value (str): The string representation of the BillingType.

        Returns:
            BillingType: The corresponding BillingType enum value.

        Raises:
            ValueError: If the input string doesn't match any BillingType.
        """
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"'{value}' is not a valid BillingType")