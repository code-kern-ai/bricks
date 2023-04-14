```python
import re
import spacy
from typing import List, Tuple

def noun_match_extraction(text: str) -> List[Tuple[str,int]]:
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # get noun chunks from spacy 
    nc = [i.text.lower() for i in doc.noun_chunks]
    
    word_repo = []
    noun_positions = []
    for noun_chunk in nc:
        # if noun chunk has more than one word, take first word as a target word
        if len(noun_chunk.split()) >= 2:
            target_word = noun_chunk.split()[0]

            # if target word has been used before, stop process
            if target_word in word_repo:
                pass
            else:
                # pass word to repository to avoid duplicate use
                word_repo.append(target_word)

                # create regex_pattern with target word
                pattern = rf"\W*({target_word})\W*([^\s]+)"
            
                # extract the spans of all found matches
                for item in re.finditer(pattern, text):
                    start, end = item.span()
                    span = doc.char_span(start, end, alignment_mode="expand")
                    noun_positions.append(("noun match", span.start, span.end))
    return noun_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["Leo likes tasty pizza.", "Mary loves delicious cake.", "And Moritz loves tasty bread."]
    for text in texts:
        found = noun_match_extraction(text)
        if found:
            print(f"text: \"{text}\" has  -> \"{found}\"")
        else:
            print(f"text: \"{text}\" didn't contain any noun matches.")

example_integration()
```