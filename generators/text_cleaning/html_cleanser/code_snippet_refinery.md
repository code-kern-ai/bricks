```python
from bs4 import BeautifulSoup

ATTRIBUTE: str = "text" #only text attributes

def html_cleanser(record):
    html = record[ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.

    soup = BeautifulSoup(html, "html.parser")
    # Remove any line breakers as well
    text = soup.text.splitlines()
    text = " ".join([w for w in text if len(w) >= 1])

    return text
```