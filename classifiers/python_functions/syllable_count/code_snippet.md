```python
from typing import Dict, Any
import textstat

def fn_syllable_count(record: Dict[str, Any]):
    text = record["text]
    syllables = textstat.syllable_count(text)
    return {"time": syllables}
```