from fastapi import APIRouter
from .python_functions import (
    language_detection,
    levenshtein_distance,
    reading_time,
    sentence_complexity,
    syllable_count,
)

router = APIRouter()

@router.post('/language_detection')
def api_language_detection(request: language_detection.LanguageDetectionModel):
    return language_detection.fn_language_detection(request)

@router.post('/levenshtein_distance')
def api_levenshtein_distance(request: levenshtein_distance.LevenshteinDistanceModel):
    return levenshtein_distance.fn_levenshtein_distance(request)

@router.post('/reading_time')
def api_reading_time(request: reading_time.ReadingTimeModel):
    return reading_time.fn_reading_time(request)

@router.post('/sentence_complexity')
def api_sentence_complexity(request:sentence_complexity.SentenceComplexityModel):
    return sentence_complexity.fn_sentence_complexity(request)

@router.post('/syllable_count')
def api_syllable_count(request: syllable_count.SyllableCountModel):
    return syllable_count.fn_syllable_count(request)
