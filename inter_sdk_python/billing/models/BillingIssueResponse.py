from dataclasses import dataclass
from typing import Optional

@dataclass
class BillingIssueResponse:
    """
    The BillingIssueResponse class represents the response received after
    issuing a billing statement, containing the request code assigned automatically
    by the bank upon the issuance of the title.

    This response is critical for confirming successful billing operations,
    allowing users to track or reference their requests based on the generated request code.
    """

    request_code: Optional[str] = None
    """The request code assigned by the bank."""

    @staticmethod
    def from_dict(data: dict) -> 'BillingIssueResponse':
        """
        Create a BillingIssueResponse instance from a dictionary.

        Args:
            data (dict): A dictionary containing the response data.

        Returns:
            BillingIssueResponse: An instance of BillingIssueResponse.
        """
        return BillingIssueResponse(
            request_code=data.get("codigoSolicitacao")
        )

    def to_dict(self) -> dict:
        """
        Convert the BillingIssueResponse instance to a dictionary.

        Returns:
            dict: A dictionary representation of the BillingIssueResponse.
        """
        return {
            "codigoSolicitacao": self.request_code
        }