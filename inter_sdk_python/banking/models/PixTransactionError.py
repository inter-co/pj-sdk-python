from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class PixTransactionError:
    """
    The PixTransactionError class represents an error associated with 
    a PIX transaction, including error codes and descriptions.
    """

    error_code: Optional[str] = None
    """The error code associated with the PIX transaction."""

    error_description: Optional[str] = None
    """A description of the error that occurred."""

    complementary_error_code: Optional[str] = None
    """An additional error code providing more context."""

    @staticmethod
    def from_dict(data: Dict) -> 'PixTransactionError':
        """
        Create a PixTransactionError instance from a dictionary.

        Args:
            data (dict): A dictionary containing PIX transaction error data.

        Returns:
            PixTransactionError: An instance of PixTransactionError.
        """
        return PixTransactionError(
            error_code=data.get("codigoErro"),
            error_description=data.get("descricaoErro"),
            complementary_error_code=data.get("codigoErroComplementar")
        )

    def to_dict(self) -> dict:
        """
        Convert the PixTransactionError instance to a dictionary.

        Returns:
            dict: A dictionary representation of the PixTransactionError instance.
        """
        return {
            "codigoErro": self.error_code,
            "descricaoErro": self.error_description,
            "codigoErroComplementar": self.complementary_error_code
        }