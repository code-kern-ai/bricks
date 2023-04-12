```python
import textstat

ATTRIBUTE: str = "text" # only text attributes

def reading_time(record):
    text = record[ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string
    time_to_read = textstat.reading_time(text, ms_per_char=14.69)
    return time_to_read
```