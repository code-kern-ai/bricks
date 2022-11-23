from pydantic import BaseModel
from better_profanity import profanity

INPUT_EXAMPLE = {
    "text": "You suck man!",
}


class ProfanityDetectionModel(BaseModel):
    text: str

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}


def profanity_detection(request: ProfanityDetectionModel):
    """Detects if a given text contains abusive language."""

    text = request.text
    result = profanity.contains_profanity(text)

    return {"profanity": result}
