import azure.functions as func
import datetime
import json
import logging

from app.fastapi_app import fastapp

# app = func.FunctionApp()
app = func.AsgiFunctionApp(app=fastapp, http_auth_level=func.AuthLevel.ANONYMOUS)


'''
@app.function_name("firstfunc")
@app.route("first", auth_level=func.AuthLevel.ANONYMOUS)
def trigger_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python http trigger function processed a request")
    return func.HttpResponse("first azure response", status_code=200)
'''

