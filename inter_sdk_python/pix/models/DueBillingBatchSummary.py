from dataclasses import dataclass
from typing import Optional

@dataclass
class DueBillingBatchSummary:
    """
    The DueBillingBatchSummary class summarizes the results
    of a billing batch processing.

    It includes fields for the creation date of the processing,
    the status of the processing, and totals for the billing transactions
    including the total number of charges, denied charges, and created
    charges in the batch.
    """

    processing_creation_date: Optional[str] = None
    """The creation date of the processing operation."""

    processing_status: Optional[str] = None
    """The status of the processing operation."""

    total_billing: Optional[int] = None
    """The total number of charges in the batch."""

    total_billing_denied: Optional[int] = None
    """The total number of denied charges."""

    total_billing_created: Optional[int] = None
    """The total number of created charges."""

    @staticmethod
    def from_dict(data: dict) -> 'DueBillingBatchSummary':
        """
        Create a DueBillingBatchSummary instance from a dictionary.

        Args:
            data (dict): A dictionary containing the DueBillingBatchSummary data.

        Returns:
            DueBillingBatchSummary: An instance of DueBillingBatchSummary.
        """
        return DueBillingBatchSummary(
            processing_creation_date=data.get("dataCriacaoProcessamento"),
            processing_status=data.get("statusProcessamento"),
            total_billing=data.get("totalCobrancas"),
            total_billing_denied=data.get("totalCobrancasNegadas"),
            total_billing_created=data.get("totalCobrancasCriadas")
        )

    def to_dict(self) -> dict:
        """
        Convert the DueBillingBatchSummary instance to a dictionary.

        Returns:
            dict: A dictionary representation of the DueBillingBatchSummary instance.
        """
        return {
            "dataCriacaoProcessamento": self.processing_creation_date,
            "statusProcessamento": self.processing_status,
            "totalCobrancas": self.total_billing,
            "totalCobrancasNegadas": self.total_billing_denied,
            "totalCobrancasCriadas": self.total_billing_created
        }