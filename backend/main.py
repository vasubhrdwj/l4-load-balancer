from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class Numbers(BaseModel):
    num1 : int
    num2 : int

@app.get("/")
def root():
    return "Server is running at port 8000"

@app.post("/add")
async def add_numbers(numbers : Numbers):
    return {"sum" : numbers.num1 + numbers.num2}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)