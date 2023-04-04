from pydantic import BaseModel
import requests

INPUT_EXAMPLE = {
    "searchTerm": "Rowan Atkinson",
    "apiKey": "<api-key-goes-here>",
    "market": "en-US"
    }

class BingNewsSearchModel(BaseModel):
    searchTerm: str
    apiKey: str
    market: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def bing_news_search(req: BingNewsSearchModel):
    '''Uses Microsoft's Bing to retrieve search results for news articles.'''
    search_url = "https://api.bing.microsoft.com/v7.0/news/search"

    headers = {"Ocp-Apim-Subscription-Key" : req.apiKey}
    params  = {"q": req.searchTerm, "textDecorations": True, "textFormat": "HTML", "mkt": req.market}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    response_description = search_results["value"][0]["description"]
    response_url = search_results["value"][0]["url"]

    return {"response_text": response_description, "URL": response_url}