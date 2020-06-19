
import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from src.components.alpr import get_plates
from src.components.models import ResponseAlpr
from src.components.error import Error


def settings():
    HOST = os.environ.get(
        'API_HOST') if 'API_HOST' in os.environ else '127.0.0.1'
    PORT = os.environ.get('API_PORT') if 'API_PORT' in os.environ else '9090'
    ORIGIN_ALLOWED = os.environ.get(
        'ORIGIN_ALLOWED') if 'ORIGIN_ALLOWED' in os.environ else '*'

    logger.info(PORT)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[ORIGIN_ALLOWED],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

 

app = FastAPI()
settings()

@app.post("/open-alpr-reconocimiento/", response_model=ResponseAlpr)
async def identify_controller(file: UploadFile = File(...)):

    logger.info(file)
    if(file is not None):
        return get_plates(file)
    else:
        return ResponseAlpr(messsage='No se envió informacion', code=Error.NO_PLATE_FOUND.value, plates=[])


@app.get("/")
async def main():
    content = """
                <body>
                <form action="/files/" enctype="multipart/form-data" method="post">
                <input name="files" type="file" multiple>
                <input type="submit">
                </form>
                <form action="/open-alpr-reconocimiento/" enctype="multipart/form-data" method="post">
                <input name="file" type="file" multiple>
                <input type="submit">
                </form>
                </body>
                    """
    return HTMLResponse(content=content)




   