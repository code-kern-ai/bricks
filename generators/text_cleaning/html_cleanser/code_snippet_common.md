```python
from bs4 import BeautifulSoup

# replace this list with a list containing your data
text = ["""
            <!DOCTYPE html>
            <html>
            <body>
            <h1>Website header</h1>
            <p>
            Hello world.
            My website is live!
            </p>
            </body>
            </html>
            """]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
}

def html_cleanser(record):
    cleaned_text = []
    for entry in record["text"]:
        soup = BeautifulSoup(entry, "html.parser")
        # Remove any line breakers as well
        text = soup.text.splitlines()
        cleaned_text.append(" ".join([w for w in text if len(w) >= 1]))
    return {"cleaned_text": cleaned_text}
```