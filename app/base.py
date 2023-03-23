from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
# from app import video
from video import open_cam

APP_DIR = os.path.dirname(__file__)

app = FastAPI()

app.mount('/static', StaticFiles(directory=os.path.join(APP_DIR, 'static')), name='static')

templates = Jinja2Templates(directory=os.path.join(APP_DIR, 'templates'))

@app.get('/', response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse('index.html', {'request': req,'msg': 'ASE KATW TH MPURA'})

@app.get('/video_feed')
async def video_feed():
    return StreamingResponse(open_cam(), media_type="multipart/x-mixed-replace; boundary=frame")