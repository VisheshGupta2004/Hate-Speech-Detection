from hate.pipeline.train_pipeline import TrainPipeline
from fastapi import FastAPI, HTTPException
import uvicorn
import sys
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from hate.pipeline.prediction_pipeline import PredictionPipeline
from hate.exception import CustomException
from hate.constants import *
from pydantic import BaseModel


class TextInput(BaseModel):
    text: str


app = FastAPI(
    title="Hate Speech Detection API",
    description="A local API for detecting hate speech in text",
    version="1.0.0"
)

# Add CORS middleware for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "healthy", "message": "Hate Speech Detection API is running"}

@app.get("/train", tags=["training"])
async def training():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        return JSONResponse(
            status_code=200,
            content={"message": "Training successful!", "status": "success"}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": f"Training failed: {str(e)}", "status": "error"}
        )

@app.post("/predict", tags=["prediction"])
async def predict_route(text_input: TextInput):
    try:
        obj = PredictionPipeline()
        result = obj.run_pipeline(text_input.text)
        return JSONResponse(
            status_code=200,
            content={
                "text": text_input.text,
                "prediction": result,
                "status": "success"
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "text": text_input.text,
                "prediction": "Error occurred during prediction",
                "error": str(e),
                "status": "error"
            }
        )

@app.get("/info", tags=["info"])
async def get_info():
    return {
        "app_name": "Hate Speech Detection",
        "version": "1.0.0",
        "description": "Local deployment of hate speech detection model",
        "endpoints": {
            "train": "/train - Train the model",
            "predict": "/predict - Predict hate speech in text",
            "health": "/health - Health check",
            "docs": "/docs - API documentation"
        }
    }

if __name__ == "__main__":
    print(f"Starting Hate Speech Detection API on {APP_HOST}:{APP_PORT}")
    print("Access the API documentation at: http://127.0.0.1:8000/docs")
    uvicorn.run(app, host=APP_HOST, port=APP_PORT, reload=True) 