```python
import re
import phonenumbers

ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "PHONE_NUMBER"

def phone_number_extraction(record):
    regex = re.compile(r"[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}")
    text = record[ATTRIBUTE].text

    for match in regex.finditer(text):
        try:
            parsed_num = phonenumbers.parse(match.group(0), None)
            if phonenumbers.is_valid_number(parsed_num):
                start, end = match.span()
                span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
                yield LABEL, span.start, span.end
        except phonenumbers.phonenumberutil.NumberParseException:
            pass 
```