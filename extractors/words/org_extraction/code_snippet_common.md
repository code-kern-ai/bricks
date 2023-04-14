```python
import spacy 

def org_extraction(text:str, extraction_keyword:str) -> List[Tuple[str,int]]:
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    org_positions = []
    for entity in doc.ents:
        if entity.label_ == "ORG":
            org_positions.append((extraction_keyword, entity.start, entity.end))
    return org_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["We are developers from Kern.ai.", "Apple is a company that sells computers.", "I really like fruit."]
    extraction_keyword = "org"
    for text in texts:
        found = org_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```