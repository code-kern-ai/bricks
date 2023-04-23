```python
import requests
import json

ATTRIBUTE: str = "texts" # only text attributes
API_KEY: str = "<API_KEY_GOES_HERE>"
MARKET: str = "en-US" # sets language, see all markets here: https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/reference/market-codes
RESPONSE_SIZE: str = "full" # choose "compact" to only get text snippet of the first result

def bing_news_search(record):
    search_url = "https://api.bing.microsoft.com/v7.0/news/search"

    headers = {"Ocp-Apim-Subscription-Key" : API_KEY}
    params  = {"q": record[ATTRIBUTE].text, "textDecorations": True, "textFormat": "HTML", "mkt": MARKET}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    if RESPONSE_SIZE == "full":
        return json.dumps(search_results) # returns full response
    elif RESPONSE_SIZE == "compact":
        return search_results["value"][0]["description"] # only returns text of first response
```