from pydantic import BaseModel
import textstat
import re
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "text": "My cat is eleven years old. My Dad plays the saxophone. My brother mows the lawn with our lawnmower. The butterfly is colorful.",
    "syllable_threshold": 3,
    "spacyTokenizer": "en_core_web_sm"
}

class DifficultWordsExtractionModel(BaseModel):
    text: str
    syllable_threshold: int
    spacyTokenizer: str = "en_core_web_sm"
    yourLabel: str = "difficult_word"

    class Config:
        schema_extra = {
            "example": INPUT_EXAMPLE
        }


def difficult_words_extraction(request: DifficultWordsExtractionModel):
    """Extracts difficult words in a given text"""

    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)

    syllable_threshold = request.syllable_threshold
    difficult_words = textstat.difficult_words_list(text, syllable_threshold)

    pattern = "|".join(difficult_words)
    difficult_words = []
    for match in re.finditer(pattern, text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        difficult_words.append([request.yourLabel, span.start, span.end])
        
    return {f"{request.yourLabel}s": difficult_words}
