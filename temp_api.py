from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

app= FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/convert")
def convert_temperature(
    temp: float =Query(..., description='Temperature to convert'),
    to: str=Query(..., regex='^(c|f)$', description='Conversion type: c for Celsius, f for Fahrenheit'),

):

    if to=='c':
        result=(temp-32)*5/9
        unit ='Celsius'

    else:
        result =(temp*9/5)+32
        unit ='Fahrenheit'
    return {
        'input': f'{temp} degrees{input_unit}',
        'output': f'{rounds(result,2)} {unit}'
    }