```python
import re

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LABEL: str = "path"
YOUR_SEPARATOR: str = "/" # use "\\" for Windows paths

def filepath_extraction(record):
    text = record[YOUR_ATTRIBUTE].text # SpaCy do , hence we need to use .text to get the string.

    # Extracts the paths from the texts
    paths = [x for x in text.split() if len(x.split(YOUR_SEPARATOR)) > 1]

    # We need to add an \ before separators to use them in regex
    regex_paths = [i.replace(YOUR_SEPARATOR, "\\"+YOUR_SEPARATOR) for i in paths]
    
    for path in regex_paths:
        pattern = rf"({path})"
        match = re.search(pattern, text)

        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        
        yield YOUR_LABEL, span.start, span.end
```