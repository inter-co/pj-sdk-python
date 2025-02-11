from dataclasses import dataclass
from decimal import Decimal
from typing import Dict

@dataclass
class Balance:
    """
    The Balance class represents details about the financial balance,
    including available funds, blocked amounts, and credit limits.
    """

    available: Decimal
    """The available amount of funds."""

    check_blocked: Decimal
    """The amount blocked due to checks."""

    judicially_blocked: Decimal
    """The amount blocked judicially."""

    administratively_blocked: Decimal
    """The amount blocked administratively."""

    limit: Decimal
    """The credit limit available."""

    @staticmethod
    def from_dict(data: Dict) -> 'Balance':
        """
        Create a Balance instance from a dictionary.

        Args:
            data (dict): A dictionary containing the balance data.

        Returns:
            Balance: An instance of Balance.
        """
        return Balance(
            available=Decimal(data.get("disponivel", 0)),
            check_blocked=Decimal(data.get("bloqueadoCheque", 0)),
            judicially_blocked=Decimal(data.get("bloqueadoJudicialmente", 0)),
            administratively_blocked=Decimal(data.get("bloqueadoAdministrativo", 0)),
            limit=Decimal(data.get("limite", 0))
        )

    def to_dict(self) -> dict:
        """
        Convert the Balance instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Balance instance.
        """
        return {
            "disponivel": float(self.available),
            "bloqueadoCheque": float(self.check_blocked),
            "bloqueadoJudicialmente": float(self.judicially_blocked),
            "bloqueadoAdministrativo": float(self.administratively_blocked),
            "limite": float(self.limit)
        }