from fastapi import APIRouter
import pandas as pd

from app.model import Whitelist

router = APIRouter()

@router.get("/whitelist")
async def get_whitelist():
    df =  pd.read_csv("app/data/whitelist.csv")
    return {"message" : df}


@router.put("/whitelist/add")
async def add_word(word:str):
    new_word={"word":word}
    Whitelist.add_data(new_word)
    return {"message" : "une ligne a été rajouté à notre csv"}
