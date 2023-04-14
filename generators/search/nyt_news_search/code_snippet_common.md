```python
import requests
import json


def nyt_news_search(query:str,api_key:str,response_size:str="full")->str:
    """ Search Google Search for a given query and return the results.
    @param query: The query to search with.
    @param api_key: New York times API key to use.
    @param response_size: The size of the response. Choose "compact" to only get text snippet of the first result. "full" creates a json dump of the results.
    @return: The search results.
    """
    req = requests.get(f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q={query}&api-key={api_key}")
    search_results = req.json()

    if response_size == "full":
        return json.dumps(search_results)
    elif response_size == "compact":
        return search_results["response"]["docs"][0]["snippet"]
# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 
def example_integration():
    queries = ["US election 2020"]
    api_key = "<API_KEY_TO_USE>" # paste your NYT API key here
    for query in queries:
        print(f"New York times search result for query: \"{query}\" is\n\n{nyt_news_search(query, api_key)}")

example_integration()
```