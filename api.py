from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import classifiers
import extractors
import generators
from extractors.util.spacy import download_all_models
from classifiers.util.nltk import download_corpora
from extractors.util.nltk import download_all_modules

api = FastAPI()

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3001",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:8000",
    "https://bricks.kern.ai",
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.get("/")
async def root():
    html_content = """
    <html>
        <head>
            <title>Kern AI - Bricks</title>
        </head>
        <body>
            <h1>Endpoints for <a href="https://kern.ai" target="_blank">Kern AI</a> bricks</h1>
            <p>Please look into bricks to see how to use these endpoints.</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


api.include_router(classifiers.router, prefix="/classifiers", tags=["classifiers"])
api.include_router(extractors.router, prefix="/extractors", tags=["extractors"])
api.include_router(generators.router, prefix="/generators", tags=["generators"])

download_all_models()
download_corpora()
download_all_modules()
