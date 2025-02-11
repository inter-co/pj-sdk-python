from enum import Enum

class MoraCode(Enum):
    """
    The MoraCode enum represents the different types of late payment interest
    that can be applied to a billing.

    VALORDIA: Indicates a fixed daily amount for late payment interest.
    TAXAMENSAL: Indicates a monthly rate for late payment interest.
    ISENTO: Indicates that no late payment interest is applied.
    CONTROLEDOBANCO: Indicates that the late payment interest is controlled by the bank.
    """

    VALORDIA = "VALORDIA"
    TAXAMENSAL = "TAXAMENSAL"
    ISENTO = "ISENTO"
    CONTROLEDOBANCO = "CONTROLEDOBANCO"

    @classmethod
    def from_string(cls, value: str) -> 'MoraCode':
        """
        Create a MoraCode instance from a string value.

        Args:
            value (str): The string representation of the MoraCode.

        Returns:
            MoraCode: The corresponding MoraCode enum value.

        Raises:
            ValueError: If the input string doesn't match any MoraCode.
        """
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"'{value}' is not a valid MoraCode")