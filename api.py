from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import classifiers

api = FastAPI()

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

api.include_router(classifiers.router, prefix='/classifiers')
