from pydantic import BaseModel
import textstat

INPUT_EXAMPLE = {
    "text": "My cat is eleven years old. My Dad plays the saxophone. My brother mows the lawn with our lawnmower. The butterfly is colorful.",
    "syllable_threshold": 3
}

class DifficultWordsExtractionModel(BaseModel):
    text: str
    syllable_threshold: int

    class Config:
        schema_extra = {
            "example": INPUT_EXAMPLE
        }


def difficult_words_extraction(request: DifficultWordsExtractionModel):
    """Extracts difficult words in a given text"""

    text = request.text
    syllable_threshold = request.syllable_threshold
    difficult_words = textstat.difficult_words_list(text, syllable_threshold)
    return {"difficult_words": difficult_words}