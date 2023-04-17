
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

INPUT_EXAMPLE = {
    "text": "percentages 110% are found -.5% at 42,13% positions 1, 5 and 8",
    "spacyTokenizer": "en_core_web_sm",
}


class PercentageExtractionModel(BaseModel):
    text: str
    regex: str = r"(-?\d+(?:[.,]\d*)?|-?[.,]\d+)%"
    spacyTokenizer: str = "en_core_web_sm"
    yourLabel: str = "percentage"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def percentage_extraction(request: PercentageExtractionModel):
    """Extracts percentages from a given text."""
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(request.text)

    matches = []

    def regex_search(pattern, string):
        """
        some helper function to easily iterate over regex matches
        """
        prev_end = 0
        while True:
            match = re.search(pattern, string)
            if not match:
                break

            start, end = match.span()
            yield start + prev_end, end + prev_end

            prev_end += end
            string = string[end:]

    for start, end in regex_search(request.regex, request.text):
        span = doc.char_span(start, end, alignment_mode="expand")
        matches.append([request.yourLabel, span.start, span.end])

    return {f"{request.yourLabel}s": matches}