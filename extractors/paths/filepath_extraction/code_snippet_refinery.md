```python
import re

ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "path"
SEPARATOR: str = "/" # use "\\" for Windows paths

def filepath_extraction(record):
    text = record[ATTRIBUTE].text # SpaCy do , hence we need to use .text to get the string.

    # Extracts the paths from the texts
    paths = [x for x in text.split() if len(x.split(SEPARATOR)) > 1]

    # We need to add an \ before separators to use them in regex
    regex_paths = [i.replace(SEPARATOR, "\\"+SEPARATOR) for i in paths]
    
    for path in regex_paths:
        pattern = rf"({path})"
        match = re.search(pattern, text)

        start, end = match.span()
        span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        
        yield LABEL, span.start, span.end
```