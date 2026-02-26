<!-- WARNING: template code, may need edits -->
"""Unit tests for utility functions."""

import pytest
import sys
from pathlib import Path
from io import StringIO
from unittest.mock import patch

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from utils import format_result, get_number_input, get_operation_choice


class TestFormatResult:
    """Test suite for format_result function."""

    def test_format_addition(self):
        """Test formatting addition result."""
        result = format_result(10, 5, '+', 15)
        assert result == "Result: 10 + 5 = 15"

    def test_format_subtraction(self):
        """Test formatting subtraction result."""
        result = format_result(10, 5, '-', 5)
        assert result == "Result: 10 - 5 = 5"

    def test_format_floats(self):
        """Test formatting with float numbers."""
        result = format_result(10.5, 5.2, '+', 15.7)
        assert result == "Result: 10.5 + 5.2 = 15.7"

    def test_format_negative_result(self):
        """Test formatting negative result."""
        result = format_result(5, 10, '-', -5)
        assert result == "Result: 5 - 10 = -5"


class TestGetNumberInput:
    """Test suite for get_number_input function."""

    @patch('builtins.input', return_value='42')
    def test_valid_integer_input(self, mock_input):
        """Test valid integer input."""
        result = get_number_input("Enter number: ")
        assert result == 42.0

    @patch('builtins.input', return_value='3.14')
    def test_valid_float_input(self, mock_input):
        """Test valid float input."""
        result = get_number_input("Enter number: ")
        assert result == 3.14

    @patch('builtins.input', return_value='-10')
    def test_negative_number_input(self, mock_input):
        """Test negative number input."""
        result = get_number_input("Enter number: ")
        assert result == -10.0

    @patch('builtins.input', return_value='abc')
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_input(self, mock_stdout, mock_input):
        """Test invalid non-numeric input."""
        result = get_number_input("Enter number: ")
        assert result is None
        assert "Error: Invalid input" in mock_stdout.getvalue()


class TestGetOperationChoice:
    """Test suite for get_operation_choice function."""

    @patch('builtins.input', return_value='1')
    def test_valid_choice_1(self, mock_input):
        """Test valid choice 1 (add)."""
        result = get_operation_choice()
        assert result == '1'

    @patch('builtins.input', return_value='2')
    def test_valid_choice_2(self, mock_input):
        """Test valid choice 2 (subtract)."""
        result = get_operation_choice()
        assert result == '2'

    @patch('builtins.input', return_value='3')
    def test_valid_choice_3(self, mock_input):
        """Test valid choice 3 (exit)."""
        result = get_operation_choice()
        assert result == '3'

    @patch('builtins.input', return_value='4')
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_choice(self, mock_stdout, mock_input):
        """Test invalid choice."""
        result = get_operation_choice()
        assert result is None
        assert "Error: Invalid choice" in mock_stdout.getvalue()

    @patch('builtins.input', return_value='abc')
    @patch('sys.stdout', new_callable=StringIO)
    def test_non_numeric_choice(self, mock_stdout, mock_input):
        """Test non-numeric choice."""
        result = get_operation_choice()
        assert result is None
