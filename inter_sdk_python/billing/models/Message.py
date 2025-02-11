from dataclasses import dataclass
from typing import Optional

@dataclass
class Message:
    """
    The Message class represents a customizable message that can be
    displayed to users, consisting of up to five lines of text.

    It is used to map data from a JSON structure, allowing the
    deserialization of received information for user notifications or alerts.
    """

    line1: Optional[str] = None
    """The first line of the message."""

    line2: Optional[str] = None
    """The second line of the message."""

    line3: Optional[str] = None
    """The third line of the message."""

    line4: Optional[str] = None
    """The fourth line of the message."""

    line5: Optional[str] = None
    """The fifth line of the message."""

    @staticmethod
    def from_dict(data: dict) -> 'Message':
        """
        Create a Message instance from a dictionary.

        Args:
            data (dict): A dictionary containing the message data.

        Returns:
            Message: An instance of Message.
        """
        return Message(
            line1=data.get("linha1"),
            line2=data.get("linha2"),
            line3=data.get("linha3"),
            line4=data.get("linha4"),
            line5=data.get("linha5")
        )

    def to_dict(self) -> dict:
        """
        Convert the Message instance to a dictionary.

        Returns:
            dict: A dictionary containing the message data.
        """
        return {
            "linha1": self.line1,
            "linha2": self.line2,
            "linha3": self.line3,
            "linha4": self.line4,
            "linha5": self.line5
        }