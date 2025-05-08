from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random as rand 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

secret_number = rand.randint(1,100)

@app.get("/guess")

def guess_number(guess: int):
    global secret_number

    if guess < secret_number:
        return{"message": "Your guess is too low!"}
    elif guess > secret_number:
        return{"message": "Your guess is too high!"}
    else:
        secret_number =rand.randint(1,100)
        return{"message": "Congratulations! You guessed the number! TRY AGAIN"}
