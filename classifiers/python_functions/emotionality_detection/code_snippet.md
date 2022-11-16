```python
from typing import Dict, Any
import nltk
nltk.download('punkt')
from LeXmo import LeXmo

def emotionality_detection(record: Dict[str, Any]):
    text = record["text-attribute"]
    emo = LeXmo.LeXmo(text)
    emo.pop("text", None)
    emo = max(emo, key=emo.get)
    
    return {"emotions": emo}
```