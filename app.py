from fastapi import FastAPI
from uuid import UUID

#intializing the application
app = FastAPI()

# Assignment********************

#initializing the in-memory storage
students = {}

#definig the api home directory
@app.get("/")
async def home():
    return {"message": "Students API home"}

#creating students
@app.post("/students")
def create_student(name: str, age: int, sex: str, height: float):
    student_id = str(UUID(int=len(students) + 1))

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "sex": sex,
        "height": height
    }
    students[student_id] = student
    return {"message": "Student created successfully", "data": student}

#retrieving the students data
@app.get('/students')
def get_students():
    students_data = []
    for student in students:
        students_data.append(students[student])
    return {"message": "Students retrieved successfully", "data": students_data}

#retreiving single student data from the students memory
@app.get('/students/{id}')
def single_student(id: str):
    if id in students:
        student = students[id]
        return {"mesage": "Student found", "data": student} #returns a single student data
    return {"message": "Student not found"} #prints if the id is not correct

#making changes to the students data by making an update using the PUT method
@app.put('/students/{id}')
def update_student(id: str, name: str, height: float):
    if id in students:
        new_student = students[id]
        new_student["name"] = name
        new_student["height"] = height

        return {"message": "Update made successfully", "data": new_student} #prints if the student ID exists
    return {"message": "Student does not exist or invalid ID"} #prints when a user inputs a false ID

#using the DELETE method to delete a student
@app.delete('/students/{id}')
def delete_student(id: str):
    student = students.get(id)
    if not student:
        return {"message": "Student does not exist or deleted"} #prints if the student has been deleted
    del students[id] #deletes the student with the given id
    return {"message": "Student deleted successfully"}

#THE END OF THE ASSIGNMENT