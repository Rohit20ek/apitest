from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
class CurrencyRequest(BaseModel):
    amount: float
    to:     str # usd or inr 

@app.post('/convert')
def convert_currency(data: CurrencyRequest):
    rate_usd_to_inr = 83.00

    if data.to == 'usd':
        result =data.amount*rate_usd_to_inr
        target = 'inr'
    elif data.to == 'usd':
        result = data.amount/rate_usd_to_inr
        target = 'usd'
    else:
        return {'error': 'invalid target currency'}

    return {
        'input':f'{data.amount} {"usd" if data.to=="inr" else "INR"}',
        'output': f'{round(result,2)} {target}'
    }