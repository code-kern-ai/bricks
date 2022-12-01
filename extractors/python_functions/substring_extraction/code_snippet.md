```python
from difflib import SequenceMatcher

YOUR_ATTRIBUTE_1: str = "originals" # only text attributes
YOUR_ATTRIBUTE_2: str = "duplicates" # only text attributes
YOUR_MIN_LEN_SUBSTRING: int = 10
YOUR_LABEL: str = "substring"

def substring_detector(record):
    """Extracts one or multiple common substrings between two strings."""

    string1 = record[YOUR_ATTRIBUTE_1].text # SpaCy doc, hence we need to use .text to get the string.
    string2 = record[YOUR_ATTRIBUTE_2].text

    duplicate = SequenceMatcher(None, string1, string2, autojunk=False).get_matching_blocks()

    for match in duplicate:
        if match.size >= YOUR_MIN_LEN_SUBSTRING:
            start, end = match.b, match.b+match.size
            span = record[YOUR_ATTRIBUTE_01].char_span(start, end, alignment_mode="expand")
            yield YOUR_LABEL, span.start, span.end
```