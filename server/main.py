from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import util

app = FastAPI(title="Bangalore House Prices Prediction API")

# Setup CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PredictionRequest(BaseModel):
    total_sqft: float = Field(..., gt=0, description="Total square footage of the property")
    location: str = Field(..., description="Location of the property")
    bhk: int = Field(..., gt=0, description="Number of bedrooms (BHK)")
    bath: int = Field(..., gt=0, description="Number of bathrooms")

@app.on_event("startup")
async def startup_event():
    print("Starting FastAPI Server For Home Price Prediction...")
    util.load_saved_artifacts()

@app.get("/api/locations")
async def get_location_names():
    locations = util.get_location_names()
    if not locations:
        raise HTTPException(status_code=500, detail="Locations data not loaded")
    return {"locations": locations}

@app.post("/api/predict")
async def predict_home_price(request: PredictionRequest):
    try:
        estimated_price = util.get_estimated_price(
            location=request.location,
            sqft=request.total_sqft,
            bhk=request.bhk,
            bath=request.bath
        )
        return {"estimated_price": estimated_price}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
