```python
from itertools import compress   
import requests

ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "Ticker"

def stock_ticker_extraction(record):
    # Import tickers from bricks github repo
    req = requests.get("https://drive.google.com/file/d/1xw9ZA3jyzIWAkJ2NDniG2VzvPWUsM2no/view?usp=sharing")
    tickers = req.text.split("\n")

    text = record[ATTRIBUTE].text
    is_ticker = [True if word in tickers and word.isupper() else False for word in text.replace("(", " ").replace(")", " ").replace(":", " ").split(sep=" ")]

    found_tickers = list(compress(text.split(), is_ticker))

    for ticker in found_tickers:
        start = text.find(ticker)
        end = start + len(ticker)
        span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield LABEL, span.start, span.end
```