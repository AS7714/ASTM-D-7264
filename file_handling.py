import os
import pandas as pd

def read_data_from_excel(excel_file, data_range):
    data_table = pd.read_excel(excel_file, usecols="A:C", skiprows=1, nrows=10)
    return data_table

def load_sample_data(sample_folder, sample_name):
    sample_data_file = os.path.join(sample_folder, 'DAQ- Crosshead, … - (Timed).txt')
    if os.path.isfile(sample_data_file):
        print(f'Processing file: {sample_data_file}')
        sample_data = pd.read_csv(sample_data_file)
        return sample_data
    else:
        print(f'File {sample_data_file} does not exist. Skipping...')
        return None
