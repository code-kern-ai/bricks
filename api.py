from fastapi import FastAPI, Request
from langdetect import detect

api = FastAPI()


@api.get("/")
async def root():
    return {"message": "Hello World"}

@api.post("/language_detection/")
async def language_detection(request: Request):
    """Detect language of text
    
    Args:
        request (Request): Request object

    Returns:
        dict: Language of text
    """

    body = await request.json()
    text = body["text"]
    language = detect(text)
    return {"language": language}
