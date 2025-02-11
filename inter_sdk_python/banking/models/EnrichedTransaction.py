from dataclasses import dataclass
from typing import Optional, Dict

from inter_sdk_python.banking.models.EnrichedTransactionDetails import EnrichedTransactionDetails


@dataclass
class EnrichedTransaction:
    """
    The EnrichedTransaction class represents a transaction with enriched details,
    including identifiers, amounts, and more specific transaction details.
    """

    cpmf: Optional[str] = None
    """The CPMF (Contribuição Provisória sobre Movimentação Financeira) related to the transaction."""

    transaction_id: Optional[str] = None
    """The unique identifier for the transaction."""

    inclusion_date: Optional[str] = None
    """The date when the transaction was included in the system."""

    transaction_date: Optional[str] = None
    """The date when the transaction occurred."""

    transaction_type: Optional[str] = None
    """The type of the transaction (e.g., credit, debit)."""

    operation_type: Optional[str] = None
    """The type of operation associated with the transaction."""

    value: Optional[str] = None
    """The monetary value of the transaction."""

    title: Optional[str] = None
    """The title or name associated with the transaction."""

    description: Optional[str] = None
    """A description of the transaction."""

    details: Optional[EnrichedTransactionDetails] = None
    """Detailed information about the transaction."""

    @staticmethod
    def from_dict(data: Dict) -> 'EnrichedTransaction':
        """
        Create an EnrichedTransaction instance from a dictionary.

        Args:
            data (dict): A dictionary containing the enriched transaction data.

        Returns:
            EnrichedTransaction: An instance of EnrichedTransaction.
        """
        return EnrichedTransaction(
            cpmf=data.get("cpmf"),
            transaction_id=data.get("idTransacao"),
            inclusion_date=data.get("dataInclusao"),
            transaction_date=data.get("dataTransacao"),
            transaction_type=data.get("tipoTransacao"),
            operation_type=data.get("tipoOperacao"),
            value=data.get("valor"),
            title=data.get("titulo"),
            description=data.get("descricao"),
            details=EnrichedTransactionDetails.from_dict(data["detalhes"]) if data.get("detalhes") else None
        )

    def to_dict(self) -> dict:
        """
        Convert the EnrichedTransaction instance to a dictionary.

        Returns:
            dict: A dictionary representation of the EnrichedTransaction instance.
        """
        return {
            "cpmf": self.cpmf,
            "idTransacao": self.transaction_id,
            "dataInclusao": self.inclusion_date,
            "dataTransacao": self.transaction_date,
            "tipoTransacao": self.transaction_type,
            "tipoOperacao": self.operation_type,
            "valor": self.value,
            "titulo": self.title,
            "descricao": self.description,
            "detalhes": self.details.to_dict() if self.details else None
        }