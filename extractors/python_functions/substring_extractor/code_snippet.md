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
    for match in substring:
        # Only get matches that are not spaces or punctuation. Change if 
        if match.size >= 1:
            try:
                start, end = match.b, match.size
                span = record[YOUR_ATTRIBUTE].char_span(start, end, alignment_mode="expand")
                yield "duplicate", span.start, span.end
                
            # Only detects duplicates from the initial string found in duplicate string, not the other way around. 
            except:
                pass

    
```