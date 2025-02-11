from enum import Enum

class ReceivingOrigin(Enum):
    """
    The ReceivingOrigin enum represents the different methods
    through which a payment can be received.

    BOLETO: Represents payment received through a bank slip (boleto).
    PIX: Represents payment received through the PIX instant payment system.
    """

    BOLETO = "BOLETO"
    PIX = "PIX"

    @classmethod
    def from_string(cls, value: str) -> 'ReceivingOrigin':
        """
        Create a ReceivingOrigin instance from a string value.

        Args:
            value (str): The string representation of the ReceivingOrigin.

        Returns:
            ReceivingOrigin: The corresponding ReceivingOrigin enum value.

        Raises:
            ValueError: If the input string doesn't match any ReceivingOrigin value.
        """
        try:
            return cls(value.upper())
        except ValueError:
            raise ValueError(f"'{value}' is not a valid ReceivingOrigin value")