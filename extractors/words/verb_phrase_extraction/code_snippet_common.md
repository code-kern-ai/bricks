```python
import textacy
import spacy

def verb_phrase_extraction(text:str, extraction_keyword:str, tokenizer: str) -> List[Tuple[str,int]]:
    patterns = [{"POS": "AUX"}, {"POS": "VERB"}]
    about_talk_doc = textacy.make_spacy_doc(
        text, lang=tokenizer
    )
    verb_phrase = textacy.extract.token_matches(
        about_talk_doc, patterns=patterns
    )
    verb_phrase_positions = []
    for chunk in verb_phrase:
        verb_phrase_positions.append((extraction_keyword, chunk.start, chunk.end)) 
    return verb_phrase_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["In the next section, we will build a new model which is more accurate than the previous one."]
    extraction_keyword = "verb-action"
    tokenizer = "en_core_web_sm"
    for text in texts:
        found = verb_phrase_extraction(text, extraction_keyword, tokenizer)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```