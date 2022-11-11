```python
import os
import re

YOUR_ATTRIBUTE = "details" # choose any available attribute here
YOUR_LABEL = "path"

def path_extractor(record, sep=None):
    sep = os.sep if record.sep is None else sep
    text = record[YOUR_ATTRIBUTE].text

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
        span = record[YOUR_ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        
        yield YOUR_LABEL, span.start, span.end
```