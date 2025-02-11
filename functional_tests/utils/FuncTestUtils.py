import decimal

class FuncTestUtils:
    @staticmethod
    def get_string(prompt: str) -> str:
        """
        Prompts the user for input and returns it as a string.

        Args:
            prompt (str): The prompt message to display.

        Returns:
            str: The user input as a string.
        """
        return input(f"{prompt}: ")

    @staticmethod
    def get_big_decimal(prompt: str) -> decimal.Decimal:
        """
        Prompts the user for input and returns it as a BigDecimal.

        Args:
            prompt (str): The prompt message to display.

        Returns:
            decimal.Decimal: The user input as a BigDecimal.
        """
        return decimal.Decimal(input(f"{prompt}: "))