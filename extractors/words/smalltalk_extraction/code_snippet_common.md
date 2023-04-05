```python
import re
from nltk.corpus import stopwords
import spacy

# replace this list with a list containing your data
text = ['''"Hello, how are you?" he asked.
            "I am doing fine, and you?", she said.
            "I am doing good as well.".
            "Listen, I wanted to talk to you about the something. Actually your car broke down on the bridge and I 
            suspect that the engine is heated up.".
            "Don't worry about that, I'll buy a new car!"''']

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "smalltalk",
}

def smalltalk_extraction(record):
    nlp = spacy.load("en_core_web_sm")
    sw = stopwords.words("english")
    regex = re.compile(r"\".*?\"")

    smalltalk_positions = []
    text_id = 0
    for entry in record["text"]:
        doc = nlp(entry)
        for match in regex.finditer(entry): 
            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            text_list_original = span.text.replace('"', '').replace(',', '').split()
            new_text = []
            stop_words = []
            for token in text_list_original:
                if token not in sw:
                    new_text.append(token)
                else:
                    stop_words.append(token)
            if len(new_text) < 0.5*len(text_list_original) or len(stop_words) < 8:
                smalltalk_positions.append({"extraction": [record["label"], span.start, span.end]})
        text_id += 1
    return {"extractions": smalltalk_positions}
```