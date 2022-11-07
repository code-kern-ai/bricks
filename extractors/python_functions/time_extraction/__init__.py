from typing import Optional
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re


class TimeExtractionModel(BaseModel):
    text: str
    spacyTokenizer: Optional[str] = "en_core_web_sm"

    class Config:
        schema_extra = {
            "example": {
                "text": "Right now it is 14:40:37. Three hours ago it was 11:40 am. Two hours and twenty mins from now it will be 5PM.",
                "spacyTokenizer": "en_core_web_sm",
            }
        }


def time_extraction(request: TimeExtractionModel):
    """
    This function extracts the time from a given text. The correct date format is necessary for successful extraction.
    Valid time formats: "H am/pm/AM/PM", "HH:MM", "HH:MM:SS".
    Invalid formats: "Twelve pm"
    """
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    regex = re.compile(
        r"(?:(?:[0-9]{1,2}(?::[0-9]{1,2}(?::[0-9]{1,2}:?)?)?)(?:(?: )?am|(?: )?pm|(?: )?AM|(?: )?PM)?)"
    )

    times = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        times.append([span.start, span.end, span.text])

    return {"times": times}
