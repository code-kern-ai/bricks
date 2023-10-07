from pydantic import BaseModel
from langdetect import detect, DetectorFactory, LangDetectException

DetectorFactory.seed = 0

INPUT_EXAMPLE = {"text": "This is an english sentence."}


class LanguageDetectionModel(BaseModel):
    text: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def language_detection(request: LanguageDetectionModel):
    """Detects the language of a given text."""

    text = request.text
    if not text or not text.strip():
        return {"language": "unknown"}
    return {"language": detect(text)}
