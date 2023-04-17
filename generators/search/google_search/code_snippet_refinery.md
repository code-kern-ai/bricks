```python
from serpapi import GoogleSearch
import json

ATTRIBUTE: str = "text" # only text attributes
LOCATION: str = "Germany"
LANGUAGE: str = "en"
GEOLOCATION: str = "de"
API_KEY: str = "<API_KEY_GOES_HERE>"
RESPONSE_SIZE: str = "full" # choose "compact" to only get text snippet of the first result

def google_search(record):
    """Uses Google search to retrieve search results, given the parameters."""
    params = {
        "q": record[ATTRIBUTE].text,
        "location": LOCATION,
        "hl": LANGUAGE,
        "gl": GEOLOCATION,
        "google_domain": f"google.{GEOLOCATION}",
        "api_key": API_KEY,
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    
    if RESPONSE_SIZE == "full":
        return json.dumps(results) # returns full response
    elif RESPONSE_SIZE == "compact":
        return results["organic_results"][0]["snippet"] # only returns text of first response
```
