from fastapi import FastAPI
from app.api.endpoints import predict
from app.api.endpoints import route2

app = FastAPI(
    title="LesPetitsBots_Project_Data-Challenge",
    version="0.1"
)


app.include_router(predict.router)
app.include_router(route2.router)

@app.get("/")
async def home():
    return {"message" : "Hello World"}

