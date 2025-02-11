from enum import Enum

class ImmediateBillingType(Enum):
    """
    The ImmediateBillingType enum represents the types of immediate PIX billing.

    cob: Cobrança imediata (Immediate billing)
    cobv: Cobrança com vencimento (Billing with due date)
    """

    cob = "cob"
    cobv = "cobv"

    @classmethod
    def from_string(cls, value: str) -> 'ImmediateBillingType':
        """
        Create an ImmediateBillingType instance from a string value.

        Args:
            value (str): The string representation of the ImmediateBillingType.

        Returns:
            ImmediateBillingType: The corresponding ImmediateBillingType enum value.

        Raises:
            ValueError: If the input string doesn't match any ImmediateBillingType value.
        """
        try:
            return cls(value.lower())
        except ValueError:
            raise ValueError(f"'{value}' is not a valid ImmediateBillingType value")