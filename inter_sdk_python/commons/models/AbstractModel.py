import json
from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class AbstractModel:
    """
    Abstract base class for all model classes in the banking SDK.
    Provides common functionality for handling additional fields and
    implements robust equals, hashCode, and toString methods.
    """

    additional_fields: Dict[str, str] = field(default_factory=dict)

    def get_additional_fields(self) -> Dict[str, str]:
        """
        Returns a copy of the additional fields.
        """
        return self.additional_fields.copy()

    def set_additional_field(self, name: str, value: str) -> None:
        """
        Adds an additional field to the model object.
        """
        self.additional_fields[name] = value

    def set_additional_fields(self, additional_fields: Dict[str, str]) -> None:
        """
        Sets the entire map of additional fields.
        """
        self.additional_fields = additional_fields.copy()

    def to_json(self) -> str:
        """
        Converts the model to JSON.
        """
        return json.dumps(self.additional_fields)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, AbstractModel):
            return False
        return self.additional_fields == other.additional_fields

    def __hash__(self) -> int:
        return hash(frozenset(self.additional_fields.items()))

    def __str__(self) -> str:
        additional_str = ", ".join(f"{key}={value}" for key, value in self.additional_fields.items())
        return f"AbstractModel[{additional_str}]"

if __name__ == "__main__":
    model = AbstractModel()
    model.set_additional_field("key1", "value1")
    model.set_additional_field("key2", "value2")
    
    print(model)  # Output: AbstractModel[key1=value1, key2=value2]
    print(model.to_json())  # Output: {"key1": "value1", "key2": "value2"}