```python
import requests
import json

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_API_KEY: str = "<api-key-goes-here>" # go here for free API key https://developer.nytimes.com/
YOUR_OUTPUT_SIZE: str = "full" # choose "compact" to only get the text of the first result

def nyt_news_search(record):
    query = record[YOUR_ATTRIBUTE]
    key = YOUR_API_KEY

    req = requests.get(f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q={query}&api-key={key}")
    search_results = req.json()

    if YOUR_OUTPUT_SIZE == "full":
        return json.dumps(search_results)
    elif YOUR_OUTPUT_SIZE == "compact":
        return search_results["response"]["docs"][0]["snippet"]
```