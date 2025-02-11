from dataclasses import dataclass
from typing import Optional

@dataclass
class BillingPixRetrievingResponse:
    """
    The BillingPixRetrievingResponse class represents the response received
    when retrieving information about a Pix transaction.

    It contains the transaction identifier (txid) and the copy-paste
    string of the Pix payment, allowing for easy transaction retrieval and processing.
    This structure is utilized to map data from a JSON format, facilitating the
    deserialization of the information received.
    """

    transaction_id: Optional[str] = None
    """The transaction identifier for the Pix transaction."""

    pix_copy_and_paste: Optional[str] = None
    """The copy-paste string for the Pix payment."""

    @staticmethod
    def from_dict(data: dict) -> 'BillingPixRetrievingResponse':
        """
        Create a BillingPixRetrievingResponse instance from a dictionary.

        Args:
            data (dict): A dictionary containing the Pix retrieving response data.

        Returns:
            BillingPixRetrievingResponse: An instance of BillingPixRetrievingResponse.
        """
        return BillingPixRetrievingResponse(
            transaction_id=data.get("txid"),
            pix_copy_and_paste=data.get("pixCopiaECola")
        )

    def to_dict(self) -> dict:
        """
        Convert the BillingPixRetrievingResponse instance to a dictionary.

        Returns:
            dict: A dictionary containing the Pix retrieving response data.
        """
        return {
            "txid": self.transaction_id,
            "pixCopiaECola": self.pix_copy_and_paste
        }