from typing import Optional, Union
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re


class DateExtractionModel(BaseModel):
    text: str
    spacy_tokenizer: Optional[str] = "en_core_web_sm"

    class Config:
        schema = {
            "example": {
                "text": "Today is 04.11.2022. Yesterday was 03/11/2022. Tomorrow is 05-11-2022. Day after tomorrow is 6 Nov 2022.",
                "spacy_tokenizer": "en_core_web_sm",
            }
        }

def date_extractor(request: DateExtractionModel):
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacy_tokenizer)
    doc = nlp(text)
    regex = re.compile(r"(?:[0-9]{1,2}|Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[\/\. -]{1}(?:[0-9]{1,2}|Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[,\/\. -]{1}(?:[0-9]{2,4})")

    spans = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        spans.append([span.start, span.end, span.text])

    return {"extracted dates": spans}
