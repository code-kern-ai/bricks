from fastapi import FastAPI, Request
from langdetect import detect

api = FastAPI()


@api.post("/language_detection/")
async def language_detection(request: Request):
    body = await request.json()
    text = body["text"]
    language = detect(text)
    return {"language": language}
