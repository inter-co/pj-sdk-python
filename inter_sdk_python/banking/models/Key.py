from dataclasses import dataclass, field
from typing import Optional, Dict

from inter_sdk_python.banking.models.Recipient import Recipient


@dataclass
class Key(Recipient):
    """
    The Key class represents a key used for PIX transactions,
    inheriting from the Recipient class and including specific key information.
    """

    type: str = field(default="CHAVE", init=False)
    """The type of the key, defaulting to "CHAVE" for PIX."""

    key: Optional[str] = None
    """The actual key value used for PIX transactions."""

    @staticmethod
    def from_dict(data: Dict) -> 'Key':
        """
        Create a Key instance from a dictionary.

        Args:
            data (dict): A dictionary containing key data.

        Returns:
            Key: An instance of Key.
        """
        return Key(
            key=data.get("chave")
        )

    def to_dict(self) -> dict:
        """
        Convert the Key instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Key instance.
        """
        return {
            "chave": self.key,
            "tipo": self.type
        }