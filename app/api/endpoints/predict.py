from fastapi import APIRouter
router = APIRouter()




@router.post("/api/predict")
async def predict_anonymous_data(sentence : str):
    return {"Le modèle a prédit que ce texte contient ces données sensibles" :"balalala" }

@router.post("/api/predict/tag")
async def replace_text_by_tag(sentence : str):
    return {"Le modèle a prédit que ce texte contient ces données sensibles" :"balalala" }

@router.post("/api/predict/fakedata")
async def replace_text_by_fakedata(sentence : str):
    return {"Le modèle a prédit que ce texte contient ces données sensibles" :"balalala" }