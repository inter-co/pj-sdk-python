from dataclasses import dataclass
from typing import Optional

from inter_sdk_python.pix.enums.AgentModality import AgentModality


@dataclass
class Change:
    """
    The Change class represents details regarding change to be
    returned in a withdrawal transaction.

    It includes fields such as the amount of change, the
    modification modality, the agent modality used for the transaction,
    and the service provider responsible for the change service.
    """

    amount: Optional[str] = None
    """The amount of change to be returned."""

    modification_modality: Optional[int] = None
    """The modality of modification applicable to the change."""

    agent_modality: Optional[AgentModality] = None
    """The modality of the agent involved in the transaction."""

    change_service_provider: Optional[str] = None
    """
    The service provider responsible for the change service.

    This field identifies the provider that handles
    the service of returning change during the withdrawal.
    """

    @staticmethod
    def from_dict(data: dict) -> 'Change':
        """
        Create a Change instance from a dictionary.

        Args:
            data (dict): A dictionary containing the change data.

        Returns:
            Change: An instance of Change.
        """
        return Change(
            amount=data.get("valor"),
            modification_modality=data.get("modalidadeAlteracao"),
            agent_modality=AgentModality.from_string(data["modalidadeAgente"]) if data.get("modalidadeAgente") else None,
            change_service_provider=data.get("prestadorDoServicoDeSaque")
        )

    def to_dict(self) -> dict:
        """
        Convert the Change instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Change instance.
        """
        return {
            "valor": self.amount,
            "modalidadeAlteracao": self.modification_modality,
            "modalidadeAgente": self.agent_modality.value if self.agent_modality else None,
            "prestadorDoServicoDeSaque": self.change_service_provider
        }