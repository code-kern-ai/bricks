```python
from serpapi import GoogleSearch
import json

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LOCATION: str = "Germany"
YOUR_LANGUAGE: str = "en"
YOUR_GEOLOCATION: str = "de"
YOUR_API_KEY: str = "<API-KEY-GOES-HERE>"
YOUR_RESPONSE_SIZE: str = "full" # choose "compact" to only get text snippet of the first result

def google_search(record):
    """Uses Google search to retrieve search results, given the parameters."""
    params = {
        "q": record[YOUR_ATTRIBUTE].text,
        "location": YOUR_LOCATION,
        "hl": YOUR_LANGUAGE,
        "gl": YOUR_GEOLOCATION,
        "google_domain": f"google.{YOUR_GEOLOCATION}",
        "api_key": YOUR_API_KEY,
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    
    if YOUR_RESPONSE_SIZE == "full":
        return json.dumps(results) # returns full response
    elif YOUR_RESPONSE_SIZE == "compact":
        return results["organic_results"][0]["snippet"] # only returns text of first response
```
