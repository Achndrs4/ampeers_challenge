import pandas as pd
from itertools import groupby

def read_csv_file(file_location = str) -> pd.DataFrame:
    filepath = file_location
    return pd.read_csv(filepath, delimiter=";")

def write_csv_file(df : pd.DataFrame , file_location = str) -> None:
    df.to_csv(file_location, index=False)
    
def write_json_file(df : pd.DataFrame , file_location = str) -> None:
    df.to_json(file_location, orient='records')
    
def split_dict_by_key(input_dict, splitting_key) -> list:
    sorted_data = sorted(input_dict, key=lambda x: x[splitting_key])
    grouped_data = groupby(sorted_data, key=lambda x: x[splitting_key])
    result = [[item for item in group] for _, group in grouped_data]
    return result
    
def write_string_to_file(text, filename):
    with open(filename, 'w') as file:
        file.write(text)
        
def get_row_name_from_temperature(temperature) -> str:
    return 'P_VALUE_FOR{}_DEGREES'.format(str(temperature))