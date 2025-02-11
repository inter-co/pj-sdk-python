from dataclasses import dataclass, field
from typing import Optional, List, Dict

from inter_sdk_python.banking.models.Payload import Payload


@dataclass
class RetrieveCallbackResponse:
    """
    The RetrieveCallbackResponse class represents the response
    received from a webhook callback for retrieving transaction data.
    """

    webhook_url: Optional[str] = None
    """The URL of the webhook that was triggered."""

    attempt_number: Optional[int] = None
    """The number of attempts made to send the callback."""

    sending_time: Optional[str] = None
    """The time when the callback was sent."""

    trigger_date_time: Optional[str] = None
    """The date and time when the webhook was triggered."""

    success: Optional[bool] = None
    """Indicates whether the callback was successful."""

    http_status: Optional[int] = None
    """The HTTP status code returned from the callback."""

    error_message: Optional[str] = None
    """An error message if the callback was not successful."""

    payload: List[Payload] = field(default_factory=list)
    """A list of payloads containing transaction data."""

    @staticmethod
    def from_dict(data: Dict) -> 'RetrieveCallbackResponse':
        """
        Create a RetrieveCallbackResponse instance from a dictionary.

        Args:
            data (dict): A dictionary containing callback response data.

        Returns:
            RetrieveCallbackResponse: An instance of RetrieveCallbackResponse.
        """
        return RetrieveCallbackResponse(
            webhook_url=data.get("webhookUrl"),
            attempt_number=data.get("numeroTentativa"),
            sending_time=data.get("dataEnvio"),
            trigger_date_time=data.get("dataHoraDisparo"),
            success=data.get("sucesso"),
            http_status=data.get("httpStatus"),
            error_message=data.get("mensagemErro"),
            payload=[Payload.from_dict(item) for item in data.get("payload", [])]
        )

    def to_dict(self) -> dict:
        """
        Convert the RetrieveCallbackResponse instance to a dictionary.

        Returns:
            dict: A dictionary representation of the RetrieveCallbackResponse instance.
        """
        return {
            "webhookUrl": self.webhook_url,
            "numeroTentativa": self.attempt_number,
            "dataEnvio": self.sending_time,
            "dataHoraDisparo": self.trigger_date_time,
            "sucesso": self.success,
            "httpStatus": self.http_status,
            "mensagemErro": self.error_message,
            "payload": [item.to_dict() for item in self.payload]
        }