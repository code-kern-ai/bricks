```python
import textstat

YOUR_ATTRIBUTE: str = "text"

def syllable_count(record):
    if not record[YOUR_ATTRIBUTE] or not record[YOUR_ATTRIBUTE].text:
        return "No text string read!"
    text = record[YOUR_ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string
    num_syllables = textstat.syllable_count(text)
    return num_syllables
```