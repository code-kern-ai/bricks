```python
from typing import List, Tuple
from itertools import compress   
import requests
import spacy

def stock_ticker_extraction(text:str, extraction_keyword:str) -> List[Tuple[str,int]]:
    # import list of tickers from bricks github repo
    req = requests.get("https://raw.githubusercontent.com/code-kern-ai/bricks/main/extractors/python_functions/stock_ticker_extraction/tickers.txt")
    tickers = req.text.split("\n")

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    is_ticker = [True if word in tickers and word.isupper() else False for word in text.replace("(", " ").replace(")", " ").replace(":", " ").replace(".", " ").split(sep=" ")]
    found_tickers = list(compress(text.split(), is_ticker))

    ticker_positions = []
    for ticker in found_tickers:
        start = text.find(ticker)
        end = start + len(ticker)
        span = doc.char_span(start, end, alignment_mode="expand")
        ticker_positions.append((extraction_keyword, span.start, span.end))
    return ticker_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["AAPL and IBM are taking losses.", "Microsofts ticker is MSFT.", "Hot stock finance news."]
    extraction_keyword = "ticker"
    for text in texts:
        found = stock_ticker_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```