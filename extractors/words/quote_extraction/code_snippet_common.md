```python
import re
import spacy

def quote_extraction(text:str, extraction_keyword:str) -> List[Tuple[str,int]]:
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    regex = re.compile(r"\".*?\"|\'.*?\'")

    quote_positions = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        quote_positions.append((extraction_keyword, span.start, span.end))

    return quote_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ['''"Hello, Nick," said Harry.
            "Hello, hello," said Nearly Headless Nick, starting and looking round. He wore a dashing, plumed hat on his long curly hair, and a tunic with a ruff, which concealed the fact that his neck was almost completely severed. He was pale as smoke, and Harry could see right through him to the dark sky and torrential rain outside.
            "You look troubled, young Potter," said Nick, folding a transparent letter as he spoke and tucking it inside his doublet.
            "So do you," said Harry.''']
    extraction_keyword = "quote"
    for text in texts:
        found = quote_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```