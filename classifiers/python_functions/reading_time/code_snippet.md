```python
from typing import Dict, Any
import textstat

def fn_reading_time(record: Dict[str, Any]):
    text = record.text
    time_to_read = textstat.reading_time(text, ms_per_char=14.69)
    return time_to_read
```