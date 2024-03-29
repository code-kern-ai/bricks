```python
import textstat

ATTRIBUTE: str = "text" # only text attributes
TARGET_LANGUAGE: str = "en" # iso codes

if TARGET_LANGUAGE is not None:
    textstat.set_lang(TARGET_LANGUAGE)

def maximum_sentence_complexity(record):
    complexities = [textstat.flesch_reading_ease(sent.text) for sent in record[ATTRIBUTE].sents] 
    return get_mapping_complexity(min(complexities))

def get_mapping_complexity(score):
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
```