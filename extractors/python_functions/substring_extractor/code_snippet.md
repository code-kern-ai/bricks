```python
from difflib import SequenceMatcher
import spacy

YOUR_ATTRIBUTE_01 = "originals"
YOUR_ATTRIBUTE_02 = "duplicates"

def substring_detector(request):
    '''Extracts one or multiple common substrings between two strings.'''

    string1 = request[YOUR_ATTRIBUTE_01].text
    string2 = request[YOUR_ATTRIBUTE_02].text

    duplicate = SequenceMatcher(None, string1, string2, autojunk=False).get_matching_blocks()

    found_substrings = []
    for match in duplicate:
        if match.size >= request.minLengthSubstring:
            start, end = match.b, match.b+match.size
            span = doc.char_span(start, end, alignment_mode="expand")
            yield "substring", span.start, span.end
```