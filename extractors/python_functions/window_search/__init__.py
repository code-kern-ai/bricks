from typing import Optional, List
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

class WindowSearchModel(BaseModel):
    text: str
    lookupValues: List[str]
    windowSize: int
    spacyTokenizer: Optional[str] = "en_core_web_sm"
    yourLabel: str

    class Config:
        schema_extra = {
            "example": {
                "text": "Max Mustermann decided to join Kern AI, where he wants to build great software.",
                "lookupValues": ["join", "works at", "is employed by"],
                "windowSize": 6,
                "spacyTokenizer": "en_core_web_sm",
                "yourLabel": "person"
            }
        }

def window_search(request: WindowSearchModel):
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(request.text)
    
    matches = []
    for chunk in doc.noun_chunks:
        left_bound = max(chunk.sent.start, chunk.start - (request.windowSize // 2) +1)
        right_bound = min(chunk.sent.end, chunk.end + (request.windowSize // 2) + 1)
        window_doc = doc[left_bound: right_bound]
        if any([term in window_doc.text for term in request.lookupValues]):
            matches.append([request.yourLabel, chunk.start, chunk.end])

    return {f"{request.yourLabel}s": matches}
