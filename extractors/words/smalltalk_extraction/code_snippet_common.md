```python
import re
from nltk.corpus import stopwords
import spacy

def smalltalk_extraction(text:str, extraction_keyword:str) -> List[Tuple[str,int]]:
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    sw = stopwords.words("english")
    regex = re.compile(r"\".*?\"")

    smalltalk_positions = []
    for match in regex.finditer(text): 
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
            smalltalk_positions.append((extraction_keyword, span.start, span.end))
    return smalltalk_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ['''"Hello, how are you?" he asked.
            "I am doing fine, and you?", she said.
            "I am doing good as well.".
            "Listen, I wanted to talk to you about the something. Actually your car broke down on the bridge and I 
            suspect that the engine is heated up.".
            "Don't worry about that, I'll buy a new car!"''']
    extraction_keyword = "smalltalk"
    for text in texts:
        found = smalltalk_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```