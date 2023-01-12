```python
import requests
import json

YOUR_ATTRIBUTE: str = "headline"
YOUR_API_KEY: str = "<API-KEY-GOES-HERE>"
YOUR_RESPONSE_SIZE: str = "full" # choose "compact" to only get text snippet of the first result

def bing_search(record):
    '''Uses Microsoft's Bing to retrieve search results.'''
    search_url = "https://api.bing.microsoft.com/v7.0/news/search"

    headers = {"Ocp-Apim-Subscription-Key" : req.apiKey}
    params  = {"q": req.searchTerm, "textDecorations": True, "textFormat": "HTML", "mkt": req.market}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    response_description = search_results["value"][0]["description"]
    response_url = search_results["value"][0]["url"]

    if YOUR_RESPONSE_SIZE == "full":
        return json.dumps(search_results) # returns full response
    elif YOUR_RESPONSE_SIZE == "compact":
        return response_snippet = search_results["webPages"]["value"][0]["snippet"] # only returns text of first response
```