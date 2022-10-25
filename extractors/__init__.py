from fastapi import APIRouter
from .python_functions.url_extraction import fn_url_extraction, UrlExtractionModel

router = APIRouter()

@router.post('/url_extraction')
def url_extraction(request: UrlExtractionModel):
    return fn_url_extraction(request)
