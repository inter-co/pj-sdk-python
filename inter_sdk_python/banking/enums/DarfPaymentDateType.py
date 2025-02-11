from enum import Enum

class DarfPaymentDateType(Enum):
    """
    The DarfPaymentDateType enum represents the different types of dates
    associated with a DARF (Documento de Arrecadação de Receitas Federais) payment.

    INCLUSAO: Represents the inclusion date of the DARF payment.
    PAGAMENTO: Represents the payment date of the DARF.
    VENCIMENTO: Represents the due date of the DARF.
    PERIODO_APURACAO: Represents the assessment period date of the DARF.
    """

    INCLUSAO = "INCLUSAO"
    PAGAMENTO = "PAGAMENTO"
    VENCIMENTO = "VENCIMENTO"
    PERIODO_APURACAO = "PERIODO_APURACAO"

    @classmethod
    def from_string(cls, value: str) -> 'DarfPaymentDateType':
        """
        Create a DarfPaymentDateType instance from a string value.

        Args:
            value (str): The string representation of the DarfPaymentDateType.

        Returns:
            DarfPaymentDateType: The corresponding DarfPaymentDateType enum value.

        Raises:
            ValueError: If the input string doesn't match any DarfPaymentDateType value.
        """
        try:
            return cls(value.upper())
        except ValueError:
            raise ValueError(f"'{value}' is not a valid DarfPaymentDateType value")