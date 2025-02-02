from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
from pydantic import BaseModel


with open("q-vercel-python.json", "r") as file:
    students = json.load(file)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["GET"],  
    allow_headers=["*"],  
)


def get_marks(names: List[str]) -> List[int]:
    marks = []
    student_dict = {student['name']: student['marks'] for student in students}
    for name in names:
        marks.append(student_dict.get(name, "Student not found"))
    return marks

@app.get("/api")
async def get_student_marks(name: List[str]):
    marks = get_marks(name)
    return {"marks": marks}
