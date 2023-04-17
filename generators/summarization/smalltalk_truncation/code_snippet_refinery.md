```python
import re
from nltk.corpus import stopwords

ATTRIBUTE: str = "text" #only text attributes

def smalltalk_truncation(record):
    sw = stopwords.words("english")
    regex = re.compile(r"\".*?\"")
    text = record[ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get string.

    removed_smalltalk = []
    for message in regex.findall(text):
        chat = message.replace('"','')
        chat = chat.split()
        new_text = []
        stop_words = []
        for token in chat:
            if token not in sw:
                new_text.append(token)
            else:
                stop_words.append(token)
        if (len(new_text) > 0.5*len(chat) or len(stop_words) > 8) and not len(chat) < 3:
            removed_smalltalk.append(" ".join(chat))

    return " ".join(removed_smalltalk)
```