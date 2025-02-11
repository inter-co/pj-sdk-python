from dataclasses import dataclass
from typing import Optional

from inter_sdk_python.pix.models.WithdrawalTransaction import WithdrawalTransaction


@dataclass
class PixValue:
    """
    The PixValue class represents the amount involved in a
    transaction. It includes the original value, modification modality,
    and withdrawal transaction details.
    """

    original: Optional[str] = None
    """The original value of the transaction."""

    modification_modality: Optional[int] = None
    """The modality of modification applied to the transaction's value."""

    withdrawal_transaction: Optional[WithdrawalTransaction] = None
    """Details of the withdrawal transaction, if applicable."""

    @staticmethod
    def from_dict(data: dict) -> 'PixValue':
        """
        Create a PixValue instance from a dictionary.

        Args:
            data (dict): A dictionary containing the PixValue data.

        Returns:
            PixValue: An instance of PixValue.
        """
        return PixValue(
            original=data.get("original"),
            modification_modality=data.get("modalidadeAlteracao"),
            withdrawal_transaction=WithdrawalTransaction.from_dict(data["retirada"]) if data.get("retirada") else None
        )

    def to_dict(self) -> dict:
        """
        Convert the PixValue instance to a dictionary.

        Returns:
            dict: A dictionary representation of the PixValue instance.
        """
        return {
            "original": self.original,
            "modalidadeAlteracao": self.modification_modality,
            "retirada": self.withdrawal_transaction.to_dict() if self.withdrawal_transaction else None
        }