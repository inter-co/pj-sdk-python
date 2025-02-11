from dataclasses import dataclass, field
from typing import Optional, List

from inter_sdk_python.pix.models.Violation import Violation


@dataclass
class Problem:
    """
    The Problem class represents an error or problem encountered
    during a PIX transaction. It includes various fields detailing the
    nature of the problem, including its type, title, status, and any
    relevant violations.
    """

    type: Optional[str] = None
    """The type of the problem."""

    title: Optional[str] = None
    """A brief title describing the problem."""

    status: Optional[int] = None
    """The HTTP status code associated with the problem."""

    detail: Optional[str] = None
    """Detailed information about the problem."""

    correlation_id: Optional[str] = None
    """A unique correlation ID for tracing the problem."""

    violations: List[Violation] = field(default_factory=list)
    """A list of violations associated with the problem."""

    @staticmethod
    def from_dict(data: dict) -> 'Problem':
        """
        Create a Problem instance from a dictionary.

        Args:
            data (dict): A dictionary containing the Problem data.

        Returns:
            Problem: An instance of Problem.
        """
        return Problem(
            type=data.get("type"),
            title=data.get("title"),
            status=data.get("status"),
            detail=data.get("detail"),
            correlation_id=data.get("correlationId"),
            violations=[Violation.from_dict(v) for v in data.get("violacoes", [])]
        )

    def to_dict(self) -> dict:
        """
        Convert the Problem instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Problem instance.
        """
        return {
            "type": self.type,
            "title": self.title,
            "status": self.status,
            "detail": self.detail,
            "correlationId": self.correlation_id,
            "violacoes": [v.to_dict() for v in self.violations]
        }