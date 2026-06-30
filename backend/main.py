from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow React (Vite dev server) to access FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

students = [
    {"id": 1, "name": "Rohan", "age": 22, "city": "Pune"},
    {"id": 2, "name": "Rahul", "age": 21, "city": "Mumbai"},
    {"id": 3, "name": "Priya", "age": 20, "city": "Nagpur"},
    {"id": 4, "name": "Sneha", "age": 23, "city": "Nashik"},
]

@app.get("/")
def home():
    return {"message": "FastAPI is Running"}

@app.get("/students")
def get_students():
    return students
