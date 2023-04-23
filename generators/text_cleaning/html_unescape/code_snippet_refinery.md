```python
import html

ATTRIBUTE: str = "text" #only text attributes

def html_unescape(record):
    text = record[ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.

    unescaped_text = html.unescape(text)

    return unescaped_text
```