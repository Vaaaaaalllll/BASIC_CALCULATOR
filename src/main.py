<!-- WARNING: template code, may need edits -->
#!/usr/bin/env python3
"""Main entry point for the Basic Calculator application."""

from calculator import Calculator
from utils import get_number_input, get_operation_choice, format_result


def display_menu() -> None:
    """Display the calculator menu options."""
    print("\n" + "="*40)
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")
    print("="*40)


def perform_calculation(choice: str, calc: Calculator) -> bool:
    """Perform the selected calculation.

    Args:
        choice: User's menu choice
        calc: Calculator instance

    Returns:
        True to continue, False to exit
    """
    if choice == '3':
        print("\nThank you for using Basic Calculator. Goodbye!")
        return False

    # Get first number
    num1 = get_number_input("Enter first number: ")
    if num1 is None:
        return True

    # Get second number
    num2 = get_number_input("Enter second number: ")
    if num2 is None:
        return True

    # Perform operation
    if choice == '1':
        result = calc.add(num1, num2)
        print(format_result(num1, num2, '+', result))
    elif choice == '2':
        result = calc.subtract(num1, num2)
        print(format_result(num1, num2, '-', result))

    return True


def main() -> None:
    """Main function to run the calculator application."""
    print("Welcome to Basic Calculator!")
    print("This calculator can add and subtract numbers.")
    
    calc = Calculator()
    
    while True:
        display_menu()
        choice = get_operation_choice()
        
        if choice is None:
            continue
        
        should_continue = perform_calculation(choice, calc)
        if not should_continue:
            break


if __name__ == "__main__":
    main()
