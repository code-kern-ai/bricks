```python
import requests
import json

YOUR_ATTRIBUTE: str = "texts"
YOUR_API_KEY: str = "<API-KEY-GOES-HERE>"
YOUR_MARKET: str = "en-US" # sets language, see all markets here: https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/reference/market-codes
YOUR_RESPONSE_SIZE: str = "full" # choose "compact" to only get text snippet of the first result

def bing_search(record):
    '''Uses Microsoft's Bing to retrieve search results for news articles.'''
    search_url = "https://api.bing.microsoft.com/v7.0/news/search"

    headers = {"Ocp-Apim-Subscription-Key" : YOUR_API_KEY}
    params  = {"q": record[YOUR_ATTRIBUTE].text, "textDecorations": True, "textFormat": "HTML", "mkt": YOUR_MARKET}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    if YOUR_RESPONSE_SIZE == "full":
        return json.dumps(search_results) # returns full response
    elif YOUR_RESPONSE_SIZE == "compact":
        return search_results["value"][0]["description"] # only returns text of first response
```