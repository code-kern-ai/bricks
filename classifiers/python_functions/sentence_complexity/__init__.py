from pydantic import BaseModel
from typing import Optional
import textstat

def setall(d, keys, value):
    for k in keys:
        d[k] = value

MAX_SCORE = 122
MIN_SCORE = 0

OUTCOMES = {}
setall(OUTCOMES, range(90, MAX_SCORE), "very easy")
setall(OUTCOMES, range(80, 90), "easy")
setall(OUTCOMES, range(70, 80), "fairly easy")
setall(OUTCOMES, range(60, 70), "standard")
setall(OUTCOMES, range(50, 60), "fairly difficult")
setall(OUTCOMES, range(30, 50), "difficult")
setall(OUTCOMES, range(MIN_SCORE, 30), "very difficult")

def get_mapping_complexity(score):
    if score < MIN_SCORE:
        return OUTCOMES[MIN_SCORE]
    return OUTCOMES[int(score)]

class SentenceComplexityModel(BaseModel):
    text: str
    language: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "text": "Wow, this is really cool!",
                "language": "en"
            }
        }

def fn_sentence_complexity(request: SentenceComplexityModel):
    """Calculate sentence complexity of text
    
    Args:
        request (SentenceComplexityModel): schema of request body

    Returns:
        dict: Sentence complexity of text
    """

    text = request.text

    language = request.language
    if language is not None:
        textstat.set_lang(language)
    

    sentence_complexity_score = textstat.flesch_reading_ease(text)
    sentence_complexity = get_mapping_complexity(sentence_complexity_score)
    return {"sentenceComplexity": sentence_complexity}