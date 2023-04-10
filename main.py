
from fastapi import FastAPI,Request
from starlette.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn
import os

app=FastAPI()

app.mount("/static",StaticFiles(directory="static"),name="static")

templates=Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
async def get_profiles(request: Request):
    return templates.TemplateResponse("barX.html",{"request":request})

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, host='0.0.0.0',reload=True)




#uvicorn main:app --host 0.0.0.0 --port 8000 to deploy on ip adress: http://172.16.42.14:8000/