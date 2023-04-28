from fastapi import FastAPI, HTTPException
import pandas as pd
import pickle

app = FastAPI()

lr_model = pickle.load(open("LinearRegressionModel.pkl", 'rb'))


def predict_price(company: str, model: str, year_of_purchase: int, fuel_type: str, kms_driven: int):
    return lr_model.predict(pd.DataFrame([[company, model, year_of_purchase, fuel_type, kms_driven]], columns=['company', 'name', 'year', 'fuel_type', 'kms_driven']))[0]


def get_models_for_company(company: str):
    return sorted(cars[cars['company'] == company]['name'].unique())


def get_fuel_types_for_model(model: str):
    return sorted(cars[cars['name'] == model]['fuel_type'].unique())


cars = pd.read_csv("cleaned_car.csv")


def get_companies():
    return sorted(cars['company'].unique())


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
