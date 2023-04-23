```python
import re
from nltk.corpus import stopwords

# currently only english language is supported here
# reach out to us if you would like to request other languages to be supported

ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "smalltalk"

def smalltalk_extraction(record):
    sw = stopwords.words("english")
    regex = re.compile(r"\".*?\"")
    text = record[ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.

    for match in regex.finditer(text): 
        start, end = match.span()
        span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        text_list_original = span.text.replace('"', '').replace(',', '').split()
        new_text = []
        stop_words = []
        for token in text_list_original:
            if token not in sw:
                new_text.append(token)
            else:
                stop_words.append(token)
        if len(new_text) < 0.5*len(text_list_original) or len(stop_words) < 8:
            yield LABEL, span.start, span.end
        else:
            pass
```