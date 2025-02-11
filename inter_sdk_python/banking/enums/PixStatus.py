from enum import Enum

class PixStatus(Enum):
    """
    The PixStatus enum represents the various states a PIX transaction can be in.

    CRIADO: Created
    AGUARDANDO_APROVACAO: Awaiting approval
    APROVADO: Approved
    REPROVADO: Rejected
    EXPIRADO: Expired
    CANCELADO: Cancelled
    FALHA: Failed
    AGENDADO: Scheduled
    PAGO: Paid
    ENVIADO: Sent
    CANCELADO_SEM_SALDO: Cancelled due to insufficient balance
    DEBITADO: Debited
    PARCIALMENTE_DEBITADO: Partially debited
    PARCIALMENTE_PAGO: Partially paid
    NAO_DEBITADO: Not debited
    AGENDAMENTO_CANCELADO: Scheduled payment cancelled
    TRANSACAO_CRIADA: Transaction created
    TRANSACAO_APROVADA: Transaction approved
    PIX_ENVIADO: PIX sent
    PIX_PAGO: PIX paid
    """

    CRIADO = "CRIADO"
    AGUARDANDO_APROVACAO = "AGUARDANDO_APROVACAO"
    APROVADO = "APROVADO"
    REPROVADO = "REPROVADO"
    EXPIRADO = "EXPIRADO"
    CANCELADO = "CANCELADO"
    FALHA = "FALHA"
    AGENDADO = "AGENDADO"
    PAGO = "PAGO"
    ENVIADO = "ENVIADO"
    CANCELADO_SEM_SALDO = "CANCELADO_SEM_SALDO"
    DEBITADO = "DEBITADO"
    PARCIALMENTE_DEBITADO = "PARCIALMENTE_DEBITADO"
    PARCIALMENTE_PAGO = "PARCIALMENTE_PAGO"
    NAO_DEBITADO = "NAO_DEBITADO"
    AGENDAMENTO_CANCELADO = "AGENDAMENTO_CANCELADO"
    TRANSACAO_CRIADA = "TRANSACAO_CRIADA"
    TRANSACAO_APROVADA = "TRANSACAO_APROVADA"
    PIX_ENVIADO = "PIX_ENVIADO"
    PIX_PAGO = "PIX_PAGO"

    @classmethod
    def from_string(cls, value: str) -> 'PixStatus':
        """
        Create a PixStatus instance from a string value.

        Args:
            value (str): The string representation of the PixStatus.

        Returns:
            PixStatus: The corresponding PixStatus enum value.

        Raises:
            ValueError: If the input string doesn't match any PixStatus value.
        """
        try:
            return cls(value.upper())
        except ValueError:
            raise ValueError(f"'{value}' is not a valid PixStatus value")

    @property
    def description(self) -> str:
        """
        Get a human-readable description of the PIX status.

        Returns:
            str: A description of the PIX status.
        """
        descriptions = {
            PixStatus.CRIADO: "Created",
            PixStatus.AGUARDANDO_APROVACAO: "Awaiting Approval",
            PixStatus.APROVADO: "Approved",
            PixStatus.REPROVADO: "Rejected",
            PixStatus.EXPIRADO: "Expired",
            PixStatus.CANCELADO: "Cancelled",
            PixStatus.FALHA: "Failed",
            PixStatus.AGENDADO: "Scheduled",
            PixStatus.PAGO: "Paid",
            PixStatus.ENVIADO: "Sent",
            PixStatus.CANCELADO_SEM_SALDO: "Cancelled due to Insufficient Balance",
            PixStatus.DEBITADO: "Debited",
            PixStatus.PARCIALMENTE_DEBITADO: "Partially Debited",
            PixStatus.PARCIALMENTE_PAGO: "Partially Paid",
            PixStatus.NAO_DEBITADO: "Not Debited",
            PixStatus.AGENDAMENTO_CANCELADO: "Scheduled Payment Cancelled",
            PixStatus.TRANSACAO_CRIADA: "Transaction Created",
            PixStatus.TRANSACAO_APROVADA: "Transaction Approved",
            PixStatus.PIX_ENVIADO: "PIX Sent",
            PixStatus.PIX_PAGO: "PIX Paid"
        }
        return descriptions[self]