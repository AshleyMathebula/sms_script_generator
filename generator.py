"""
generator.py

Contains the function to generate formatted SMS action lines
from phone numbers and a specified destination.

Function:
- generate_actions: Converts numbers into properly formatted action lines.
"""

from typing import List

def generate_actions(numbers: List[str], dest: str) -> List[str]:
    """
    Generate SMS action lines for a list of phone numbers.

    Args:
        numbers (List[str]): List of phone numbers (strings).
        dest (str): Destination code to use in the action lines.

    Returns:
        List[str]: Formatted SMS action lines ready for output.

    Example format:
        { "?.?.27840037335*" }  : Actions SET_DEST_LA("cellfsc"),SET_ESME_GROUP(SAG_GROUP_1, A_ADDR)

    Notes:
        - If a number contains '?' and '*', the '?' is removed and '*' is kept.
        - Replaces default placeholder destination with the provided 'dest'.
    """
    actions = []
    for number in numbers:
        # Replace '?' with nothing and keep '*' if present
        clean_number = number.replace("?", "")
        # Format line according to the action pattern
        line = f'{{ "?.?.{clean_number}" }}  : Actions SET_DEST_LA("{dest}"),SET_ESME_GROUP(SAG_GROUP_1, A_ADDR)'
        actions.append(line)
    return actions
