from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    name: str
    department: str
    designation: str
    salary: float
    experience: int

EMPLOYEES = [
    {
        "id": 1,
        "name": "Rahul Sharma",
        "department": "IT",
        "designation": "Software Engineer",
        "salary": 60000,
        "experience": 2
    },
    {
        "id": 2,
        "name": "Priya Verma",
        "department": "HR",
        "designation": "HR Manager",
        "salary": 70000,
        "experience": 5
    },
    {
        "id": 3,
        "name": "Mohammed Zubair",
        "department": "Data Engineering",
        "designation": "Data Engineer",
        "salary": 120000,
        "experience": 4
    }
]

# Helper Function
def find_employee(employee_id: int):
    employee = next((e for e in EMPLOYEES if e["id"] == employee_id),None)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

# Root or homepage
@app.get("/")
async def home():
    return {"message": "Welcome to Employee CRUD API"}

# Get All Employees
@app.get("/employees")
async def get_all_employees():
    return EMPLOYEES

# Get One Employee
@app.get("/employees/{employee_id}")
async def get_employee(employee_id: int):
    return find_employee(employee_id)

# Create Employee
@app.post("/employees")
async def create_employee(employee: Employee):
    new_employee = {
        "id": len(EMPLOYEES) + 1,
        "name": employee.name,
        "department": employee.department,
        "designation": employee.designation,
        "salary": employee.salary,
        "experience": employee.experience
    }
    EMPLOYEES.append(new_employee)
    return new_employee

# Update Employee
@app.put("/employees/{employee_id}")
async def update_employee(employee_id: int, updated_employee: Employee):
    employee = find_employee(employee_id)

    employee["name"] = updated_employee.name
    employee["department"] = updated_employee.department
    employee["designation"] = updated_employee.designation
    employee["salary"] = updated_employee.salary
    employee["experience"] = updated_employee.experience
    return employee

# Delete Employee
@app.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int):
    employee = find_employee(employee_id)
    EMPLOYEES.remove(employee)
    return {"message": "Employee deleted successfully"}
