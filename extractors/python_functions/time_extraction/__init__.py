from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

INPUT_EXAMPLE = {
    "text": "Right now it is 14:40:37. Three hours ago it was 11:40 am. Two hours and twenty mins from now it will be 5PM.",
    "spacyTokenizer": "en_core_web_sm",
}


class TimeExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def time_extraction(request: TimeExtractionModel):
    """Extracts times from a given text."""
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    regex = re.compile(
        r"\b(1[0-2]|[1-9])\s*[apAP][. ]*[mM]\.?|(?:(?:[01]?[0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?(?:(?:\s?[ap](?:\.m\.)?)|(?:\s?[AP](?:\.M\.)?)))|(?:[01]?[0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?"
    )

    times = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        times.append(["time", span.start, span.end])

    return {"times": times}
