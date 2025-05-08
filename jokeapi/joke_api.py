from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "I used to play piano by ear, but now I use my hands.",
    "Why don't skeletons fight each other? They don't have guts!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the math book look sad? Because it had too many problems.",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
]

@app.get("/joke")

def get_joke():
    joke = random.choice(jokes)
    return {"joke": joke}
