from dataclasses import dataclass
from typing import Dict

from inter_sdk_python.banking.enums.OperationType import OperationType
from inter_sdk_python.banking.enums.TransactionType import TransactionType


@dataclass
class FilterRetrieveEnrichedStatement:
    """
    The FilterRetrieveEnrichedStatement class represents the filters used to retrieve
    enriched bank statements based on operation and transaction types.
    """

    operation_type: str = None
    """The type of operation filter for enriched statements."""

    transaction_type: str = None
    """The type of transaction filter for enriched statements."""

    @staticmethod
    def from_dict(data: Dict) -> 'FilterRetrieveEnrichedStatement':
        """
        Create a FilterRetrieveEnrichedStatement instance from a dictionary.

        Args:
            data (dict): A dictionary containing the filter data.

        Returns:
            FilterRetrieveEnrichedStatement: An instance of FilterRetrieveEnrichedStatement.
        """
        return FilterRetrieveEnrichedStatement(
            operation_type=OperationType(data["operationType"]).name if "operationType" in data else None,
            transaction_type=TransactionType(data["transactionType"]).name if "transactionType" in data else None
        )

    def to_dict(self) -> dict:
        """
        Convert the FilterRetrieveEnrichedStatement instance to a dictionary.

        Returns:
            dict: A dictionary representation of the FilterRetrieveEnrichedStatement instance.
        """
        return {
            "operationType": self.operation_type if self.operation_type else None,
            "transactionType": self.transaction_type if self.transaction_type else None
        }