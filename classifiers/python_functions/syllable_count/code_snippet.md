```python
import textstat

YOUR_ATTRIBUTE = "text"

def fn_syllable_count(record):
    text = record[YOUR_ATTRIBUTE].text
    num_syllables = textstat.syllable_count(text)
    return num_syllables
```