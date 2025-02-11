from enum import Enum

class BillingDateType(Enum):
    """
    The BillingDateType enum represents the different types of dates
    that can be used in billing operations.

    VENCIMENTO: Represents the due date of the billing.
    EMISSAO: Represents the issue date of the billing.
    PAGAMENTO: Represents the payment date of the billing.
    """

    VENCIMENTO = "VENCIMENTO"
    EMISSAO = "EMISSAO"
    PAGAMENTO = "PAGAMENTO"

    @classmethod
    def from_string(cls, value: str) -> 'BillingDateType':
        """
        Create a BillingDateType instance from a string value.

        Args:
            value (str): The string representation of the BillingDateType.

        Returns:
            BillingDateType: The corresponding BillingDateType enum value.

        Raises:
            ValueError: If the input string doesn't match any BillingDateType.
        """
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"'{value}' is not a valid BillingDateType")