from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/age')
def calculate_age(
    dob: str = Query(None, description='your date of birth in YYYY-MM-DD format', min_length=10, max_length=10,regex='^\d{4}-\d{2}-\d{2}$')

):
    if not dob:
        return{'error': 'date of birth is required in YYYY-MM-DD format'}
    

    try:
        birth_date=datetime.strptime(dob,'%Y-%m-%d')
    except ValueError:
        return{'error': 'invalid date format! use yyyy-mm-dd'}

    today = datetime.today()
    age = today.year - birth_date.year - (
        (today.month,today.day)<(birth_date.month, birth_date.day)
    )

    return{
        'date_of_birth': dob,
        'age': age,
        
 }