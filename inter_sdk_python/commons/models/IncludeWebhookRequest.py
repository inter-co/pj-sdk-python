from dataclasses import dataclass


@dataclass
class IncludeWebhookRequest:
    """
    The IncludeWebhookRequest class represents a request to
    include a webhook URL for receiving notifications about specific events.
    """

    webhook_url: str

    def to_dict(self) -> dict:
        return {
            "webhookUrl": str(self.webhook_url)
        }