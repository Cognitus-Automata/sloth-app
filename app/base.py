from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

APP_DIR = os.path.dirname(__file__)

app = FastAPI()

app.mount('/static', StaticFiles(directory=os.path.join(APP_DIR, 'static')), name='static')

templates = Jinja2Templates(directory=os.path.join(APP_DIR, 'templates'))

@app.get('/', response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse('index.html', {'request': req,'msg': 'ASE KATW TH MPURA'})