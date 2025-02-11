from enum import Enum

class TransactionType(Enum):
    """
    The TransactionType enum represents the various types of financial transactions.

    PIX: PIX instant payment
    CAMBIO: Foreign exchange
    ESTORNO: Refund or chargeback
    INVESTIMENTO: Investment
    TRANSFERENCIA: Transfer
    PAGAMENTO: Payment
    BOLETO_COBRANCA: Payment slip (boleto)
    OUTROS: Other types of transactions
    """

    PIX = "PIX"
    CAMBIO = "CAMBIO"
    ESTORNO = "ESTORNO"
    INVESTIMENTO = "INVESTIMENTO"
    TRANSFERENCIA = "TRANSFERENCIA"
    PAGAMENTO = "PAGAMENTO"
    BOLETO_COBRANCA = "BOLETO_COBRANCA"
    OUTROS = "OUTROS"

    @classmethod
    def from_string(cls, value: str) -> 'TransactionType':
        """
        Create a TransactionType instance from a string value.

        Args:
            value (str): The string representation of the TransactionType.

        Returns:
            TransactionType: The corresponding TransactionType enum value.

        Raises:
            ValueError: If the input string doesn't match any TransactionType value.
        """
        try:
            return cls(value.upper())
        except ValueError:
            raise ValueError(f"'{value}' is not a valid TransactionType value")

    @property
    def description(self) -> str:
        """
        Get a human-readable description of the transaction type.

        Returns:
            str: A description of the transaction type.
        """
        descriptions = {
            TransactionType.PIX: "PIX Instant Payment",
            TransactionType.CAMBIO: "Foreign Exchange",
            TransactionType.ESTORNO: "Refund/Chargeback",
            TransactionType.INVESTIMENTO: "Investment",
            TransactionType.TRANSFERENCIA: "Transfer",
            TransactionType.PAGAMENTO: "Payment",
            TransactionType.BOLETO_COBRANCA: "Payment Slip (Boleto)",
            TransactionType.OUTROS: "Other"
        }
        return descriptions[self]