from pydantic import BaseModel
from typing import Optional
import textstat

INPUT_EXAMPLE = {"text": "Wow, this is really cool!", "language": "en"}

def setall(d, keys, value):
    for k in keys:
        d[k] = value

OUTCOMES = {}
setall(OUTCOMES, range(90, 122), "very easy")
setall(OUTCOMES, range(80, 90), "easy")
setall(OUTCOMES, range(70, 80), "fairly easy")
setall(OUTCOMES, range(60, 70), "standard")
setall(OUTCOMES, range(50, 60), "fairly difficult")
setall(OUTCOMES, range(30, 50), "difficult")
setall(OUTCOMES, range(0, 30), "very difficult")


def get_mapping_complexity(score):
    if score < 0:
        return OUTCOMES[0]
    return OUTCOMES[int(score)]


class SentenceComplexityModel(BaseModel):
    text: str
    language: Optional[str]

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def sentence_complexity(request: SentenceComplexityModel):
    """Calculate sentence complexity of a text."""

    text = request.text
    if len(text.strip()) == 0:
        return "Please provide a text input."
    else:
        language = request.language
        if language is not None:
            try:
                textstat.set_lang(language)
            except:
                print("Set language couldn't get identified. Setting to english as default.")
                textstat.set_lang("en")

        sentence_complexity_score = textstat.flesch_reading_ease(text)
        sentence_complexity = get_mapping_complexity(sentence_complexity_score)
        return {"sentenceComplexity": sentence_complexity}
