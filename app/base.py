from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
# from app import video
from  video2 import open_cam2

APP_DIR = os.path.dirname(__file__)

app = FastAPI()

app.mount('/static', StaticFiles(directory=os.path.join(APP_DIR, 'static')), name='static')

templates = Jinja2Templates(directory=os.path.join(APP_DIR, 'templates'))

@app.get('/', response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse('index.html', {'request': req,'msg': 'ASE KATW TH MPURA'})



import cv2

camera = cv2.VideoCapture(0)
def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.get('/video_feed')
# def video_feed():
#     return StreamingResponse(gen_frames(), media_type='multipart/x-mixed-replace; boundary=frame')

@app.get('/video_feed')
async def video_feed():
    return StreamingResponse(open_cam2(), media_type="multipart/x-mixed-replace; boundary=frame")