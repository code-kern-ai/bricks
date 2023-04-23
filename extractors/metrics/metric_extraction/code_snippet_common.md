```python
from quantulum3 import parser
from typing import List, Tuple

def metric_extraction(text:str, extraction_keyword:str) -> List[Tuple[str, int]]:
    """
    @param text: the input text
    @param extraction_keyword: the label that is assigned to extracted words
    @return: positions of extracted metrics
    """
    quants = parser.parse(text)

    metric_positions = []
    for quant in quants:
        span = quant.span
        metric_positions.append((extraction_keyword, span[0], span[1]))
    return metric_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["My weight is 82 kilos.", "The eifel tower is 187 meters high.", "One football field long."]
    extraction_keyword = "metric"
    for text in texts:
        found = metric_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```