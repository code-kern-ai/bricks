```python
import textacy
import spacy

ATTRIBUTE: str = "text"  # only texts allowed
TOKENIZER: str = "en_core_web_sm" 
LABEL: str = "verb-action"

# replace this list with a list containing your data
text = ["In the next section, we will build a new model which is more accurate than the previous one."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "tokenizer": "en_core_web_sm",
    "label": "verb_action",
}

def verb_phrase_extraction(record):
    nlp = spacy.load(record["tokenizer"])

    verb_phrase_positions = []
    text_id = 0
    for entry in record["text"]:
        patterns = [{"POS": "AUX"}, {"POS": "VERB"}]
        about_talk_doc = textacy.make_spacy_doc(
            entry, lang=record["tokenizer"]
        )
        verb_phrase = textacy.extract.token_matches(
            about_talk_doc, patterns=patterns
        )
        
        for chunk in verb_phrase:
            verb_phrase_positions.append({f"text_{text_id}": [record["label"], chunk.start, chunk.end]}) 
        text_id += 1
    return {"extractions": verb_phrase_positions}
```