"""
io_utils.py

This module provides utility functions for reading numbers from a text file
and writing the formatted output to a file.

Functions:
- read_numbers: Reads numbers from a text file, one per line.
- write_output: Writes a list of formatted action lines to a text file.
"""

from pathlib import Path
from typing import List

def read_numbers(file_path: str) -> List[str]:
    """
    Read numbers from a text file, one per line.

    Args:
        file_path (str): Path to the input text file containing numbers.

    Returns:
        List[str]: List of raw number strings from the file.

    Raises:
        FileNotFoundError: If the input file does not exist.

    Notes:
        - Strips trailing newline characters from each line.
        - Returns only non-empty lines, ignoring empty lines.
    """
    path = Path(file_path)

    # Check if the file exists
    if not path.exists():
        raise FileNotFoundError(f"❌ Error: {file_path} not found.")

    # Read all lines from the file
    lines = path.read_text(encoding="utf-8").splitlines()

    # Filter out empty lines
    numbers = [line.strip() for line in lines if line.strip()]
    return numbers


def write_output(file_path: str, lines: List[str]) -> None:
    """
    Write the formatted action lines to a text file.

    Args:
        file_path (str): Path to the output file.
        lines (List[str]): List of formatted action lines to write.

    Returns:
        None

    Notes:
        - Overwrites the file if it already exists.
        - Each line in 'lines' will be written on a separate line in the file.
        - Uses UTF-8 encoding for cross-platform compatibility.
    """
    path = Path(file_path)

    # Join all lines with newline characters and save to file
    path.write_text("\n".join(lines), encoding="utf-8")
