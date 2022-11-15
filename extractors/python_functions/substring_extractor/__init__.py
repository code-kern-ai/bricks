from pydantic import BaseModel
from typing import Optional
from difflib import SequenceMatcher
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "textInitial": "Hello this is my house. This is not a duplicate. It's good to see you.", 
    "textDuplicate": "Hello this is my flat. This is a duplicate. It's good to see you.",
    "minLengthSubstring": 10,
    "spacyTokenizer": "en_core_web_sm"
}

class SubstringExtractorModel(BaseModel):
    textInitial: str
    textDuplicate: str
    minLengthSubstring: int
    spacyTokenizer: Optional[str] = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def substring_extractor(request: SubstringExtractorModel):
    '''Extracts one or multiple substring found between two strings.'''

    string1 = request.textInitial
    string2 = request.textDuplicate

    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(string2)

    duplicate = SequenceMatcher(None, string1, string2, autojunk=False).get_matching_blocks()

    found_duplicates = []
    for match in duplicate:
        if match.size >= request.minLengthSubstring:
            start, end = match.b, match.b+match.size
            span = doc.char_span(start, end, alignment_mode="expand")
            found_duplicates.append(["substring", span.start, span.end])

    return {"substrings": found_duplicates}
