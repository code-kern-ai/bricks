from pydantic import BaseModel
from textblob import TextBlob

INPUT_EXAMPLE = {
    "text": "His text contaisn some speling errors.",
}

class TextblobSpellingCorrectionModel(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": INPUT_EXAMPLE,
        }

def textblob_spelling_correction(request: TextblobSpellingCorrectionModel):
    """Correct spelling mistakes in a text."""

    text = request.text
    textblob_text = TextBlob(text)

    return {"correctedText": str(textblob_text.correct())}
