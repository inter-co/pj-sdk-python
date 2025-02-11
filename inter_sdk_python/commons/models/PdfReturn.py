from dataclasses import dataclass
from typing import Optional

@dataclass
class PdfReturn:
    """
    The PdfReturn class represents the response object
    that includes a PDF file in string format along with any
    additional fields that may be required.
    """

    pdf: Optional[str] = None
    """The PDF file represented as a Base64 encoded string."""

    @staticmethod
    def from_dict(data: dict) -> 'PdfReturn':
        """
        Create a PdfReturn instance from a dictionary.

        Args:
            data (dict): A dictionary containing the PdfReturn data.

        Returns:
            PdfReturn: An instance of PdfReturn.
        """
        return PdfReturn(
            pdf=data.get("pdf")
        )

    def to_dict(self) -> dict:
        """
        Convert the PdfReturn instance to a dictionary.

        Returns:
            dict: A dictionary representation of the PdfReturn instance.
        """
        return {
            "pdf": self.pdf
        }