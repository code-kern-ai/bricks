```python
from typing import Dict, Any
from LeXmo import LeXmo
import nltk
nltk.download('punkt')

YOUR_ATTRIBUTE: str = "text"

def emotionality_detection(record: Dict[str, Any]):
    text = record[YOUR_ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string
    emo = LeXmo.LeXmo(text)
    emo.pop("text", None)
    emo = max(emo, key=emo.get)
    
    return emo
```