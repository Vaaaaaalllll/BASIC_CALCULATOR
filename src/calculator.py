<!-- WARNING: template code, may need edits -->
"""Calculator module containing core arithmetic operations."""

from typing import Union


class Calculator:
    """A simple calculator class that performs addition and subtraction."""

    @staticmethod
    def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b

        Examples:
            >>> Calculator.add(5, 3)
            8
            >>> Calculator.add(2.5, 1.5)
            4.0
        """
        return a + b

    @staticmethod
    def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract second number from first number.

        Args:
            a: First number (minuend)
            b: Second number (subtrahend)

        Returns:
            Difference of a and b

        Examples:
            >>> Calculator.subtract(10, 3)
            7
            >>> Calculator.subtract(5.5, 2.5)
            3.0
        """
        return a - b
