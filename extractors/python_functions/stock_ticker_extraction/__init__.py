import requests
from itertools import compress   
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "text": "AAPL announces new iPhone",
    "spacyTokenizer": "en_core_web_sm",
}

class StockTickerExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def stock_ticker_extraction(req: StockTickerExtractionModel):
    """Stock tickers from a texts."""
    # Import tickers from bricks github repo
    req_obj = requests.get("https://raw.githubusercontent.com/code-kern-ai/bricks/main/extractors/python_functions/stock_ticker_extraction/tickers.txt")
    tickers = req_obj.text.split("\n")

    text = req.text
    is_ticker = [True if word in tickers and word.isupper() else False for word in text.replace("(", " ").replace(")", " ").replace(":", " ").split(sep=" ")]

    nlp = SpacySingleton.get_nlp(req.spacyTokenizer)
    doc = nlp(text)

    found_tickers = list(compress(text.split(), is_ticker))

    results = []
    for ticker in found_tickers:
        start = text.find(ticker)
        end = start + len(ticker)
        span = doc.char_span(start, end)
        results.append([span.text, span.start, span.end])

    return {"Tickers": results}

             

