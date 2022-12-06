import re
from typing import Optional
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "text": "My favourite file is stored in: /usr/bin/myfavfiles/cats.png",
    "separator": "/",
    "spacyTokenizer": "en_core_web_sm",
    "yourLabel": "path"
}

class FilepathExtractionModel(BaseModel):
    text: str
    separator: Optional[str] 
    spacyTokenizer: str
    yourLabel: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def filepath_extraction(request: FilepathExtractionModel):
    """Extracts a path from a string."""

    sep = request.separator
    text = request.text
    tokenizer = request.spacyTokenizer

    nlp = SpacySingleton.get_nlp(tokenizer)
    doc = nlp(text)

    # Extracts the paths from the texts
    paths = [x for x in text.split() if len(x.split(sep)) > 1]

    # We need to add an \ before sparators to use them in regex
    regex_paths = [i.replace(sep, "\\"+sep) for i in paths]
    print(regex_paths)
    
    matches = []
    for path in regex_paths:
        pattern = rf"({path})"
        match = re.search(pattern, text)

        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")

        matches.append([request.yourLabel, span.start, span.end])
    
    return {f"{request.yourLabel}s": matches}