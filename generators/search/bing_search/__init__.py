from pydantic import BaseModel
import requests

INPUT_EXAMPLE = {
    "searchTerm": "Chattering lori",
    "apiKey": "<api-key-goes-here>",
    }

class BingSearchModel(BaseModel):
    searchTerm: str
    apiKey: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def bing_search(req: BingSearchModel):
    '''Uses Microsoft's Bing to retrieve search results.'''
    subscription_key = req.apiKey
    search_url = "https://api.bing.microsoft.com/v7.0/search"

    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    params  = {"q": req.searchTerm, "textDecorations": True, "textFormat": "HTML"}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    response_url = search_results["webPages"]["value"][0]["url"]
    response_snippet = search_results["webPages"]["value"][0]["snippet"]

    return {"response_text": response_snippet, "URL": response_url}