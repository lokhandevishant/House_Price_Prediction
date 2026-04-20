from fastapi import FastAPI, HTTPException
from .model import predict, train_and_save_model
from pydantic import BaseModel

app = FastAPI(title="Housing Price API")

class HousingFeatures(BaseModel):
    area: int
    bedrooms: int
    bathrooms: int
    stories: int
    mainroad: str
    guestroom: str
    basement: str
    hotwaterheating: str
    airconditioning: str
    parking: int
    prefarea: str
    furnishingstatus: str

@app.post("/train")
def train():
    try:
        metrics = train_and_save_model("data/housing.csv")
        return {"message": "Model trained successfully", "metrics": metrics}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict")
def get_prediction(features: HousingFeatures):
    try:
        res = predict(features.dict())
        return {"estimated_price": res}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))