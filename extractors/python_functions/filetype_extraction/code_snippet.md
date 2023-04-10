import re
from collections import defaultdict


YOUR_ATTRIBUTE: str = "text" # only text attributes.
YOUR_LABEL: str = "filetypes"

with open('extractors/python_functions/filetype_extraction/file_types.json') as f:
    file_types_json = json.load(f)

def filetype_extraction(record):
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.
    
    patterns = [re.compile(fr"(?<=\w)\{filetype}(\b)(?!\.)", re.IGNORECASE) for filetype in file_types_json]
    filetypes = defaultdict(list)


    for pattern, filetype in zip(patterns, file_types_json):
        for match in pattern.finditer(text):
            try:
                start, end = match.span()
                span = record[YOUR_ATTRIBUTE].char_span(start, end, alignment_mode="expand")
            except AttributeError:
                break
            filetypes[f"{filetype[1:]}"].append([span.start, span.end])

    return filetypes
