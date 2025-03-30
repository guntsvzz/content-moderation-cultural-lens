import os
import pickle
import json
import datasets
import tqdm
import time
import pandas as pd
from datasets import load_dataset

def read_parsed_culture_info(
    data_dir="datasets", 
    fpath="/culture_info_beta_Nov21.pkl", 
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

def load_dataframe(dataset_path):
    df_neg = pd.read_csv(dataset_path)
    df_neg = df_neg.drop(df_neg.columns[[11, 12, 13, 14, 15,16]], axis=1)

    # Set the column names
    df_neg.columns = [
        'country', 'topic', 'subtopic', 'subsubtopic',
        'url', 'assertion', 'pos1', 'pos2', 'pos3', 'neg', 'label'
    ]
    return df_neg.to_dict(orient='records')


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
    elif dataset_name == 'culture-atlas-negative':
        print("Loading 'culture-atlas-negative' dataset...")
        ds = load_dataframe(dataset_path = 'experiment-02/datasets/benchmark/benchmarK_Feb4_neg10k.csv')
    else:
        raise ValueError(f"Unknown dataset: {dataset_name}")
    
    return ds