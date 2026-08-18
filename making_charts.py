import os

import kagglehub
import pandas as pd

path = kagglehub.dataset_download("andrewsundberg/college-basketball-dataset")
csv_files = [f for f in os.listdir(path) if f.endswith(".csv")]
data_file_path = os.path.join(path, csv_files[0])

# Load the dataset into Pandas
df = pd.read_csv(data_file_path)
