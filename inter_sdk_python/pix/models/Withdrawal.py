from dataclasses import dataclass
from typing import Optional

from inter_sdk_python.pix.enums.AgentModality import AgentModality


@dataclass
class Withdrawal:
    """
    The Withdrawal class represents details regarding a withdrawal
    transaction. It includes fields such as the amount of the withdrawal,
    the modification modality, the agent modality used for the transaction,
    and the service provider responsible for the withdrawal.
    """

    amount: Optional[str] = None
    """The amount of the withdrawal."""

    modification_modality: Optional[int] = None
    """The modification modality for the withdrawal."""

    agent_modality: Optional[AgentModality] = None
    """The agent modality used for the transaction."""

    withdrawal_service_provider: Optional[str] = None
    """The service provider responsible for the withdrawal."""

    @staticmethod
    def from_dict(data: dict) -> 'Withdrawal':
        """
        Create a Withdrawal instance from a dictionary.

        Args:
            data (dict): A dictionary containing the Withdrawal data.

        Returns:
            Withdrawal: An instance of Withdrawal.
        """
        return Withdrawal(
            amount=data.get("valor"),
            modification_modality=data.get("modalidadeAlteracao"),
            agent_modality=AgentModality[data["modalidadeAgente"]] if "modalidadeAgente" in data else None,
            withdrawal_service_provider=data.get("prestadorDoServicoDeSaque")
        )

    def to_dict(self) -> dict:
        """
        Convert the Withdrawal instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Withdrawal instance.
        """
        return {
            "valor": self.amount,
            "modalidadeAlteracao": self.modification_modality,
            "modalidadeAgente": self.agent_modality.name if self.agent_modality else None,
            "prestadorDoServicoDeSaque": self.withdrawal_service_provider
        }