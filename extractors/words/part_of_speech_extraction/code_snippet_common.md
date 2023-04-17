```python
import spacy 
from typing import List, Tuple

def part_of_speech_extraction(text:str) -> List[Tuple[str,int]]:
    """
    @param text: the input text
    @return: POS tag positions
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    pos_positions = []
    for token in doc:
            pos = token.pos_
            if pos:
                pos_positions.append((pos, token.i, token.i+1))  
    return pos_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["My favourite british tea is Yorkshire tea", "Coffee is made from beans."]
    for text in texts:
        found = part_of_speech_extraction(text)
        print(f"text: \"{text}\" has -> \"{found}\"")

example_integration()
```