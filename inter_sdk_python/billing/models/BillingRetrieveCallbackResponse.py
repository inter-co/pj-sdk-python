from dataclasses import dataclass, field
from typing import Optional, List

from inter_sdk_python.billing.models.BillingPayload import BillingPayload


@dataclass
class BillingRetrieveCallbackResponse:
    """
    The BillingRetrieveCallbackResponse class represents the response structure
    for retrieving callback information.

    It includes details such as the URL of the webhook, the number of
    attempts made to trigger the callback, the timestamp of the last trigger,
    and the success status of the callback. Additionally, it may contain the
    HTTP status, error message, and a list of payloads related to the callback.
    This structure is essential for managing and responding to callback inquiries.
    """

    webhook_url: Optional[str] = None
    """The URL of the webhook that handles the callbacks."""

    attempt_number: Optional[int] = None
    """The number of attempts made to trigger the callback."""

    trigger_date_time: Optional[str] = None
    """The timestamp of the last trigger of the callback."""

    success: Optional[bool] = None
    """The success status of the callback attempt."""

    http_status: Optional[int] = None
    """The HTTP status code returned from the last callback attempt."""

    error_message: Optional[str] = None
    """The error message related to the last callback attempt, if any."""

    payload: List[BillingPayload] = field(default_factory=list)
    """A list of payloads related to the callback."""

    @staticmethod
    def from_dict(data: dict) -> 'BillingRetrieveCallbackResponse':
        """
        Create a BillingRetrieveCallbackResponse instance from a dictionary.

        Args:
            data (dict): A dictionary containing the callback response data.

        Returns:
            BillingRetrieveCallbackResponse: An instance of BillingRetrieveCallbackResponse.
        """
        return BillingRetrieveCallbackResponse(
            webhook_url=data.get("webhookUrl"),
            attempt_number=data.get("numeroTentativa"),
            trigger_date_time=data.get("dataHoraDisparo"),
            success=data.get("sucesso"),
            http_status=data.get("httpStatus"),
            error_message=data.get("mensagemErro"),
            payload=[BillingPayload.from_dict(item) for item in data.get("payload", [])]
        )

    def to_dict(self) -> dict:
        """
        Convert the BillingRetrieveCallbackResponse instance to a dictionary.

        Returns:
            dict: A dictionary containing the callback response data.
        """
        return {
            "webhookUrl": self.webhook_url,
            "numeroTentativa": self.attempt_number,
            "dataHoraDisparo": self.trigger_date_time,
            "sucesso": self.success,
            "httpStatus": self.http_status,
            "mensagemErro": self.error_message,
            "payload": [item.to_dict() for item in self.payload]
        }