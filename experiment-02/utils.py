import json

def load_datasets(dataset_path):
    # Initialize an empty list to store the data
    all_data = []
    # Reading a JSONL file
    with open(dataset_path, 'r') as f:
        for line in f:
            # Parse the JSON object from each line
            data = json.loads(line.strip())
            all_data.append(data)
    return all_data