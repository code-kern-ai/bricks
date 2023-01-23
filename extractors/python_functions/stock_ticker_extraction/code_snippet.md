```python
from itertools import compress   
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

YOUR_ATTRIBUTE: str = "text"
YOUR_LABEL: str = "symbol

def stock_ticker_extraction(record):
    with open("tickers.txt", "r") as f:
        tickers = f.read().splitlines()

    text = record[YOUR_ATTRIBUTE].text
    is_ticker = [True if word in tickers else False for word in text.split()]

    nlp = SpacySingleton.get_nlp(req.spacyTokenizer)
    doc = nlp(text)

    found_tickers = list(compress(text.split(), is_ticker))

    for ticker in found_tickers:
        start = text.find(ticker)
        end = start + len(ticker)
        span = doc.char_span(start, end)
        yield YOUR_LABEL, span.start, span.end
```