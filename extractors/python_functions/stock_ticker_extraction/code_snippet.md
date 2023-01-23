```python
from itertools import compress   
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

YOUR_ATTRIBUTE: str = "text"

def stock_ticker_extraction(record):
    """Detects phone numbers in a given text."""
    with open("tickers.txt", "r") as f:
        tickers = f.read().splitlines()

    text = req.text
    is_ticker = [True if word in tickers else False for word in text.split()]

    nlp = SpacySingleton.get_nlp(req.spacyTokenizer)
    doc = nlp(text)

    found_tickers = list(compress(text.split(), is_ticker))

    results = []
    for ticker in found_tickers:
        start = text.find(ticker)
        end = start + len(ticker)
        span = doc.char_span(start, end)
        results.append([span.text, span.start, span.end])

    return {results}
```