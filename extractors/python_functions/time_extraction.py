from typing import Optional, Union
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

class TimeExtractionModel(BaseModel):
    text: str
    spacy_tokenizer: Optional[str] = "en_core_web_sm"

def time_ext(request: TimeExtractionModel):
    """
    This function extracts the time from a given text. The correct date format is necessary for successful extraction.
    Valid time formats: "H am/pm/AM/PM", "HH:MM", "HH:MM:SS".
    Invalid formats: "Twelve pm"
    """
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacy_tokenizer)
    doc = nlp(text)
    regex = re.compile(r"(?:(?:[0-9]{1,2}(?::[0-9]{1,2}(?::[0-9]{1,2}:?)?)?)(?:(?: )?am|(?: )?pm|(?: )?AM|(?: )?PM)?)")

    spans = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        spans.append([span.start, span.end, span.text])

    return {"spans": spans}
