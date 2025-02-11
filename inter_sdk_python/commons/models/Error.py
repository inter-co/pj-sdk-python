from dataclasses import dataclass, field
from typing import List, Optional, Dict

from inter_sdk_python.commons.models.Violation import Violation

@dataclass
class Error:
    """
    The Error class represents an error response object containing
    details about an error that occurred during processing. It includes
    a title, a detailed description, the timestamp of the error,
    any violations associated with the error, and additional fields.
    """

    title: Optional[str] = None
    detail: Optional[str] = None
    timestamp: Optional[str] = None
    violations: List[Violation] = field(default_factory=list)

    @staticmethod
    def from_dict(data: Dict) -> 'Error':
        """Create an Error instance from a dictionary."""

        violations_data = data.get("violacoes", [])
        violations = [Violation.from_dict(v) for v in violations_data] if violations_data else []

        return Error(
            title=data.get("title"),
            detail=data.get("detail"),
            timestamp=data.get("timestamp"),
            violations=violations
        )

    def to_dict(self) -> Dict:
        """Convert the Error instance to a dictionary."""

        return {
            "title": self.title,
            "detail": self.detail,
            "timestamp": self.timestamp,
            "violations": [violation.to_dict() for violation in self.violations]
        }