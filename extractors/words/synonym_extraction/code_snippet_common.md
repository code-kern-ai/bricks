```python
from nltk.corpus import wordnet
import re
import spacy 
from typing import List, Tuple


def synonym_extraction(text:str, extraction_keyword:str, target_word: str) -> List[Tuple[str,int]]:
    """
    @param text: the input text
    @param extraction_keyword: the label that is assigned to extracted words
    @param target_word: the word to find synonyms to
    @return: found synonyms
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)  

    synonyms = []
    for syn in wordnet.synsets(target_word):
        for i in syn.lemmas():
            synonyms.append(i.name())
            
    # word are sometimes connected by a _, which we want to remove   
    split_synonyms = [item.split(sep="_") for item in synonyms]
    combined_synonyms = [item for sublist in split_synonyms for item in sublist]

    synonym_positions = []
    for word in combined_synonyms:
        try:
            pattern = rf"({word})"
            match = re.search(pattern, text)

            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            synonym_positions.append((extraction_keyword, span.start, span.end)) 
        except:
            pass
    return synonym_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["My sister is good at playing football.", "Japan is a country in asia."]
    extraction_keyword = "synonym"
    target_word = "soccer"
    for text in texts:
        found = synonym_extraction(text, extraction_keyword, target_word)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```