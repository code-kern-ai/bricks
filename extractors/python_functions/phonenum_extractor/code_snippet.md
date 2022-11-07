```python
import re
from typing import Dict, Optional, Any
from pydantic import BaseModel
import spacy
import phonenumbers

def validate_phone_number(request: Dict[str, Any]):
    text = request["text"]

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    regex = re.compile(r"[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}")
    regex.findall(text)

    valid_numbers = []
    for match in regex.finditer(text):
        try:
            parsed_num = phonenumbers.parse(match.group(0), None)
            if phonenumbers.is_valid_number(parsed_num):
                start, end = match.span()
                span = doc.char_span(start, end)
                valid_numbers.append([span.start, span.end, span.text]) 
        except:
            pass
    
    return {"valid_numbers": valid_numbers}
```