from fastapi import APIRouter
import pandas as pd
from csv import DictWriter

router = APIRouter()

@router.get("/route")
async def get_whitelist():
    df =  pd.read_csv("app/data/whitelist.csv")
    return {"message" : df}


@router.put("/route")
async def model_donnee_en_plus(Word:str):
    new_word={"word":Word}
    add_data(new_word)
    return {"message" : "une ligne a été rajouté à notre csv"}


def append_dict_as_row(file_name, dict_of_elem, field_names):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as row in the csv
        dict_writer.writerow(dict_of_elem)

def add_data(row_dict):
    field_names=list(row_dict.keys())
    append_dict_as_row('app/datasource/whitelist.csv', row_dict, field_names)

