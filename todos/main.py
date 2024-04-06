from fastapi import FastAPI,Path,Query
import uvicorn
from pydantic import BaseModel,Field
from typing import Union,Optional,Annotated
app = FastAPI()

class Todo(BaseModel):
    id:int 
    title:str = "Any default"
    description:str

class User(BaseModel):
    username:str = Field(max_length=10)
# Assignment Work
# students = [{
#     "rollnumber": 00 ,
#     "name" : "Shahroz",
#     "age" : "25",
#     "grade":"A"
# },{
#     "rollnumber": 11 ,
#     "name" : "Naveed",
#     "age" : "55",
#     "grade":"A"
# }]

# # # Get all Students from dictionary
# @app.get('/students')
# def get_students():
#     return students
# # # Get students with  id
# @app.get('/students/{rollnumber}')
# def getfilteredStudent(rollnumber):
#     print(rollnumber)
#     filteredStudents = list(filter(lambda item: item[rollnumber] == students))
#     return getfilteredStudent
# #  Add students
# @app.post('/students/addNew')
# def addStudent(rollnumber,name):
#     global students
#     students.append({"rollnumber":int(rollnumber),"name":name})
#     return "Student Created"
# #  Update student
# def updateStudents(students):
#     if students["rollnumber"] == 11:
#         return {
#             "rollnumber": 11,
#             "name": "updatedName"
#       }
# @app.put('/students/update/{rollnumber}')
# def updateStudent(rollnumber,name):
#     global students
#     updatedStudents = list(map(updateStudents,students)) 
#     print("Updated student")
#     students = updateStudents
#     return "Student Updated"
# #  Delete student
# @app.delete('/students/delete/{rollnumber}')
# def deleteStudent(rollnumber,name):
#     global students
#     students.pop({"rollnumber":rollnumber, "name":name})
#     return "Student Deleted"


# # @app.get("/students")
# # def sts():
# #     return students
# # @app.get("/")
# # def helloWorld():
# #     return "Hello, world!"
# # @app.get("/getTodos")
# # def getTodos(username:str, rollnumber:str):
# #     print("Get Todos Called",username,rollnumber)
# #     return "Get Todos Method " ,username + rollnumber

# # @app.post("/getTodos")
# # def getTodosPost():
# #     print("Get Post Method Todos ")
# #     return "Post getTodos Called"

# # @app.get("/getSingleTodo")
# # def getSingleTodo():
# #     print("Get getSingleTodo Called")
# #     return "getSingleTodo Called"

# # @app.post("/updateTodo")
# # def updateTodo():
# #     return "updateTodo Called"

### Pydantic Modal || Annotated 
userName:Annotated[str,Path(ge=10)]  = "Shahroz Naveed"
age:int = 25
listOfUserNames:list[str] = ["Name1", "Name2","Name3"]
## Here we use pydantic class model for custom types in dictionary
car:Todo = {

    "id":2525,
    "title":"seaBlue",
    "description": "1st Batch Model"
}
def getName(firstName:Optional[str],Lastname:str):#str | None = None
    return firstName + " " + Lastname
## Practicing Adavance Query and Path Parameter
## Use of Body parameter

# def MainRoute(todos:Todo):
#     return todos
@app.get('/')
def MarinRoute(item: Annotated[str,Query(max_length=10,min_length=6,pattern="^fix[a-zA-Z0-9)]")]):
             return item  
## Practice Path parameter and validation on it
@app.get('/todos/{id}') 
def MainRoute(id:Annotated[int,Path(ge=0,le=100)]):
      return id   
## Practicing Body Parameter with multiple paremeters
@app.get('/students') 
def MainRoute(todos:Todo,users:User):
      print(users)
      return todos          
def start():
    uvicorn.run("todos.main:app", host= "127.0.0.1" , port= 8080, reload= True)