```python
import re
import spacy
import phonenumbers

def validate_phone_number(record):
    text = record["text"]

    regex = re.compile(r"[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}")

    valid_numbers = []
    for match in regex.finditer(text.text):
        try:
            parsed_num = phonenumbers.parse(match.group(0), None)
            if phonenumbers.is_valid_number(parsed_num):
                start, end = match.span()
                span = text.char_span(start, end)
                valid_numbers.append(["phoneNumber", span.start, span.end]) 
        except phonenumbers.phonenumberutil.NumberParseException:
            pass
    
    return {"phoneNumbers": valid_numbers}
```