from fastapi import FastAPI

import classifiers

api = FastAPI()

@api.get("/")
async def root():
    return {"message": "Hello World"}

api.include_router(classifiers.router, prefix='/classifiers')
