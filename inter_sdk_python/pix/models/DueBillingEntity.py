from dataclasses import dataclass
from typing import Optional

from inter_sdk_python.pix.models.Problem import Problem


@dataclass
class DueBillingEntity:
    """
    The DueBillingEntity class represents a single billing
    transaction within a due billing batch.

    It includes fields for the transaction ID (txid), the
    status of the transaction, any associated problem details, and
    the creation date of the transaction.
    """

    txid: Optional[str] = None
    """The transaction ID associated with the billing entity."""

    status: Optional[str] = None
    """The current status of the billing transaction."""

    problem: Optional[Problem] = None
    """The problem associated with the billing transaction."""

    creation_date: Optional[str] = None
    """The creation date of the billing transaction."""

    @staticmethod
    def from_dict(data: dict) -> 'DueBillingEntity':
        """
        Create a DueBillingEntity instance from a dictionary.

        Args:
            data (dict): A dictionary containing the DueBillingEntity data.

        Returns:
            DueBillingEntity: An instance of DueBillingEntity.
        """
        return DueBillingEntity(
            txid=data.get("txid"),
            status=data.get("status"),
            problem=Problem.from_dict(data["problema"]) if data.get("problema") else None,
            creation_date=data.get("criacao")
        )

    def to_dict(self) -> dict:
        """
        Convert the DueBillingEntity instance to a dictionary.

        Returns:
            dict: A dictionary representation of the DueBillingEntity instance.
        """
        return {
            "txid": self.txid,
            "status": self.status,
            "problema": self.problem.to_dict() if self.problem else None,
            "criacao": self.creation_date
        }