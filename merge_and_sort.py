import sys

def read_files(file_names):
    """Read the content of each file and return a set of unique lines."""
    unique_lines = set()
    for file_name in file_names:
        try:
            with open(file_name, 'r') as file:
                unique_lines.update(map((lambda x: x.strip() + "\n"), file.readlines()))
        except FileNotFoundError:
            print(f"Error: The file {file_name} could not be found.")
        except IOError:
            print(f"Error: An error occurred while reading the file {file_name}.")
    return unique_lines

def write_to_file(content, output_file_name):
    """Write content to a file."""
    try:
        with open(output_file_name, 'w') as file:
            file.writelines(content)
    except IOError:
        print(f"Error: An error occurred while writing to the file {output_file_name}.")

def main():
    # Retrieve the list of file names excluding the script name
    input_file_names = sys.argv[1:]

    if not input_file_names:
        print("Error: No input files provided.")
        sys.exit(1)

    # Define the output file name
    output_file_name = "merged_and_sorted.txt"

    # Read the unique lines from the files
    unique_lines = read_files(input_file_names)

    # Sort the unique lines
    sorted_unique_lines = sorted(unique_lines)

    # Write the sorted unique lines to the output file
    write_to_file(sorted_unique_lines, output_file_name)

    print(f"Output written to {output_file_name}")

if __name__ == "__main__":
    main()
