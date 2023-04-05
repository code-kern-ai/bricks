```python
from nltk.corpus import wordnet
import re
import spacy 

# replace this list with a list containing your data
text = ["My sister is good at playing football."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "target_word": "soccer",
    "label": "synonym"
}

def synonym_extraction(record):
    nlp = spacy.load("en_core_web_sm")

    synonyms = []
    for syn in wordnet.synsets(record["target_word"]):
        for i in syn.lemmas():
            synonyms.append(i.name())
            
    # word are sometimes connected by a _, which we want to remove   
    split_synonyms = [item.split(sep="_") for item in synonyms]
    combined_synonyms = [item for sublist in split_synonyms for item in sublist]

    synonym_positions = []
    text_id = 0
    for entry in record["text"]:
        doc = nlp(entry)  
        for word in combined_synonyms:
            try:
                pattern = rf"({word})"
                match = re.search(pattern, entry)

                start, end = match.span()
                span = doc.char_span(start, end, alignment_mode="expand")
                synonym_positions.append({f"text_{text_id}": [record["label"], span.start, span.end]}) 
            except:
                pass
        text_id += 1
    return {"extractions": synonym_positions}
```