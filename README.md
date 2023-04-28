## Tutorial

[https://www.youtube.com/watch?v=iRCaMnR_bpA&list=PLKnIA16_RmvY5eP91BGPa0vXUYmIdtfPQ&index=3](https://www.youtube.com/watch?v=iRCaMnR_bpA&list=PLKnIA16_RmvY5eP91BGPa0vXUYmIdtfPQ&index=3)

## Running

`uvicorn main:app --reload`

this starts the application in development mode (refreshes on code changes)

## Api

http://localhost:8000/

```
{
  "message": "Server running on port: 8000"
}
```

below endpoint gives list of all the companies

http://localhost:8000/companies

```json
[
  "Honda",
  "Mini",
  "Hindustan",
  "Skoda",
  "BMW",
  "Jeep",
  "Force",
  "Maruti",
  "Volkswagen",
  "Ford",
  "Datsun",
  "Mitsubishi",
  "Volvo",
  "Hyundai",
  "Audi",
  "Jaguar",
  "Fiat",
  "Mahindra",
  "Mercedes",
  "Tata",
  "Toyota",
  "Chevrolet",
  "Renault",
  "Land",
  "Nissan",
];
```

below endpoint gives list of all the models for company given as query param

http://localhost:8000/models?company=Datsun

```json
["Datsun GO T", "Datsun Redi GO", "Datsun Go Plus"]
```

below endpoint gives list of fuel_types available for model given as query param

http://localhost:8000/fuel_types?model=Datsun%20Redi%20GO

```json
["Petrol"]
```

below endpoint gives the estimated_price given the company, model, year_of_purchase, fuel_type, kms_driven

http://localhost:8000/predict-price?company=Datsun&model=Datsun%20Redi%20GO&year_of_purchase=2019&fuel_type=Petrol&kms_driven=4

```json
{
  "estimated_price": 279230.94513001293
}
```
