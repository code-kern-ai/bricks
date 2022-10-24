from fastapi import APIRouter
from .python_functions.language_detection import fn_language_detection, LanguageDetectionModel
from .python_functions.sentence_complexity import SentenceComplexityModel, fn_sentence_complexity

router = APIRouter()

@router.post('/language_detection')
def language_detection(request: LanguageDetectionModel):
    return fn_language_detection(request)

@router.post('/sentence_complexity')
def sentence_complexity(request: SentenceComplexityModel):
    return fn_sentence_complexity(request)