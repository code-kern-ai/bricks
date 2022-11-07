from pydantic import BaseModel
import textstat

INPUT_EXAMPLE = {"text": "This sentence has 7 syllables."}


class SyllableCountModel(BaseModel):
    text: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def syllable_count(request: SyllableCountModel):
    """Counts the number of sylabbles in a text."""
    text = request.text
    syllables = textstat.syllable_count(text)
    return {"syllableCount": syllables}
