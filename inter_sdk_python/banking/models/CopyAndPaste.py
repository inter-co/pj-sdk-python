from dataclasses import dataclass
from typing import Optional, Dict

from inter_sdk_python.banking.models.Recipient import Recipient


@dataclass
class CopyAndPaste(Recipient):
    """
    The CopyAndPaste class represents a recipient using the Copy and Paste method,
    including the copy-and-paste data and type.
    """

    copy_and_paste: Optional[str] = None
    """The data to be used for copy-and-paste."""

    _type_: Optional[str] = None
    """The type of copy-and-paste data."""

    @staticmethod
    def from_dict(data: Dict) -> 'CopyAndPaste':
        """
        Create a CopyAndPaste instance from a dictionary.

        Args:
            data (dict): A dictionary containing the copy-and-paste data.

        Returns:
            CopyAndPaste: An instance of CopyAndPaste.
        """
        return CopyAndPaste(
            copy_and_paste=data.get("pixCopiaECola"),
            _type_=data.get("tipo")
        )

    def to_dict(self) -> dict:
        """
        Convert the CopyAndPaste instance to a dictionary.

        Returns:
            dict: A dictionary representation of the CopyAndPaste instance.
        """
        return {
            "pixCopiaECola": self.copy_and_paste,
            "tipo": self._type_
        }