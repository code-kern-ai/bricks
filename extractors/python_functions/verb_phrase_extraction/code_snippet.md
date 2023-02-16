```python
import textacy

YOUR_ATTRIBUTE: str = "text"  # only texts allowed
YOUR_TOKENIZER: str = "en_core_web_sm" 
YOUR_LABEL: str = "verb-action"

def verb_phrase_extraction(record):
    if not record[YOUR_ATTRIBUTE] or not record[YOUR_ATTRIBUTE].text:
        return "No text string read!"
    text = record[YOUR_ATTRIBUTE].text
    patterns = [{"POS": "AUX"}, {"POS": "VERB"}]
    about_talk_doc = textacy.make_spacy_doc(
        text, lang=YOUR_TOKENIZER
    )
    verb_phrase = textacy.extract.token_matches(
        about_talk_doc, patterns=patterns
    )
    
    for chunk in verb_phrase:
        yield YOUR_LABEL, chunk.start, chunk.end
```