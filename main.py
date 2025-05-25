from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data once on startup
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)

@app.get("/api")
def get_marks(name: list[str] = []):
    name_to_marks = {student["name"]: student["marks"] for student in data}
    result = [name_to_marks.get(n, None) for n in name]
    return {"marks": result}
