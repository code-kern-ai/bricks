```python
import textstat

YOUR_ATTRIBUTE = "text"

def fn_reading_time(record):
    text = record["YOUR_ATTRIBUTE"].text # SpaCy document, hence we need to call .text to get the string
    time_to_read = textstat.reading_time(text, ms_per_char=14.69)
    return time_to_read
```