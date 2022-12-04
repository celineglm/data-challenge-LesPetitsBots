from fastapi import APIRouter
from fastapi.responses import FileResponse
import pandas as pd

from app.model import Whitelist

router = APIRouter()

@router.get("/whitelist")
async def get_whitelist():
    return FileResponse('app/data/whitelist.csv', media_type="text/csv")


@router.put("/whitelist/add")
async def add_word(word:str):
    new_word={"word":word}
    Whitelist.add_data(new_word)
    return {"message" : "une ligne a été rajouté à notre csv"}
