import sys
from datetime import datetime

def trim_file(file_name: object, start_index: object, end_index: object = None) -> object:
    with open(file_name, 'r') as file:
        lines = file.readlines()

    if end_index is None:
        trimmed_lines = [line[start_index:].replace('%', '') for line in lines]
    else:
        trimmed_lines = [line[start_index:end_index].replace('%', '') for line in lines]

    # Generate output file name
    timestamp = datetime.now().strftime('%d%m%Y%H%M')
    output_file_name = f"{file_name.split('.')[0]}_trimmed{timestamp}.log"

    with open(output_file_name, 'w') as file:
        file.writelines(trimmed_lines)

    # Print the input and output content side by side in the terminal
    for original, trimmed in zip(lines, trimmed_lines):
        print(f"Original: {original}Trimmed: {trimmed}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python trim.py <file_name> <start_index> [<end_index>]")
        sys.exit(1)

    file_name = sys.argv[1]
    start_index = int(sys.argv[2])
    end_index = int(sys.argv[3]) if len(sys.argv) > 3 else None

    trim_file(file_name, start_index, end_index)