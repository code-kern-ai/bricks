```python
import re
import spacy
import phonenumbers

YOUR_ATTRIBUTE = "your-text"

def validate_phone_number(record):
    regex = re.compile(r"[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}")
    text = record[YOUR_ATTRIBUTE].text

    valid_numbers = []
    for match in regex.finditer(text):
        try:
            parsed_num = phonenumbers.parse(match.group(0), None)
            if phonenumbers.is_valid_number(parsed_num):
                start, end = match.span()
                span = record[YOUR_ATTRIBUTE].char_span(start, end)
                valid_numbers.append(["phoneNumber", span.start, span.end]) 
        except phonenumbers.phonenumberutil.NumberParseException:
            pass
    
    return valid_numbers
```