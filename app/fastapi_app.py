# https://github.com/pamelafox/fastapi-azure-function-apim

from fastapi import FastAPI

fastapp = FastAPI()

@fastapp.get("/")
def root():
    return {"Message": "Hello World"}
