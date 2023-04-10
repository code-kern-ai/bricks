import re
import json
from collections import defaultdict
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "text": "You can find the new changes done to the .docx file in the document untitled_final.docx.pdf, or also in changes.pptx",
}


class FiletypeExtractionModel(BaseModel):
    text: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


# Load JSON file with all covered filetypes
with open('extractors/python_functions/filetype_extraction/file_types.json') as f:
    file_types_json = json.load(f)


def filetype_extraction(req: FiletypeExtractionModel):
    """Extracts all covered filetypes from a string using regex.
    Returns a dictionary where keys are filetypes & values are lists of matches."""
    text = req.text

    nlp = SpacySingleton.get_nlp("en_core_web_sm")
    doc = nlp(text)
    
    patterns = [re.compile(fr"(?<=\w)\{filetype}(\b)(?!\.)", re.IGNORECASE) for filetype in file_types_json]
    # covers tricky cases, like files with an extension as part of their names or extensions mentioned on their own.
    # does not check if filename is valid or if it ends with a valid character.
    
    filetypes = defaultdict(list)
    
    for pattern, filetype in zip(patterns, file_types_json):
        for match in pattern.finditer(text):
            try:
                start, end = match.span()
                span = doc.char_span(start, end, alignment_mode="expand")
            except AttributeError:
                break
            filetypes[f"{filetype[1:]}"].append([span.start, span.end])

    return filetypes