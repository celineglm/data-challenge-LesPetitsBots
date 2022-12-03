from fastapi import APIRouter
import pandas as pd

from app.model.Whitelist import add_data

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