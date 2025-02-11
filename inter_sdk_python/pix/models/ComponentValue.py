from dataclasses import dataclass
from typing import Optional

@dataclass
class ComponentValue:
    """
    The ComponentValue class represents a component associated
    with a monetary value.

    It includes the value, the agent's modality, and the
    service provider responsible for handling withdrawal transactions.
    """

    value: Optional[str] = None
    """
    The monetary value of the component.

    This field holds the amount associated with the
    component, represented as a string.
    """

    agent_modality: Optional[str] = None
    """The modality of the agent involved in the withdrawal."""

    withdrawal_service_provider: Optional[str] = None
    """The service provider handling withdrawal transactions."""

    @staticmethod
    def from_dict(data: dict) -> 'ComponentValue':
        """
        Create a ComponentValue instance from a dictionary.

        Args:
            data (dict): A dictionary containing the ComponentValue data.

        Returns:
            ComponentValue: An instance of ComponentValue.
        """
        return ComponentValue(
            value=data.get("valor"),
            agent_modality=data.get("modalidadeAgente"),
            withdrawal_service_provider=data.get("prestadorDoServicoDeSaque")
        )

    def to_dict(self) -> dict:
        """
        Convert the ComponentValue instance to a dictionary.

        Returns:
            dict: A dictionary representation of the ComponentValue instance.
        """
        return {
            "valor": self.value,
            "modalidadeAgente": self.agent_modality,
            "prestadorDoServicoDeSaque": self.withdrawal_service_provider
        }