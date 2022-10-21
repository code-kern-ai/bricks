from fastapi import APIRouter, Request
from .language_detection import fn_language_detection

router = APIRouter()

@router.post('/language_detection')
async def language_detection(request: Request):
    """Detect language of text

    Args:
        request (Request): request body

    Returns:
        dict: Language of text
    """
    return fn_language_detection(await request.json())