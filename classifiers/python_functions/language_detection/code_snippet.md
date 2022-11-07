```python
from typing import Dict, Any
from langdetect import detect

def fn_language_detection(record: Dict[str, Any]) -> str:
    """Detect language of text
        
    Args:
        record (Dict): one single record you want to process

    Returns:
        str: Language of your text
    """

    text = record["your-text"]
    language = detect(text)
    return language

```