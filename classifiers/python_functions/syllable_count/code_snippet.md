```python
from typing import Dict, Any
import textstat

def fn_syllable_count(record: Dict[str, Any]):
    text = record["text"]
    num_syllables = textstat.syllable_count(text)
    return num_syllables
```