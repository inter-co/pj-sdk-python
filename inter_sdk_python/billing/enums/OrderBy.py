from enum import Enum

class OrderBy(Enum):
    """
    The OrderBy enum represents the different fields by which
    billing data can be ordered.

    PESSOA_PAGADORA: Order by the payer.
    TIPO_COBRANCA: Order by the type of billing.
    CODIGO_COBRANCA: Order by the billing code.
    IDENTIFICADOR: Order by the identifier.
    DATA_EMISSAO: Order by the issue date.
    DATA_VENCIMENTO: Order by the due date.
    VALOR: Order by the amount.
    STATUS: Order by the status.
    """

    PESSOA_PAGADORA = "PESSOA_PAGADORA"
    TIPO_COBRANCA = "TIPO_COBRANCA"
    CODIGO_COBRANCA = "CODIGO_COBRANCA"
    IDENTIFICADOR = "IDENTIFICADOR"
    DATA_EMISSAO = "DATA_EMISSAO"
    DATA_VENCIMENTO = "DATA_VENCIMENTO"
    VALOR = "VALOR"
    STATUS = "STATUS"

    @classmethod
    def from_string(cls, value: str) -> 'OrderBy':
        """
        Create an OrderBy instance from a string value.

        Args:
            value (str): The string representation of the OrderBy.

        Returns:
            OrderBy: The corresponding OrderBy enum value.

        Raises:
            ValueError: If the input string doesn't match any OrderBy value.
        """
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"'{value}' is not a valid OrderBy value")