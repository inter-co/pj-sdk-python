from enum import Enum

class PaymentDateType(Enum):
    """
    The PaymentDateType enum represents the different types of dates
    associated with a payment.

    INCLUSAO: Represents the inclusion date of the payment.
    PAGAMENTO: Represents the actual payment date.
    VENCIMENTO: Represents the due date of the payment.
    """

    INCLUSAO = "INCLUSAO"
    PAGAMENTO = "PAGAMENTO"
    VENCIMENTO = "VENCIMENTO"

    @classmethod
    def from_string(cls, value: str) -> 'PaymentDateType':
        """
        Create a PaymentDateType instance from a string value.

        Args:
            value (str): The string representation of the PaymentDateType.

        Returns:
            PaymentDateType: The corresponding PaymentDateType enum value.

        Raises:
            ValueError: If the input string doesn't match any PaymentDateType value.
        """
        try:
            return cls(value.upper())
        except ValueError:
            raise ValueError(f"'{value}' is not a valid PaymentDateType value")

    @property
    def description(self) -> str:
        """
        Get a human-readable description of the payment date type.

        Returns:
            str: A description of the payment date type.
        """
        descriptions = {
            PaymentDateType.INCLUSAO: "Inclusion Date",
            PaymentDateType.PAGAMENTO: "Payment Date",
            PaymentDateType.VENCIMENTO: "Due Date"
        }
        return descriptions[self]