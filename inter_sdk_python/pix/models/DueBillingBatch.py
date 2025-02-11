from dataclasses import dataclass, field
from typing import Optional, List

from inter_sdk_python.pix.models.DueBillingEntity import DueBillingEntity


@dataclass
class DueBillingBatch:
    """
    The DueBillingBatch class represents a batch of due billing
    transactions.

    It includes fields for the batch ID, a description of the batch,
    the creation date, and a list of individual due billing entities
    associated with this batch.
    """

    id: Optional[str] = None
    """The unique identifier for the billing batch."""

    description: Optional[str] = None
    """A description of the billing batch."""

    creation_date: Optional[str] = None
    """The creation date of the billing batch."""

    due_billing_entities: List[DueBillingEntity] = field(default_factory=list)
    """A list of due billing entities within the batch."""

    @staticmethod
    def from_dict(data: dict) -> 'DueBillingBatch':
        """
        Create a DueBillingBatch instance from a dictionary.

        Args:
            data (dict): A dictionary containing the DueBillingBatch data.

        Returns:
            DueBillingBatch: An instance of DueBillingBatch.
        """
        return DueBillingBatch(
            id=data.get("id"),
            description=data.get("descricao"),
            creation_date=data.get("criacao"),
            due_billing_entities=[DueBillingEntity.from_dict(entity) for entity in data.get("cobsv", [])]
        )

    def to_dict(self) -> dict:
        """
        Convert the DueBillingBatch instance to a dictionary.

        Returns:
            dict: A dictionary representation of the DueBillingBatch instance.
        """
        return {
            "id": self.id,
            "descricao": self.description,
            "criacao": self.creation_date,
            "cobsv": [entity.to_dict() for entity in self.due_billing_entities]
        }