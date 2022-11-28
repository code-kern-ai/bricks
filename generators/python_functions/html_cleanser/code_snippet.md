```python
from bs4 import BeautifulSoup

YOUR_ATTRIBUTE = "html" # Choose any available attribute here.

def html_cleanser(record):
    html = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.

    soup = BeautifulSoup(html, "html.parser")
    text = soup.text 

    # Remove any line breakers as well
    text = soup.text.splitlines()
    text = " ".join([w for w in text if len(w) >= 1])

    return text
```