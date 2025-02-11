from enum import Enum

class DiscountCode(Enum):
    """
    The DiscountCode enum represents the different types of discounts
    that can be applied to a payment.

    NAOTEMDESCONTO: Indicates that no discount is applied.
    VALORFIXODATAINFORMADA: Indicates a fixed value discount on a specified date.
    PERCENTUALDATAINFORMADA: Indicates a percentage discount on a specified date.
    VALORANTECIPACAODIAUTIL: Indicates a fixed value discount for early payment on a business day.
    PERCENTUALVALORNOMINALDIACORRIDO: Indicates a percentage discount based on the nominal value per calendar day.
    PERCENTUALVALORNOMINALDIAUTIL: Indicates a percentage discount based on the nominal value per business day.
    """

    NAOTEMDESCONTO = "NAOTEMDESCONTO"
    VALORFIXODATAINFORMADA = "VALORFIXODATAINFORMADA"
    PERCENTUALDATAINFORMADA = "PERCENTUALDATAINFORMADA"
    VALORANTECIPACAODIAUTIL = "VALORANTECIPACAODIAUTIL"
    PERCENTUALVALORNOMINALDIACORRIDO = "PERCENTUALVALORNOMINALDIACORRIDO"
    PERCENTUALVALORNOMINALDIAUTIL = "PERCENTUALVALORNOMINALDIAUTIL"

    @classmethod
    def from_string(cls, value: str) -> 'DiscountCode':
        """
        Create a DiscountCode instance from a string value.

        Args:
            value (str): The string representation of the DiscountCode.

        Returns:
            DiscountCode: The corresponding DiscountCode enum value.

        Raises:
            ValueError: If the input string doesn't match any DiscountCode value.
        """
        try:
            return cls(value.upper())
        except ValueError:
            raise ValueError(f"'{value}' is not a valid DiscountCode value")