```python
import os
import re

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LABEL: str = "path"

def path_extraction(record, sep=None):
    sep = os.sep if record.sep is None else sep
    text = record[YOUR_ATTRIBUTE].text # SpaCy do , hence we need to use .text to get the string.

    # Extracts the paths from the texts
    paths = [x for x in text.split() if len(x.split(sep)) > 1]

    # We need to add an \ before sparators to use them in regex
    regex_paths = [i.replace(sep, "\\"+sep) for i in paths]
    
    for path in regex_paths:
        pattern = rf"({path})"
        match = re.search(pattern, text)

        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        
        yield YOUR_LABEL, span.start, span.end
```