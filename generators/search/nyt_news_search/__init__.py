from pydantic import BaseModel
import requests

INPUT_EXAMPLE = {
    "query": "US election 2020.",
    "apiKey": "<API_KEY_GOES_HERE>",
}


class NytNewsSearchModel(BaseModel):
    query: str
    apiKey: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def nyt_news_search(req: NytNewsSearchModel):
    """Search for New York Times news articles."""
    query = req.query
    key = req.apiKey

    req = requests.get(
        f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q={query}&api-key={key}"
    )
    search_results = req.json()

    response_snippet = search_results["response"]["docs"][0]["snippet"]
    response_url = search_results["response"]["docs"][0]["web_url"]

    return {"response_text": response_snippet, "url": response_url}
