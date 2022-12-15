```python
import re
from typing import List, Tuple

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LABEL: str = "url"

def url_extraction(record) -> List[Tuple[str, int, int]]:
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.
    regex_pattern = re.compile(r"(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+")

    for match in regex_pattern.finditer(text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield YOUR_LABEL, span.start, span.end
```