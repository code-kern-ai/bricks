```python
from typing import Dict, Any
from quantulum3 import parser

def metric_extractor(request: Dict[str, Any]):
    '''Extracts units of measurement and metrics from a text.'''
    text = request["text"]
    quants = parser.parse(text)
    return quants
```