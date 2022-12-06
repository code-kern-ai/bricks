from pydantic import BaseModel
from typing import Optional
from difflib import SequenceMatcher
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "text": "Hello this is my flat. This is a duplicate.", 
    "substring": "This is a duplicate.",
    "spacyTokenizer": "en_core_web_sm"
}

class SubstringExtractionModel(BaseModel):
    text: str
    substring: str
    spacyTokenizer: Optional[str] = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def substring_extraction(req: SubstringExtractionModel):
    """Extracts a common substring between two strings."""

    string1 = req.text # SpaCy doc, hence we need to use .text to get the string.
    string2 = req.substring

    start_index = string1.find(string2)
    end_index = start_index + len(string2)

    nlp = SpacySingleton.get_nlp(req.spacyTokenizer)
    doc = nlp(string1)

    if start_index != -1:
        span = doc.char_span(start_index, end_index, alignment_mode="expand")
        return {"Substring": [span.start, span.end]}
    else:
        return "No substring found!"
