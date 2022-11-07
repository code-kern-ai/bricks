from fastapi import APIRouter
from .python_functions import (
    language_detection,
    levenshtein_distance,
    lookup_list,
    reading_time,
    sentence_complexity,
    syllable_count,
    textblob_sentiment,
    textblob_subjectivity,
)

router = APIRouter()

@router.post('/language_detection')
def api_language_detection(request: language_detection.LanguageDetectionModel):
    return language_detection.fn_language_detection(request)

@router.post('/levenshtein_distance')
def api_levenshtein_distance(request: levenshtein_distance.LevenshteinDistanceModel):
    return levenshtein_distance.fn_levenshtein_distance(request)

@router.post('/lookup_list')
def api_lookup_list(request: lookup_list.LookupListModel):
    return lookup_list.fn_lookup_list(request)

@router.post('/reading_time')
def api_reading_time(request: reading_time.ReadingTimeModel):
    return reading_time.fn_reading_time(request)

@router.post('/sentence_complexity')
def api_sentence_complexity(request:sentence_complexity.SentenceComplexityModel):
    return sentence_complexity.fn_sentence_complexity(request)

@router.post('/syllable_count')
def api_syllable_count(request: syllable_count.SyllableCountModel):
    return syllable_count.fn_syllable_count(request)

@router.post('/textblob_sentiment')
def api_textblob_sentiment(request: textblob_sentiment.TextblobSentimentModel):
    return textblob_sentiment.fn_textblob_sentiment(request)

@router.post('/textblob_subjectivity')
def api_textblob_subjectivity(request: textblob_subjectivity.TextblobSentimentModel):
    return textblob_subjectivity.fn_textblob_subjectivity(request)
