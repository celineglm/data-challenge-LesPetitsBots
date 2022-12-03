import pandas as pd
from csv import DictWriter
def append_dict_as_row(file_name, dict_of_elem, field_names):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as row in the csv
        dict_writer.writerow(dict_of_elem)

def add_data(row_dict):
    field_names=list(row_dict.keys())
    append_dict_as_row('app/data/whitelist.csv', row_dict, field_names)

def get_data():
    return pd.read_csv('app/data/whitelist.csv')
    
    
    

