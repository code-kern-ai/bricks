from fastapi import APIRouter
from .python_functions.language_detection import LanguageDetectionModel, fn_language_detection
from .python_functions.sentence_complexity import SentenceComplexityModel, fn_sentence_complexity
from .python_functions.reading_time import ReadingTimeModel, fn_reading_time
from .python_functions.syllable_count import SyllableCountModel, fn_syllable_count
from .python_functions.levenshtein_distance import LevenshteinDistanceModel, fn_levenshtein_distance

router = APIRouter()

@router.post('/language_detection')
def language_detection(request: LanguageDetectionModel):
    return fn_language_detection(request)

@router.post('/sentence_complexity')
def sentence_complexity(request: SentenceComplexityModel):
    return fn_sentence_complexity(request)

@router.post('/reading_time')
def reading_time(request: ReadingTimeModel):
    return fn_reading_time(request)

@router.post('/syllable_count')
def syllable_count(request: SyllableCountModel):
    return fn_syllable_count(request)

@router.post('/levenshtein_distance')
def levenshtein_distance(request: SyllableCountModel):
    return fn_levenshtein_distance(request)