from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load JSON data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, '..', 'data.json')
with open(DATA_PATH) as f:
    students = json.load(f)

@app.get("/api")
async def get_marks(name: list[str] = Query(None)):
    name_to_marks = {entry["name"]: entry["marks"] for entry in students}
    marks = [name_to_marks.get(n, None) for n in name]
    return JSONResponse(content={"marks": marks})
