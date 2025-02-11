from enum import Enum

class AccountType(Enum):
    """
    The AccountType enum represents the different types of bank accounts.

    CONTA_CORRENTE: Represents a checking account.
    CONTA_POUPANCA: Represents a savings account.
    CONTA_SALARIO: Represents a salary account.
    CONTA_PAGAMENTO: Represents a payment account.
    """

    CONTA_CORRENTE = "CONTA_CORRENTE"
    CONTA_POUPANCA = "CONTA_POUPANCA"
    CONTA_SALARIO = "CONTA_SALARIO"
    CONTA_PAGAMENTO = "CONTA_PAGAMENTO"

    @classmethod
    def from_string(cls, value: str) -> 'AccountType':
        """
        Create an AccountType instance from a string value.

        Args:
            value (str): The string representation of the AccountType.

        Returns:
            AccountType: The corresponding AccountType enum value.

        Raises:
            ValueError: If the input string doesn't match any AccountType value.
        """
        try:
            return cls(value.upper())
        except ValueError:
            raise ValueError(f"'{value}' is not a valid AccountType value")