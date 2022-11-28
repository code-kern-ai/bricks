```python
from typing import Dict, Any
from LeXmo import LeXmo
import nltk
nltk.download('punkt')

YOUR_ATTRIBUTE = "text-attribute"

def emotionality_detection(record: Dict[str, Any]):
    text = record[YOUR_ATTRIBUTE].text
    emo = LeXmo.LeXmo(text)
    emo.pop("text", None)
    emo = max(emo, key=emo.get)
    
    return {"emotions": emo}
```