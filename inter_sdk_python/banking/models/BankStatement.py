from dataclasses import dataclass
from typing import List, Optional, Dict

from inter_sdk_python.banking.models.Transaction import Transaction


@dataclass
class BankStatement:
    """
    The BankStatement class represents a summary of transactions 
    for a specified bank account within a certain period.
    """

    transactions: Optional[List[Transaction]] = None
    """A list of transactions included in the bank statement."""

    @staticmethod
    def from_dict(data: Dict) -> 'BankStatement':
        """
        Create a BankStatement instance from a dictionary.

        Args:
            data (dict): A dictionary containing the bank statement data.

        Returns:
            BankStatement: An instance of BankStatement.
        """
        return BankStatement(
            transactions=[Transaction.from_dict(item) for item in data.get("transacoes", [])]
        )

    def to_dict(self) -> dict:
        """
        Convert the BankStatement instance to a dictionary.

        Returns:
            dict: A dictionary representation of the BankStatement instance.
        """
        return {
            "transacoes": [transaction.to_dict() for transaction in self.transactions] if self.transactions else []
        }