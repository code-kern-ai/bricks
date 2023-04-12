```python
import requests
import json

ATTRIBUTE: str = "text" # only text attributes
API_KEY: str = "<api-key-goes-here>" # go here for free API key https://developer.nytimes.com/
OUTPUT_SIZE: str = "full" # choose "compact" to only get the text of the first result

def nyt_news_search(record):
    query = record[ATTRIBUTE]
    key = API_KEY

    req = requests.get(f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q={query}&api-key={key}")
    search_results = req.json()

    if OUTPUT_SIZE == "full":
        return json.dumps(search_results)
    elif OUTPUT_SIZE == "compact":
        return search_results["response"]["docs"][0]["snippet"]
```