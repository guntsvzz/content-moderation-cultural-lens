import os
import pickle
import json
import datasets
import tqdm
import time
from datasets import load_dataset

def read_parsed_culture_info(
    data_dir, 
    fpath="culture_scraped_info/culture_info_beta_Nov21.pkl", 
    multi_ling=False
    ):  
    if os.path.exists(data_dir+fpath):
        with open(data_dir+fpath, "rb") as f:
            culture_results = pickle.load(f)
        return culture_results
    return {"metadata":{}}

def load_json(dataset_path):
    # Initialize an empty list to store the data
    all_data = []
    # Reading a JSONL file
    with open(dataset_path, 'r') as f:
        for line in f:
            # Parse the JSON object from each line
            data = json.loads(line.strip())
            all_data.append(data)
    return all_data

def load_datasets(dataset_name):
    """
    Load the dataset based on the selected name.
    """
    if dataset_name == 'candle':
        print("Loading 'candle' dataset...")
        ds = load_json(dataset_path = "datasets/candle_dataset_v1.jsonl")
    elif dataset_name == 'mango':
        print("Loading 'mango' dataset...")
        ds = load_json(dataset_path = "datasets/mango_dataset_v1.jsonl")
    elif dataset_name == 'culture-bank':
        print("Loading 'culture-bank' dataset...")
        ds = datasets.load_dataset("SALT-NLP/CultureBank")
    elif dataset_name == 'culture-atlas':
        print("Loading 'culture-atlas' dataset...")
        ds = None
    else:
        raise ValueError(f"Unknown dataset: {dataset_name}")
    
    return ds