```python
from nltk.corpus import wordnet
import re

#currently only english language is supported here
#reach out to us if this should be extended for other languages

YOUR_TARGET_WORD: str = "soccer"
YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LABEL: str = "synonym"

def synonym_extraction(record):
    # Find synonyms to a word using Wordnet
    synonyms = []
    for syn in wordnet.synsets(YOUR_TARGET_WORD):
        for i in syn.lemmas():
            synonyms.append(i.name())
            
    # Word are sometimes connected by a _, which we want to remove   
    split_synonyms = [item.split(sep="_") for item in synonyms]
    combined_synonyms = [item for sublist in split_synonyms for item in sublist]

    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.

    # Word are sometimes connected by a _, which we want to remove   
    for word in combined_synonyms:
        try:
            pattern = rf"({word})"
            match = re.search(pattern, text)

            start, end = match.span()
            span = record[YOUR_ATTRIBUTE].char_span(start, end, alignment_mode="expand")
            yield YOUR_LABEL, span.start, span.end
        except:
            pass
```