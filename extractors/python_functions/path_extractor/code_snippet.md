```python
import os
from typing import Dict, Any

def get_paths(request: Dict[str, Any]):
    text = request["text"]
    sep = os.sep if request["sep"] is None else request["sep"]
    return [x for x in text.split() if len(x.split(sep)) > 1]
```