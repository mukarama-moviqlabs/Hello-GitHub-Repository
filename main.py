#from fastapi import FastAPI

#app = FastAPI()

#@app.get("/")
#def home():
    #return {"message": "My first API is working!"}






#practise 2 
""" from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "Ayesha", "course": "CSE"},
    {"id": 2, "name": "yusra", "course": "IT"},
    {"id": 3, "name": "Sara", "course": "ECE"}
]


@app.get("/")
def home():
    return {"message": "My API is working!"}


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    return {"message": "Student not found"} """


#practise 3 pydrantic and FastApi
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    email: EmailStr


@app.get("/")
def home():
    return {"message": "Student API is working!"}


@app.post("/students")
def add_student(student: Student):
    return {
        "message": "Student registered successfully!",
        "student_details": student
    }