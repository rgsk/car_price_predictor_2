from ipynb.fs.full.base import get_companies, get_models_for_company, get_fuel_types_for_model, predict_price
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get('/')
async def root():
    return {
        "message": "Server running on port: 8000"
    }


@app.get("/companies")
async def companies():
    return get_companies()


@app.get("/models")
async def models(company: str = ""):
    return get_models_for_company(company)


@app.get("/fuel_types")
async def fuel_types(model: str = ""):
    return get_fuel_types_for_model(model)


@app.get("/predict-price")
async def predict(company: str, model: str, year_of_purchase: int, fuel_type: str, kms_driven: int):
    try:
        return {
            'estimated_price': predict_price(company, model, year_of_purchase, fuel_type, kms_driven)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
