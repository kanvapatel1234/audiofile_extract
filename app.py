from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from test import download_mp3, download_mp4

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return FileResponse("index.html")


@app.get("/script.js")
def serve_script():
    return FileResponse("script.js")


@app.get("/download/mp3")
def get_mp3(url: str):

    try:
        file_path = download_mp3(url)

        return FileResponse(
            path=file_path,
            filename=file_path,
            media_type="audio/mpeg"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.get("/download/mp4")
def get_mp4(url: str):

    try:
        file_path = download_mp4(url)

        return FileResponse(
            path=file_path,
            filename=file_path,
            media_type="video/mp4"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )