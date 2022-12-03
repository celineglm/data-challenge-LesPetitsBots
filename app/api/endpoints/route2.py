from fastapi import APIRouter

router = APIRouter()

@router.get("/route")
async def yo():
    return {"message" : "Le modèle sérialisé est sauvegardé"}



