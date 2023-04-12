```python
import textacy

ATTRIBUTE: str = "text"  # only texts allowed
TOKENIZER: str = "en_core_web_sm" 
LABEL: str = "verb-action"

def verb_phrase_extraction(record):
    text = record[ATTRIBUTE].text
    patterns = [{"POS": "AUX"}, {"POS": "VERB"}]
    about_talk_doc = textacy.make_spacy_doc(
        text, lang=TOKENIZER
    )
    verb_phrase = textacy.extract.token_matches(
        about_talk_doc, patterns=patterns
    )
    
    for chunk in verb_phrase:
        yield LABEL, chunk.start, chunk.end
```