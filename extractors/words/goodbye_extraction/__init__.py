from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

INPUT_EXAMPLE = {
    "text": "I will leave for now since I have to cook dinner. Goodbye, and ciao to you as well!",
    "spacyTokenizer": "en_core_web_sm",
}


class GoodbyeExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"


    class Config:
        schema_extra = {
            "example": INPUT_EXAMPLE
        }


def goodbye_extraction(request: GoodbyeExtractionModel):
    """Extracts all the words associated to farewell"""

    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    regex = re.compile(r"((?:((?i)good)(?:[ ])?)?((?i)bye)|(?i)Ciao|(?:((?i)see you)(?:[ ]?)((?i)tomorrow|later|soon)?))")

    farewell = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        farewell.append(["span", span.start, span.end])

    return {"farewellWords": farewell}
