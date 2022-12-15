```python
import textstat

YOUR_ATTRIBUTE: str = "text"

def fn_syllable_count(record) -> int:
    text = record[YOUR_ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string
    num_syllables = textstat.syllable_count(text)
    return num_syllables
```