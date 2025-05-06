from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BMIRequest(BaseModel):
    weight: float
    height: float

@app.post('/bmi')
def calculate_bmi(data : BMIRequest):

    height_in_meters = data.height / 100
    
    bmi = data.weight / (data.height_in_meters ** 2)
    return {
        'bmi': round(bmi,2),
        'category':(
            'underweight'   if bmi < 18.5 else
            'normal'        if bmi < 25 else
            'overweight'    if bmi < 30 else
            'obese' 
        )
    }

    
