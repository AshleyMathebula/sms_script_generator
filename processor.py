"""
processor.py

This module handles processing of phone numbers before generating actions.
It includes a basic validation function to filter out numbers containing
unexpected characters.
"""

from typing import List

def filter_valid_numbers(numbers: List[str]) -> List[str]:
    """
    Filters out invalid phone numbers from a list.

    Args:
        numbers (List[str]): List of phone numbers to validate.

    Returns:
        List[str]: Only numbers that pass basic validation.

    Notes:
        - A number is considered valid if it contains only:
            - Digits (0-9)
            - '*' character
            - '?' character
        - Numbers containing any other characters are skipped.
        - Prints a warning for each invalid number.
        - Can be extended in the future to include more complex validation rules.
    """
    valid = []  # Initialize empty list to store valid numbers

    # Loop through all numbers in the input list
    for num in numbers:
        # Check if all characters in the number are either digits, '*' or '?'
        if all(c.isdigit() or c in ["*", "?"] for c in num):
            # If valid, add to the valid list
            valid.append(num)
        else:
            # If invalid, print a warning and skip it
            print(f"Skipping invalid number: {num}")

    # Return the filtered list of valid numbers
    return valid
