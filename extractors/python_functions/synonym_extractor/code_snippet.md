```python
from nltk.corpus import wordnet
import re

TARGET_WORD = "soccer"
YOUR_ATTRIBUTE = "sentences"

def synonym_extractor(record):
    # Find synonyms to a word using Wordnet
    synonyms = []
    for syn in wordnet.synsets(TARGET_WORD):
        for i in syn.lemmas():
            synonyms.append(i.name())
            
    # Word are sometimes connected by a _, which we want to remove   
    split_synonyms = [item.split(sep="_") for item in synonyms]
    combined_synonyms = [item for sublist in split_synonyms for item in sublist]

    text = record[YOUR_ATTRIBUTE].text

    # Word are sometimes connected by a _, which we want to remove   
    for word in combined_synonyms:
        try:
            pattern = rf"({word})"
            match = re.search(pattern, text)

            start, end = match.span()
            span = record[YOUR_ATTRIBUTE].char_span(start, end, alignment_mode="expand")
            yield "synonym", span.start, span.end
        except:
            pass
```