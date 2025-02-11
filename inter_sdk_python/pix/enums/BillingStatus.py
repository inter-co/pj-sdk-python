from enum import Enum

class BillingStatus(Enum):
    """
    The BillingStatus enum represents the different statuses a PIX billing can have.

    ATIVA: Active billing
    CONCLUIDA: Completed billing
    REMOVIDO_PELO_USUARIO_RECEBEDOR: Removed by the receiving user
    REMOVIDO_PELO_PSP: Removed by the Payment Service Provider (PSP)
    """

    ATIVA = "ATIVA"
    CONCLUIDA = "CONCLUIDA"
    REMOVIDO_PELO_USUARIO_RECEBEDOR = "REMOVIDO_PELO_USUARIO_RECEBEDOR"
    REMOVIDO_PELO_PSP = "REMOVIDO_PELO_PSP"

    @classmethod
    def from_string(cls, value: str) -> 'BillingStatus':
        """
        Create a BillingStatus instance from a string value.

        Args:
            value (str): The string representation of the BillingStatus.

        Returns:
            BillingStatus: The corresponding BillingStatus enum value.

        Raises:
            ValueError: If the input string doesn't match any BillingStatus value.
        """
        try:
            return cls(value.upper())
        except ValueError:
            raise ValueError(f"'{value}' is not a valid BillingStatus value")