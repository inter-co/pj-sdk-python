from dataclasses import dataclass
from typing import Optional

from inter_sdk_python.pix.models.Change import Change
from inter_sdk_python.pix.models.Withdrawal import Withdrawal


@dataclass
class WithdrawalTransaction:
    """
    The WithdrawalTransaction class represents details of a
    withdrawal operation. It includes fields for the withdrawal
    details (Withdrawal) and any change returned (Change).
    """

    withdrawal: Optional[Withdrawal] = None
    """The details of the withdrawal operation."""

    change: Optional[Change] = None
    """The change returned during the withdrawal."""

    @staticmethod
    def from_dict(data: dict) -> 'WithdrawalTransaction':
        """
        Create a WithdrawalTransaction instance from a dictionary.

        Args:
            data (dict): A dictionary containing the WithdrawalTransaction data.

        Returns:
            WithdrawalTransaction: An instance of WithdrawalTransaction.
        """
        return WithdrawalTransaction(
            withdrawal=Withdrawal.from_dict(data["saque"]) if data.get("saque") else None,
            change=Change.from_dict(data["troco"]) if data.get("troco") else None,
        )

    def to_dict(self) -> dict:
        """
        Convert the WithdrawalTransaction instance to a dictionary.

        Returns:
            dict: A dictionary representation of the WithdrawalTransaction instance.
        """
        return {
            "saque": self.withdrawal.to_dict() if self.withdrawal else None,
            "troco": self.change.to_dict() if self.change else None,
        }