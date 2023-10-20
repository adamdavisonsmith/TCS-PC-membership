import re
import sys

def extract_names(input_file_path, output_file_path):
    try:
        # Open the input file and read the content
        with open(input_file_path, 'r') as input_file:
            lines = input_file.readlines()

        # Prepare a list to store extracted names
        names = []

        # Regular expression to identify the name and ignore the parentheses part
        pattern = re.compile(r'^(.*?)\s*\((.*?)\)\s*$')

        for line in lines:
            # Remove the trailing spaces and newline characters
            line = line.strip()

            # Search for the pattern in the line
            match = pattern.search(line)
            if match:
                # Extract the name part, which is the first group in the match
                names.append(match.group(1))

        # Write the names to the output file
        with open(output_file_path, 'w') as output_file:
            for name in names:
                output_file.write(name + '\n')

    except FileNotFoundError:
        print(f"File not found: {input_file_path}")
        sys.exit(1)
    except IOError as e:
        print(f"An I/O error occurred: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    # The script expects exactly two arguments (excluding the script name): input and output file paths
    if len(sys.argv) != 3:
        print("Usage: python script.py <path_to_input_file> <path_to_output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    extract_names(input_file, output_file)

if __name__ == "__main__":
    main()
