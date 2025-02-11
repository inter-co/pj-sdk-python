from enum import Enum

class BillingSituation(Enum):
    """
    The BillingSituation enum represents the different states or situations
    that a billing can be in.

    RECEBIDO: The payment has been received.
    A_RECEBER: The payment is pending and expected to be received.
    MARCADO_RECEBIDO: The payment has been marked as received.
    ATRASADO: The payment is overdue.
    CANCELADO: The billing has been canceled.
    EXPIRADO: The billing has expired.
    FALHA_EMISSAO: There was a failure in issuing the billing.
    EM_PROCESSAMENTO: The billing is currently being processed.
    PROTESTO: The billing is being protested.
    """

    RECEBIDO = "RECEBIDO"
    A_RECEBER = "A_RECEBER"
    MARCADO_RECEBIDO = "MARCADO_RECEBIDO"
    ATRASADO = "ATRASADO"
    CANCELADO = "CANCELADO"
    EXPIRADO = "EXPIRADO"
    FALHA_EMISSAO = "FALHA_EMISSAO"
    EM_PROCESSAMENTO = "EM_PROCESSAMENTO"
    PROTESTO = "PROTESTO"

    @classmethod
    def from_string(cls, value: str) -> 'BillingSituation':
        """
        Create a BillingSituation instance from a string value.

        Args:
            value (str): The string representation of the BillingSituation.

        Returns:
            BillingSituation: The corresponding BillingSituation enum value.

        Raises:
            ValueError: If the input string doesn't match any BillingSituation.
        """
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"'{value}' is not a valid BillingSituation")