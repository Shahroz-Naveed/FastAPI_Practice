from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
app = FastAPI()

class Todo(BaseModel):
    id:int
    title:str = "Any default Tilte"
    description:str

# Assignment Work
students = [{
    "id": 00 ,
    "name" : "Shahroz",
    "age" : "25",
    "grade":"A"
},{
    "id": 11 ,
    "name" : "Naveed",
    "age" : "55",
    "grade":"A"
}]

# # Get all Students from dictionary
@app.get('/students')
def get_students():
    return students
# # Get students with  id
@app.get('/students/{id}')
def getSingleStudent(id):
    return id
#  Add students
@app.post('/students/addNew')
def addStudent(id):
    students.append[(id)]
    return{
        "id":id
    }
#  Update student
@app.put('/students/update/{id}')
#  Delete student
@app.delete('/students/delete/{id}')


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