from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

INPUT_EXAMPLE = {
    "text": "Today is 04.11.2022. Yesterday was 03/11/2022. Tomorrow is 05-11-2022. Day after tomorrow is 6 Nov 2022.",
    "spacyTokenizer": "en_core_web_sm",
}


class DateExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def date_extraction(request: DateExtractionModel):
    """Detects dates in a text and returns them in a list."""

    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    regex = re.compile(
        r"(?:[0-9]{1,2}|[0-9]{4}|Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[\/\. -]{1}(?:[0-9]{1,2}|Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[,\/\. -]{1}(?:[0-9]{2,4})"
    )

    dates = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        dates.append(["date", span.start, span.end])

    return {"dates": dates}
