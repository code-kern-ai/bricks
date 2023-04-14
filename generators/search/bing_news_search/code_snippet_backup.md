```python
import requests
import json

# replace this list with a list containing your data
text = ["Election 2020.", "Cute cats", "Apple pie recepies."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "bing_api_key": "paste your bing api key here",
    "market": "en-US", # sets language, see all markets here: https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/reference/market-codes
    "response_size": "full" # choose "compact" to only get text snippet of the first result
}

def bing_news_search(record):
    all_results = []
    for entry in record["text"]:
        search_url = "https://api.bing.microsoft.com/v7.0/news/search"

        headers = {"Ocp-Apim-Subscription-Key" : record["bing_api_key"]}
        params  = {"q": entry, "textDecorations": True, "textFormat": "HTML", "mkt": record["market"]}

        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()

        if record["response_size"] == "full":
            all_results.append(json.dumps(search_results)) # returns full response
        elif record["response_size"] == "compact":
            all_results.append(search_results["value"][0]["description"]) # only returns text of first response
    return {"searchResults": all_results}
```