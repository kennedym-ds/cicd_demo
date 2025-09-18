"""Test module for Python CI/CD Demo

Comprehensive tests for the main module functions.
"""

import pytest

from python_cicd_demo.main import add, calculate, subtract


class TestAdd:
    """Test cases for the add function."""

    def test_add_positive_integers(self):
        """Test adding positive integers."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30

    def test_add_negative_integers(self):
        """Test adding negative integers."""
        assert add(-2, -3) == -5
        assert add(-10, 5) == -5

    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(2.5, 3.7) == pytest.approx(6.2)
        assert add(1.1, 2.2) == pytest.approx(3.3)

    def test_add_zero(self):
        """Test adding zero."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0


class TestSubtract:
    """Test cases for the subtract function."""

    def test_subtract_positive_integers(self):
        """Test subtracting positive integers."""
        assert subtract(5, 3) == 2
        assert subtract(20, 10) == 10

    def test_subtract_negative_result(self):
        """Test subtraction resulting in negative number."""
        assert subtract(3, 5) == -2
        assert subtract(10, 20) == -10

    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""
        assert subtract(5.5, 2.2) == pytest.approx(3.3)
        assert subtract(10.7, 3.2) == pytest.approx(7.5)

    def test_subtract_zero(self):
        """Test subtracting zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5
        assert subtract(0, 0) == 0


class TestCalculate:
    """Test cases for the calculate function."""

    def test_calculate_add(self):
        """Test calculate function with add operation."""
        assert calculate("add", 2, 3) == 5
        assert calculate("add", -1, 1) == 0

    def test_calculate_subtract(self):
        """Test calculate function with subtract operation."""
        assert calculate("subtract", 5, 3) == 2
        assert calculate("subtract", 1, 1) == 0

    def test_calculate_invalid_operation(self):
        """Test calculate function with invalid operation."""
        with pytest.raises(ValueError, match="Unsupported operation: multiply"):
            calculate("multiply", 2, 3)

        with pytest.raises(ValueError, match="Unsupported operation: divide"):
            calculate("divide", 6, 2)

    def test_calculate_edge_cases(self):
        """Test calculate function edge cases."""
        # Test with floats
        assert calculate("add", 1.5, 2.5) == pytest.approx(4.0)
        assert calculate("subtract", 5.5, 2.5) == pytest.approx(3.0)


# Integration tests
class TestIntegration:
    """Integration test cases."""

    def test_multiple_operations(self):
        """Test multiple operations in sequence."""
        result1 = add(10, 5)
        result2 = subtract(result1, 3)
        assert result2 == 12

    def test_operation_consistency(self):
        """Test that operations are consistent."""
        a, b = 10, 3
        add_result = add(a, b)
        subtract_result = subtract(add_result, b)
        assert subtract_result == a
