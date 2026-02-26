<!-- WARNING: template code, may need edits -->
"""Utility functions for the calculator application."""

from typing import Optional, Union


def get_number_input(prompt: str) -> Optional[float]:
    """Get and validate numeric input from user.

    Args:
        prompt: Message to display to user

    Returns:
        Float number if valid input, None if invalid

    Examples:
        >>> get_number_input("Enter a number: ")
        # User enters: 42
        42.0
    """
    try:
        value = input(prompt)
        return float(value)
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
        return None


def get_operation_choice() -> Optional[str]:
    """Get operation choice from user.

    Returns:
        Operation choice ('1', '2', or '3') if valid, None otherwise
    """
    choice = input("Enter choice (1/2/3): ").strip()
    if choice in ['1', '2', '3']:
        return choice
    print("Error: Invalid choice. Please enter 1, 2, or 3.")
    return None


def format_result(num1: Union[int, float], num2: Union[int, float], 
                  operation: str, result: Union[int, float]) -> str:
    """Format calculation result as a string.

    Args:
        num1: First number
        num2: Second number
        operation: Operation symbol ('+' or '-')
        result: Calculation result

    Returns:
        Formatted string representation of the calculation

    Examples:
        >>> format_result(10, 5, '+', 15)
        'Result: 10 + 5 = 15'
    """
    return f"Result: {num1} {operation} {num2} = {result}"
