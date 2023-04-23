```python
from quantulum3 import parser

ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "metric"

def metric_extraction(record):
    text = record[ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.
    
    quants = parser.parse(text)
    for quant in quants:
        span = quant.span

        yield LABEL, span[0], span[1]
```