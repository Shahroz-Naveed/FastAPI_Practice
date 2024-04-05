from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
app = FastAPI()

class Todo(BaseModel):
    id:int
    title:str = "Any default"
    description:str

# Assignment Work
students = [{
    "rollnumber": 00 ,
    "name" : "Shahroz",
    "age" : "25",
    "grade":"A"
},{
    "rollnumber": 11 ,
    "name" : "Naveed",
    "age" : "55",
    "grade":"A"
}]

# # Get all Students from dictionary
@app.get('/students')
def get_students():
    return students
# # Get students with  id
@app.get('/students/{rollnumber}')
def getfilteredStudent(rollnumber):
    print(rollnumber)
    filteredStudents = list(filter(lambda item: item[rollnumber] == students))
    return getfilteredStudent
#  Add students
@app.post('/students/addNew')
def addStudent(rollnumber,name):
    global students
    students.append({"rollnumber":int(rollnumber),"name":name})
    return "Student Created"
#  Update student
def updateStudents(students):
    if students["rollnumber"] == 11:
        return {
            "rollnumber": 11,
            "name": "updatedName"
      }
@app.put('/students/update/{rollnumber}')
def updateStudent(rollnumber,name):
    global students
    updatedStudents = list(map(updateStudents,students)) 
    print("Updated student")
    students = updateStudents
    return "Student Updated"
#  Delete student
@app.delete('/students/delete/{rollnumber}')
def deleteStudent(rollnumber,name):
    global students
    students.pop({"rollnumber":rollnumber, "name":name})
    return "Student Deleted"


# @app.get("/students")
# def sts():
#     return students
# @app.get("/")
# def helloWorld():
#     return "Hello, world!"
# @app.get("/getTodos")
# def getTodos(username:str, rollnumber:str):
#     print("Get Todos Called",username,rollnumber)
#     return "Get Todos Method " ,username + rollnumber

# @app.post("/getTodos")
# def getTodosPost():
#     print("Get Post Method Todos ")
#     return "Post getTodos Called"

# @app.get("/getSingleTodo")
# def getSingleTodo():
#     print("Get getSingleTodo Called")
#     return "getSingleTodo Called"

# @app.post("/updateTodo")
# def updateTodo():
#     return "updateTodo Called"

def start():
    uvicorn.run("todos.main:app", host= "127.0.0.1" , port= 8080, reload= True)