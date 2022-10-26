from fastapi import APIRouter
from .python_functions.url_extraction import fn_url_extraction, UrlExtractionModel
from .python_functions.hashtag_extraction import hash_ext, HashExtraction
from .python_functions.email_extraction import email_ext, EmailExtraction

router = APIRouter()

@router.post('/url_extraction')
def url_extraction(request: UrlExtractionModel):
    return fn_url_extraction(request)

@router.post('/hashtag_extraction')
def hash_extraction(request: HashExtraction):
    return hash_ext(request)

@router.post('/email_extraction')
def email_extraction(request: EmailExtraction):
    return email_ext(request)
