```python
from serpapi import GoogleSearch
import json

def google_search(query:str, api_key:str, location:str="Germany", geolocation:str="de", language:str="en", response_size:str="full")->str:
    """ Search Google Search for a given query and return the results.
    @param query: The query to search with.
    @param api_key: Google API key to use.
    @param location: Google location to use.
    @param geolocation: Google geolocation to use.
    @param language: Google language to use.
    @param response_size: The size of the response. Choose "compact" to only get text snippet of the first result. "full" creates a json dump of the results.
    @return: The search results.
    """
    params = {
        "q": query,
        "location": location,
        "hl": language,
        "gl": geolocation,
        "google_domain": f"google.{geolocation}",
        "api_key": api_key,
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    
    if response_size == "full":
        return json.dumps(results) # returns full response
    elif response_size == "compact":
        return results["organic_results"][0]["snippet"] # only returns text of first response

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    queries = ["code kern ai"]
    api_key = "<API_KEY_TO_USE>" # paste your Google API key here
    for query in queries:
        print(f"Google search result for query: \"{query}\" is\n\n{google_search(query, api_key)}")

example_integration()
```