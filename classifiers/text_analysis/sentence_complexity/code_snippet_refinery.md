```python
import textstat

ATTRIBUTE: str = "text" # only text attributes
TARGET_LANGUAGE: str = "en" # iso codes

def sentence_complexity(record):
    text = record[ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string
    sentence_complexity_score = textstat.flesch_reading_ease(text)
    return lookup_label(sentence_complexity_score)

def lookup_label(score:int) -> str:
    if score < 30:
        return "very difficult"
    if score < 50:
        return "difficult"
    if score < 60:
        return "fairly difficult"
    if score < 70:
        return "standard"
    if score < 80:
        return "fairly easy"
    if score < 90:
        return "easy"        
    return "very easy"

if TARGET_LANGUAGE is not None:
    textstat.set_lang(TARGET_LANGUAGE)

```