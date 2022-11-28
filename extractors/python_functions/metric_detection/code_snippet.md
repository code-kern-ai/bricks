```python
from quantulum3 import parser

YOUR_ATTRIBUTE = "your_text" # choose any available attribute here

def metric_detection(record):
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.
    
    quants = parser.parse(text)
    for quant in quants:
        span = quant.span
        name = quant.unit.name

        yield name, span[0], span[1]
```