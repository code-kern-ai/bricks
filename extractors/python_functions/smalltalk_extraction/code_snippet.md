```python
import re
from nltk.corpus import stopwords

YOUR_ATTRIBUTE = "your-text" # Choose any available attribute here

def smalltalk_extraction(record):
    sw = stopwords.words("english")
    regex = re.compile(r"\".*?\"")
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.

    smalltalk = []
    for match in regex.finditer(): 
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end)
        text_list_original = span.text.replace('"', '').replace(',', '').split()
        new_text = []
        stop_words = []
        for token in text_list_original:
            if token not in sw:
                new_text.append(token)
            else:
                stop_words.append(token)
        if len(new_text) < 0.5*len(text_list_original) or len(stop_words) < 8:
            smalltalk.append(["span.text", span.start, span.end])
    return {"smalltalk": smalltalk}
```