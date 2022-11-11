```python
from quantulum3 import parser

YOUR_ATTRIBUTE = "text" # choose any available attribute here

def metric_detector(record):
    text = record["text"]
    
    quants = parser.parse(text)
    for quant in quants:
        span = quant.span
        name = quant.unit.name

        yield name, span[0], span[1]
```