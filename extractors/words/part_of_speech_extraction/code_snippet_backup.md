```python
# expects labelling task to have labels ["ADJ", "ADP", "ADV", "AUX", "CONJ", "CCONJ", "DET", "INTJ", "NOUN", "NUM", "PART", "PRON", "PROP", "PUNCT", "SCONJ", "SYM", "VERB", "X", "SPACE"]
# replace this list with a list containing your data
import spacy 
text = ["My favourite british tea is Yorkshire tea", "Coffee is made from beans."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
}

def part_of_speech_extraction(record):
    nlp = spacy.load("en_core_web_sm")

    pos_positions = []
    text_id = 0
    for entry in record["text"]:
        doc = nlp(entry)
        for token in doc:
                pos = token.pos_
                if pos:
                    pos_positions.append({f"text_{text_id}": [pos, token.i, token.i+1]}) 
        text_id += 1    
    return {"extractions": pos_positions}
```