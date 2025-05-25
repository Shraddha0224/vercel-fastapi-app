from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# CORS to allow any frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load JSON data
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)

@app.get("/")
def root():
    return {"message": "Hello from FastAPI on Vercel"}

@app.get("/api")
def get_marks(name: list[str] = []):
    name_to_marks = {student["name"]: student["marks"] for student in data}
    result = [name_to_marks.get(n, None) for n in name]
    return {"marks": result}
