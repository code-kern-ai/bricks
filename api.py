from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import classifiers
import extractors
from extractors.util.spacy import download_all_models

api = FastAPI()

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
    "http://localhost",
    "http://localhost:3000",
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
            <title>Kern AI - Content Library Endpoints</title>
        </head>
        <body>
            <h1>Endpoints for the <a href="https://kern.ai" target="_blank">Kern AI</a> Content Library</h1>
            <p>Please look into the content library to see how to use these endpoints.</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200) 

api.include_router(classifiers.router, prefix='/classifiers', tags=['classifiers'])
api.include_router(extractors.router, prefix='/extractors', tags=['extractors'])

download_all_models()
