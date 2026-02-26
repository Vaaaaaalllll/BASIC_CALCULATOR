<!-- WARNING: template code, may need edits -->
"""Unit tests for the Calculator class."""

import pytest
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from calculator import Calculator


class TestCalculator:
    """Test suite for Calculator class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        assert self.calc.add(5, 3) == 8
        assert self.calc.add(10, 20) == 30

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        assert self.calc.add(-5, -3) == -8
        assert self.calc.add(-10, 5) == -5

    def test_add_floats(self):
        """Test addition of floating point numbers."""
        assert self.calc.add(2.5, 3.5) == 6.0
        assert self.calc.add(1.1, 2.2) == pytest.approx(3.3)

    def test_add_zero(self):
        """Test addition with zero."""
        assert self.calc.add(0, 5) == 5
        assert self.calc.add(10, 0) == 10
        assert self.calc.add(0, 0) == 0

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        assert self.calc.subtract(10, 3) == 7
        assert self.calc.subtract(20, 5) == 15

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        assert self.calc.subtract(-5, -3) == -2
        assert self.calc.subtract(10, -5) == 15

    def test_subtract_floats(self):
        """Test subtraction of floating point numbers."""
        assert self.calc.subtract(5.5, 2.5) == 3.0
        assert self.calc.subtract(10.7, 3.2) == pytest.approx(7.5)

    def test_subtract_zero(self):
        """Test subtraction with zero."""
        assert self.calc.subtract(5, 0) == 5
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(0, 0) == 0

    def test_subtract_larger_from_smaller(self):
        """Test subtracting larger number from smaller."""
        assert self.calc.subtract(3, 10) == -7
        assert self.calc.subtract(1, 100) == -99

    def test_large_numbers(self):
        """Test operations with large numbers."""
        assert self.calc.add(1000000, 2000000) == 3000000
        assert self.calc.subtract(5000000, 2000000) == 3000000
