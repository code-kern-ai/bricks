```python
from itertools import compress   
import requests

YOUR_ATTRIBUTE: str = "Headline"
YOUR_LABEL: str = "Ticker"

def stock_ticker_extraction(record):
    # Import tickers from bricks github repo
    req = requests.get("https://raw.githubusercontent.com/code-kern-ai/bricks/main/extractors/python_functions/stock_ticker_extraction/tickers.txt")
    tickers = req.text.split("\n")

    text = record[YOUR_ATTRIBUTE].text
    is_ticker = [True if word in tickers and word.isupper() else False for word in text.replace("(", " ").replace(")", " ").replace(":", " ").split(sep=" ")]

    found_tickers = list(compress(text.split(), is_ticker))

    for ticker in found_tickers:
        start = text.find(ticker)
        end = start + len(ticker)
        span = record[YOUR_ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield YOUR_LABEL, span.start, span.end
```