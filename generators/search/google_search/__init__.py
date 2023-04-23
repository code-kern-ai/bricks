from pydantic import BaseModel
from serpapi import GoogleSearch

INPUT_EXAMPLE = {
    "searchTerm": "code kern ai",
    "location": "Germany",
    "language": "en",
    "geoLocation": "de",
    "apiKey": "<API_KEY_GOES_HERE>",
}


class GoogleSearchModel(BaseModel):
    searchTerm: str
    location: str
    language: str
    geoLocation: str
    apiKey: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def google_search(request: GoogleSearchModel):
    """Uses google search API to retrieve search results"""

    search_term = request.searchTerm
    location = request.location
    language = request.language
    geo_location = request.geoLocation
    api_key = request.apiKey

    params = {
        "q": search_term,
        "location": location,
        "hl": language,
        "gl": geo_location,
        "google_domain": f"google.{geo_location}",
        "api_key": api_key,
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    response_url = results["organic_results"][0]["link"]
    response_snippet = results["organic_results"][0]["snippet"]

    return {"response_text": response_snippet, "URL": response_url}
