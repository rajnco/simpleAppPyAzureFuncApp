# https://github.com/pamelafox/fastapi-azure-function-apim

from fastapi import FastAPI

fastapp = FastAPI()

@fastapp.get("")
def root():
    return {"Message": "Hello World - Azure"}

@fastapp.get("/")
def doc_root():
    return {"Message": "Hello World - Doc Root - Azure"}
