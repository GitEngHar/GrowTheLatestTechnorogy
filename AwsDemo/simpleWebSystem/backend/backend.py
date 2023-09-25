import mysqlConnect as connect
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware # 追加

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   
    allow_methods=["*"],      
    allow_headers=["*"]     
)

def createTupleRespons(result):
    response = ""
    print(result)
    for i in range(len(result)):
        data = "skilltype:{0},certname:{1}".format(result[i][0],result[i][1])
        response += "{" + data + "}"
        if len(result)-1 != i : response += ","
    response = "{" + response + "}"
    return response

def createJsonResponse(result):
    print(type(result))
    data = "{0}".format(result)
    response = data.replace("[","{")
    response = response.replace("]","}")
    return response
    
class Item(BaseModel):
    skilltype: str
    certname: str

@app.get("/")
async def helthcheck():
    response = "oK"
    return response
    
@app.get("/getcert")
async def root():
    result = connect.viewDB()
    if type(result) is tuple:
        response = createTupleRespons(result)
    elif type(result) is list: 
        response = createJsonResponse(result)
    return response
    
@app.post("/regcert")
def update_item(item: Item):
    connect.regDB(item.skilltype,item.certname)
    return {"rsponse": "OK"}