```python
from bs4 import BeautifulSoup

YOUR_ATTRIBUTE = "html"

def html_cleanser(record):
    html = record[YOUR_ATTRIBUTE].text

    soup = BeautifulSoup(html, "html.parser")
    text = soup.text 

    # Remove any line breakers as well
    text = soup.text.splitlines()
    text = " ".join([w for w in text if len(w) >= 1])

    return text
```