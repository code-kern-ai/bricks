```python
from difflib import SequenceMatcher

YOUR_ATTRIBUTE_01 = "originals" # Choose any available attributes here.
YOUR_ATTRIBUTE_02 = "duplicates"
MIN_LEN_SUBSTRING = 10

def substring_detector(request):
    '''Extracts one or multiple common substrings between two strings.'''

    string1 = request[YOUR_ATTRIBUTE_01].text # SpaCy doc, hence we need to use .text to get the string.
    string2 = request[YOUR_ATTRIBUTE_02].text

    duplicate = SequenceMatcher(None, string1, string2, autojunk=False).get_matching_blocks()

    found_substrings = []
    for match in duplicate:
        if match.size >= MIN_LEN_SUBSTRING:
            start, end = match.b, match.b+match.size
            span = doc.char_span(start, end, alignment_mode="expand")
            yield "substring", span.start, span.end
```