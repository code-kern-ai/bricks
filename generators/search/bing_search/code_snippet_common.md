```python
import requests
import json

def bing_search(query:str,api_key:str,market:str="en-US",response_size:str="full")->str:
    """ Search Bing Search for a given query and return the results.
    @param query: The query to search with.
    @param api_key: The Bing API key to use.
    @param market: The market to search in. Further markets here: https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/reference/market-codes
    @param response_size: The size of the response. Choose "compact" to only get text snippet of the first result. "full" creates a json dump of the results.
    @return: The search results.
    """
    search_url = "https://api.bing.microsoft.com/v7.0/search"

    headers = {"Ocp-Apim-Subscription-Key" : api_key}
    params  = {"q": query, "textDecorations": True, "textFormat": "HTML", "mkt": market}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    if response_size == "full":
        return json.dumps(search_results)
    elif response_size == "compact":
        return search_results["value"][0]["description"]

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 
def example_integration():
    queries = ["Election 2020.", "Cute cats", "Apple pie recepies."]
    api_key = "<API_KEY_TO_USE>" # paste your Bing API key here
    for query in queries:
        print(f"Bing search result for query: \"{query}\" is\n\n{bing_search(query, api_key)}")

example_integration()
```