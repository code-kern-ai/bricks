```python
import re
from nltk.corpus import stopwords

def smalltalk_extraction(record):
    
    sw = stopwords.words("english")
    regex = re.compile(r"\".*?\"")
    smalltalk = []

    for match in regex.finditer(record["your-text"].text):
        start, end = match.span()
        span = record["your-text"].char_span(start, end)
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