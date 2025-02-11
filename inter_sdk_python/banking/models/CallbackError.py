from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class CallbackError:
    """
    The CallbackError class represents an error returned in a callback,
    including an error code and a description.
    """

    error_code: Optional[str] = None
    """The code associated with the error."""

    error_description: Optional[str] = None
    """A description of the error."""

    @staticmethod
    def from_dict(data: Dict) -> 'CallbackError':
        """
        Create a CallbackError instance from a dictionary.

        Args:
            data (dict): A dictionary containing the callback error data.

        Returns:
            CallbackError: An instance of CallbackError.
        """
        return CallbackError(
            error_code=data.get("codigoErro"),
            error_description=data.get("descricaoErro")
        )

    def to_dict(self) -> dict:
        """
        Convert the CallbackError instance to a dictionary.

        Returns:
            dict: A dictionary representation of the CallbackError instance.
        """
        return {
            "codigoErro": self.error_code,
            "descricaoErro": self.error_description
        }