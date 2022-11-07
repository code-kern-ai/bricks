```python
from typing import Dict, Any
from langdetect import detect

def fn_language_detection(record: Dict[str, Any]) -> str:
    text = record["your-text"]
    language = detect(text)
    return language
```