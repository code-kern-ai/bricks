```python
from itertools import compress   
import requests
import spacy

# replace this list with a list containing your data
text = ["AAPL announces new iPhone", "This is our analysis on MSFT."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "ticker",
}

def stock_ticker_extraction(record):
    # import list of tickers from bricks github repo
    req = requests.get("https://raw.githubusercontent.com/code-kern-ai/bricks/main/extractors/python_functions/stock_ticker_extraction/tickers.txt")
    tickers = req.text.split("\n")

    nlp = spacy.load("en_core_web_sm")

    ticker_positions = []
    text_id = 0
    for entry in record["text"]:
        is_ticker = [True if word in tickers and word.isupper() else False for word in entry.replace("(", " ").replace(")", " ").replace(":", " ").replace(".", " ").split(sep=" ")]

        found_tickers = list(compress(entry.split(), is_ticker))

        doc = nlp(entry)
        for ticker in found_tickers:
            start = entry.find(ticker)
            end = start + len(ticker)
            span = doc.char_span(start, end, alignment_mode="expand")
            ticker_positions.append({f"text_{text_id}": [record["label"], span.start, span.end]})
        text_id += 1
    return {"extraction": ticker_positions}
```