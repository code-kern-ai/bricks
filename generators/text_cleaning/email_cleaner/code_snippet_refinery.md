```python
import re

ATTRIBUTE: str = "headline" #only text attributes

def email_cleaner(record):
        text = record[ATTRIBUTE].text
        text = re.sub("DISCLAIMER((\w|\s|\S))+?(?=From:|\Z)", "",text, flags=re.IGNORECASE)
        text = re.sub("EXTERNAL EMAIL.*?(?=\.)\.", "", text, re.IGNORECASE)
        text = re.sub("\[cid:image.*?(?=\])\]", "",text, re.IGNORECASE)
        text = re.sub("signature((\w|\s|\S))+?(?=From:|\Z)","",text, re.IGNORECASE)
        return text
```