from pydantic import BaseModel, EmailStr

class Student(BaseModel):
    name: str
    age: int
    email: EmailStr

student = Student(
    name="Ayesha",
    age=23,
    email="ayesha@gmail.com"
)

print(student)