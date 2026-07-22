from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    standard: str

#Default Student list
STUDENTS = [
    {'id':1, 'name':'Zubair', 'standard':'5'},
    {'id':2, 'name':'mohammed', 'standard':'6'},
    {'id':3, 'name':'Siddiqui', 'standard':'7'},
    {'id':4, 'name':'Ali', 'standard':'8'},
]

#Root or homepage
@app.get('/')
async def index():
    return {'hello':'world'}

#Create a new student
@app.post("/students")
async def create_student(student: Student):
    new_id = len(STUDENTS) + 1
    new_student = {
        "id": new_id,
        "name": student.name,
        "standard": student.standard
    }
    STUDENTS.append(new_student)
    return new_student

#Get or read a student detail with id 
@app.get('/students/{student_id}')
async def student(student_id: int):
    student = next ((b for b in STUDENTS if b['id'] == student_id), None)
    if student is None:
        # status code  404 
        raise HTTPException(status_code= 404, detail='student not found')
    return student

#Get or read list of all students
@app.get('/students/')
async def studentsall():
    return STUDENTS

@app.get('/about')
async def about():
    return {'about':'This is a student database'}
