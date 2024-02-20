from fastapi import FastAPI

from uuid import UUID


app = FastAPI()

students = {}


students_data = {"id": 0, "name": "", "age": "", "sex": 0, "height": 0.0}


@app.get("/")
def home():
    return {"message": "Hello from the Students API"}


@app.get("/students") 
def get_students():
    return students



@app.get("/students/{id}")
def get_student_by_id(id: str):
    student = students.get(id)
    if not student:
        return {"error": "student not found"}

    return student


@app.post("/students")
def add_student(
    name: str, age: int, sex: str, height: float
):  
    new_student = students_data.copy()
    new_student["id"] = str(UUID(int=len(students) + 1))
    new_student["name"] = name
    new_student["age"] = age
    new_student["sex"] = sex
    new_student["height"] = height

    students[new_student["id"]] = new_student

    return {"message": "student added successfully", "data": new_student}


@app.put("/students/{id}") 
def update_student(
    id: str, name: str, age: int,sex:str, height: float):
    student = students.get(id)
    if not student:
     return {"error": "student not found"}
    
    student["name"]=name
    student["age"] = age
    student["sex"] = sex
    student["height"] = height


    return {"message": "student updated successfully", "data": student}
print('student')



@app.delete("/students/{id}")
def delete_student(id: str):
    book = students.get(id)
    if not book:
        return {"error": "student not found"}

    del students[id]

    return {"message": "student deleted successfully"}
