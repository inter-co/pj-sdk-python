from dataclasses import dataclass
from typing import Optional

from inter_sdk_python.pix.models.PixPayload import PixPayload


@dataclass
class RetrieveCallbackResponse:
    """
    The RetrieveCallbackResponse class represents the response
    received after attempting to retrieve callbacks. It includes
    details such as the webhook URL, number of attempts,
    timestamp of the trigger, success status, HTTP status,
    error message, and associated payload.
    """

    webhook_url: Optional[str] = None
    """The URL of the webhook where the callback is sent."""

    attempt_number: Optional[int] = None
    """The number of attempts made to send the callback."""

    trigger_timestamp: Optional[str] = None
    """The timestamp of when the callback was triggered."""

    success: Optional[bool] = None
    """Indicates whether the callback was sent successfully."""

    http_status: Optional[int] = None
    """The HTTP status code returned after the callback attempt."""

    error_message: Optional[str] = None
    """An error message that may be returned if the callback failed."""

    payload: Optional[PixPayload] = None
    """Payload associated with the callback request."""

    @staticmethod
    def from_dict(data: dict) -> 'RetrieveCallbackResponse':
        """
        Create a RetrieveCallbackResponse instance from a dictionary.

        Args:
            data (dict): A dictionary containing the RetrieveCallbackResponse data.

        Returns:
            RetrieveCallbackResponse: An instance of RetrieveCallbackResponse.
        """
        return RetrieveCallbackResponse(
            webhook_url=data.get("webhookUrl"),
            attempt_number=data.get("numeroTentativa"),
            trigger_timestamp=data.get("dataHoraDisparo"),
            success=data.get("sucesso"),
            http_status=data.get("httpStatus"),
            error_message=data.get("mensagemErro"),
            payload=PixPayload.from_dict(data["payload"]) if data.get("payload") else None
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
            "dataHoraDisparo": self.trigger_timestamp,
            "sucesso": self.success,
            "httpStatus": self.http_status,
            "mensagemErro": self.error_message,
            "payload": self.payload.to_dict() if self.payload else None
        }