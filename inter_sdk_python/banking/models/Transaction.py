from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class Transaction:
    """
    The Transaction class represents a financial transaction with
    various details such as type, value, and description.
    """

    cpmf: Optional[str] = None
    """The CPMF code associated with the transaction."""

    entry_date: Optional[str] = None
    """The date when the transaction was entered."""

    transaction_type: Optional[str] = None
    """The type of the transaction."""

    operation_type: Optional[str] = None
    """The type of operation related to the transaction."""

    value: Optional[str] = None
    """The monetary value of the transaction."""

    title: Optional[str] = None
    """The title of the transaction."""

    description: Optional[str] = None
    """A description of the transaction."""

    @staticmethod
    def from_dict(data: Dict) -> 'Transaction':
        """
        Create a Transaction instance from a dictionary.

        Args:
            data (dict): A dictionary containing transaction data.

        Returns:
            Transaction: An instance of Transaction.
        """
        return Transaction(
            cpmf=data.get("cpmf"),
            entry_date=data.get("dataEntrada"),
            transaction_type=data.get("tipoTransacao"),
            operation_type=data.get("tipoOperacao"),
            value=data.get("valor"),
            title=data.get("titulo"),
            description=data.get("descricao")
        )

    def to_dict(self) -> dict:
        """
        Convert the Transaction instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Transaction instance.
        """
        return {
            "cpmf": self.cpmf,
            "dataEntrada": self.entry_date,
            "tipoTransacao": self.transaction_type,
            "tipoOperacao": self.operation_type,
            "valor": self.value,
            "titulo": self.title,
            "descricao": self.description
        }