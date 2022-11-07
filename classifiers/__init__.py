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


@router.post(f"/{language_detection.language_detection.__name__.lower()}")
def api_language_detection(request: language_detection.LanguageDetectionModel):
    return language_detection.language_detection(request)


@router.post(f"/{levenshtein_distance.levenshtein_distance.__name__.lower()}")
def api_levenshtein_distance(request: levenshtein_distance.LevenshteinDistanceModel):
    return levenshtein_distance.levenshtein_distance(request)


@router.post(f"/{lookup_list.lookup_list.__name__.lower()}")
def api_lookup_list(request: lookup_list.LookupListModel):
    return lookup_list.lookup_list(request)


@router.post(f"/{reading_time.reading_time.__name__.lower()}")
def api_reading_time(request: reading_time.ReadingTimeModel):
    return reading_time.reading_time(request)


@router.post(f"/{sentence_complexity.sentence_complexity.__name__.lower()}")
def api_sentence_complexity(request: sentence_complexity.SentenceComplexityModel):
    return sentence_complexity.sentence_complexity(request)


@router.post(f"/{syllable_count.syllable_count.__name__.lower()}")
def api_syllable_count(request: syllable_count.SyllableCountModel):
    return syllable_count.syllable_count(request)


@router.post(f"/{textblob_sentiment.textblob_sentiment.__name__.lower()}")
def api_textblob_sentiment(request: textblob_sentiment.TextblobSentimentModel):
    return textblob_sentiment.textblob_sentiment(request)


@router.post(f"/{textblob_subjectivity.textblob_subjectivity.__name__.lower()}")
def api_textblob_subjectivity(request: textblob_subjectivity.TextblobSentimentModel):
    return textblob_subjectivity.textblob_subjectivity(request)
