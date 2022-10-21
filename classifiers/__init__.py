from fastapi import APIRouter, Request
from .language_detection import fn_language_detection
from .sentence_complexity import fn_sentence_complexity

router = APIRouter()

@router.post('/language_detection')
async def language_detection(request: Request):
    return fn_language_detection(await request.json())

@router.post('/sentence_complexity')
async def sentence_complexity(request: Request):
    return fn_sentence_complexity(await request.json())