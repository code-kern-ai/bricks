```python
from quantulum3 import parser
from typing import List, Tuple

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LABEL: str = "metric"

def metric_detection(record) -> List[Tuple[str, int, int]]:
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.
    
    quants = parser.parse(text)
    for quant in quants:
        span = quant.span

        yield YOUR_LABEL, span[0], span[1]
```