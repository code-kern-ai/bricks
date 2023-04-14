```python
from serpapi import GoogleSearch
import json

# replace this list with a list containing your data
text = ["code kern ai."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "location": "Germany",
    "language": "en",
    "geolocation": "de",
    "api_key": "paste your api key here!",
    "response_size": "full",
}

def google_search(record):
    search_results = []
    for entry in record["text"]:
        params = {
            "q": entry,
            "location": record["location"],
            "hl": record["language"],
            "gl": record["geolocation"],
            "google_domain": f"google.{record['geolocation']}",
            "api_key": record["api_key"],
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        
        if record["response_size"] == "full":
            search_results.append(json.dumps(results)) # returns full response
        elif record["response_size"] == "compact":
            search_results.append(results["organic_results"][0]["snippet"]) # only returns text of first response
    return {"searchResults": search_results}
```