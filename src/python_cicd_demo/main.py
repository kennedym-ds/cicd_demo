"""Main module for Python CI/CD Demo

This module contains simple mathematical functions to demonstrate
testing, documentation, and CI/CD practices.
"""

import os
from typing import Union

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b

    Examples:
        >>> add(2, 3)
        5
        >>> add(2.5, 1.5)
        4.0
    """
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Subtract the second number from the first.

    Args:
        a: Number to subtract from
        b: Number to subtract

    Returns:
        The difference of a and b

    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(10.5, 3.5)
        7.0
    """
    return a - b


def calculate(
    operation: str, a: Union[int, float], b: Union[int, float]
) -> Union[int, float]:
    """Perform a calculation based on the operation string.

    Args:
        operation: The operation to perform ('add' or 'subtract')
        a: First number
        b: Second number

    Returns:
        The result of the calculation

    Raises:
        ValueError: If operation is not supported

    Examples:
        >>> calculate('add', 2, 3)
        5
        >>> calculate('subtract', 5, 3)
        2
    """
    operations = {"add": add, "subtract": subtract}

    if operation not in operations:
        raise ValueError(f"Unsupported operation: {operation}")

    return operations[operation](a, b)


def main():
    """Main function for demonstration purposes."""
    print("Python CI/CD Demo")
    print("=================")

    # Example usage
    result1 = add(10, 5)
    result2 = subtract(10, 3)

    print(f"10 + 5 = {result1}")
    print(f"10 - 3 = {result2}")

    # Use environment variable if available
    debug_mode = os.getenv("DEBUG", "false").lower() == "true"
    if debug_mode:
        print("Debug mode is enabled")


if __name__ == "__main__":
    main()
