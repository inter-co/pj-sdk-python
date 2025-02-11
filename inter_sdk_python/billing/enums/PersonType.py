from enum import Enum

class PersonType(Enum):
    """
    The PersonType enum represents the types of legal entities
    that can be involved in a billing transaction.

    FISICA: Represents a natural person (individual).
    JURIDICA: Represents a legal entity (company or organization).
    """

    FISICA = "FISICA"
    JURIDICA = "JURIDICA"

    @classmethod
    def from_string(cls, value: str) -> 'PersonType':
        """
        Create a PersonType instance from a string value.

        Args:
            value (str): The string representation of the PersonType.

        Returns:
            PersonType: The corresponding PersonType enum value.

        Raises:
            ValueError: If the input string doesn't match any PersonType value.
        """
        try:
            return cls(value.upper())
        except ValueError:
            raise ValueError(f"'{value}' is not a valid PersonType value")