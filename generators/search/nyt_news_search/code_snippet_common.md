```python
import requests
import json

# replace this list with a list containing your data
text = ["US election 2020."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "nyt_api_key": "paste your NYT API key here", # go here for free API key https://developer.nytimes.com/
    "output_size": "full", # choose "compact" to only get the text of the first result
}

def nyt_news_search(record):
    search_results = []
    for entry in record["text"]:
        req = requests.get(f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q={entry}&api-key={record["nyt_api_key"]}")
        search_results = req.json()

        if record["output_size"] == "full":
            search_results.append(json.dumps(search_results))
        elif record["output_size"] == "compact":
            search_results.append(search_results["response"]["docs"][0]["snippet"])
    return {"nytResults": search_results}
```