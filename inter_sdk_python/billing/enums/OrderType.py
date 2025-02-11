from enum import Enum

class OrderType(Enum):
    """
    The OrderType enum represents the direction of ordering
    that can be applied to sorting operations.

    ASC: Represents ascending order.
    DESC: Represents descending order.
    """

    ASC = "ASC"
    DESC = "DESC"

    @classmethod
    def from_string(cls, value: str) -> 'OrderType':
        """
        Create an OrderType instance from a string value.

        Args:
            value (str): The string representation of the OrderType.

        Returns:
            OrderType: The corresponding OrderType enum value.

        Raises:
            ValueError: If the input string doesn't match any OrderType value.
        """
        try:
            return cls(value.upper())
        except ValueError:
            raise ValueError(f"'{value}' is not a valid OrderType value")