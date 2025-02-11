from enum import Enum

class AgentModality(Enum):
    """
    The AgentModality enum represents the different types of agent modalities
    in the PIX system.

    AGTEC: Agente Estabelecimento Comercial (Commercial Establishment Agent)
    AGTOT: Agente Outra Espécie de Pessoa Jurídica ou Correspondente no País
           (Other Type of Legal Entity Agent or Correspondent in the Country)
    AGPSS: Agente Facilitador de Serviço de Saque (Withdrawal Service Facilitator Agent)
    """

    AGTEC = "AGTEC"
    AGTOT = "AGTOT"
    AGPSS = "AGPSS"

    @classmethod
    def from_string(cls, value: str) -> 'AgentModality':
        """
        Create an AgentModality instance from a string value.

        Args:
            value (str): The string representation of the AgentModality.

        Returns:
            AgentModality: The corresponding AgentModality enum value.

        Raises:
            ValueError: If the input string doesn't match any AgentModality value.
        """
        try:
            return cls(value.upper())
        except ValueError:
            raise ValueError(f"'{value}' is not a valid AgentModality value")