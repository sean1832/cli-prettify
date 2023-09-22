import json
import sys

flatten = False

try:
    # check if argument is given
    if len(sys.argv) < 2:
        print("Usage: prettify <input_file_path>")
        exit(1)

    input_file_path = sys.argv[1]
    if len(sys.argv) > 2:
        if sys.argv[2] == '--flatten':
            flatten = True

    if flatten:
        with open(input_file_path) as f:
            data = json.load(f)
        data_flattened = json.dumps(data)
        with open(input_file_path, 'w') as f:
            f.write(data_flattened)
    else:
        if not input_file_path.endswith('.json'):
            print("Input file must be a JSON file.")
            exit(1)

        with open(input_file_path, 'r') as f:
            data = json.load(f)

        prettified = json.dumps(data, indent=4)

        with open(input_file_path, 'w') as f:
            f.write(prettified)
    print("prettification completed.")
except Exception as e:
    print(e)
    print("failed to prettify file.")
    exit(1)