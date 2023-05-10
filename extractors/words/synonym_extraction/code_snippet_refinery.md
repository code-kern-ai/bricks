```python
from nltk.corpus import wordnet
import re

TARGET_WORD: str = "soccer"
ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "synonym"

def synonym_extraction(record):
    # find synonyms to a word using Wordnet
    synonyms = []
    for syn in wordnet.synsets(TARGET_WORD):
        for i in syn.lemmas():
            synonyms.append(i.name())
            
    # word are sometimes connected by a _, which we want to remove   
    split_synonyms = [item.split(sep="_") for item in synonyms]
    combined_synonyms = [item for sublist in split_synonyms for item in sublist]

    text = record[ATTRIBUTE].text # spaCy doc, hence we need to use .text to get the string.

    # extracted words are sometimes connected by an underscore, which we want to remove   
    for word in combined_synonyms:
        try:
            pattern = rf"({word})"
            match = re.search(pattern, text)

            start, end = match.span()
            span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
            yield LABEL, span.start, span.end
        except:
            pass
```