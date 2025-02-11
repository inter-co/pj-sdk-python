from typing import Dict

from pydantic import BaseModel


class Webhook(BaseModel):
    """
    The Webhook class represents a webhook configuration,
    including the webhook URL and creation date.
    """

    webhook_url: str
    creation_date: str

    @staticmethod
    def from_dict(_data_: Dict) -> 'Webhook':
        """
        Create a Webhook instance from a dictionary.

        Args:
            _data_ (dict): A dictionary containing webhook data.

        Returns:
            Webhook: An instance of Webhook.
        """
        return Webhook(
            webhook_url=_data_.get("webhookUrl"),
            creation_date=_data_.get("criacao")
        )

    def to_dict(self) -> Dict[str, str]:
        """
        Convert the Webhook instance to a dictionary.

        Returns:
            dict: A dictionary containing webhook data.
        """
        return {
            "webhookUrl": self.webhook_url,
            "criacao": self.creation_date
        }


