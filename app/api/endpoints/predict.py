from fastapi import APIRouter
router = APIRouter()




@router.post("/api/predict")
async def predict_anonymous_data(texte : str):
    return {"Le modèle a prédit que ce texte contient ces données sensibles" :"balalala" }

@router.post("/api/predict/tag")
async def replace_text_by_tag(texte : str):
    return {"Le modèle a prédit que ce texte contient ces données sensibles" :"balalala" }

@router.post("/api/predict/fakedata")
async def replace_text_by_fakedata(texte : str):
    return {"Le modèle a prédit que ce texte contient ces données sensibles" :"balalala" }