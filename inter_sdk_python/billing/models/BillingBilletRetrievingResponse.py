from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class BillingBilletRetrievingResponse:
    """
    The BillingBilletRetrievingResponse class represents the response 
    received when retrieving billing billet details, including 
    our number, barcode, and digit line.
    """

    our_number: Optional[str] = None
    """The "our number" associated with the billing billet."""

    barcode: Optional[str] = None
    """The barcode of the billing billet."""

    digit_line: Optional[str] = None
    """The digit line representation of the billing billet."""

    @staticmethod
    def from_dict(data: Dict) -> 'BillingBilletRetrievingResponse':
        """
        Create a BillingBilletRetrievingResponse instance from a dictionary.

        Args:
            data (dict): A dictionary containing billing billet retrieval data.

        Returns:
            BillingBilletRetrievingResponse: An instance of BillingBilletRetrievingResponse.
        """
        return BillingBilletRetrievingResponse(
            our_number=data.get("nossoNumero"),
            barcode=data.get("codigoBarras"),
            digit_line=data.get("linhaDigitavel")
        )

    def to_dict(self) -> dict:
        """
        Convert the BillingBilletRetrievingResponse instance to a dictionary.

        Returns:
            dict: A dictionary representation of the BillingBilletRetrievingResponse instance.
        """
        return {
            "nossoNumero": self.our_number,
            "codigoBarras": self.barcode,
            "linhaDigitavel": self.digit_line
        }