"""
main.py

Entry point for the SMS action line generator.

This script:
1. Reads numbers from 'numbers.txt' located in the project root.
2. Generates formatted SMS action lines using the specified destination.
3. Writes the results to an output file named 'output_<destination>.txt'.
4. Supports an optional command-line argument to specify the destination.
"""

# Standard library imports
from pathlib import Path  # For handling file paths in a cross-platform way
import sys               # For accessing command-line arguments

# Local package imports (modules within sms_generator/)
from .io_utils import read_numbers, write_output  # Functions to read/write files
from .generator import generate_actions           # Function to generate SMS actions

def main():
    """
    Main workflow of the SMS action generator.

    Steps:
    1. Get destination from command-line arguments (default: 'cellfsc').
    2. Determine absolute paths for input and output files.
    3. Check if the input file exists; exit with error if not.
    4. Read numbers from the input file.
    5. Generate formatted action lines for each number.
    6. Write the results to the output file.
    7. Print a summary of the operation.
    """

    # Get destination name from command-line argument if provided
    # Example usage: python -m sms_generator.main mydest
    # Default destination is "cellfsc" if no argument is given
    dest = sys.argv[1] if len(sys.argv) > 1 else "cellfsc"

    # Determine absolute path to project root (parent of sms_generator/)
    project_root = Path(__file__).parent.parent.resolve()

    # Construct paths for input and output files
    # Input file is 'numbers.txt' in project root
    input_file = project_root / "numbers.txt"
    # Output file will be 'output_<dest>.txt' in the same folder
    output_file = project_root / f"output_{dest}.txt"

    # Debug print statements to verify paths
    print(f"Looking for numbers.txt at: {input_file}")
    print(f"Output file will be: {output_file}")

    # Check if input file exists; if not, print error and exit
    if not input_file.exists():
        print(f"❌ Error: {input_file} not found.")
        return

    # --- Workflow ---
    # Step 1: Read all numbers from the input file
    numbers = read_numbers(input_file)

    # Step 2: Generate formatted SMS action lines for each number
    actions = generate_actions(numbers, dest)

    # Step 3: Write the generated actions to the output file
    write_output(output_file, actions)

    # Step 4: Print a summary
    print(f"✅ Done! Processed {len(actions)} numbers.")
    print(f"Results saved in {output_file}")
    print(f"Destination used: {dest}")

# Standard Python idiom to ensure main() runs only if script is executed directly
if __name__ == "__main__":
    main()
