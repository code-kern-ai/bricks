```python
import requests

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_API_KEY: str = "<API_KEY_GOES_HERE"
YOUR_LANGUAGE: str = "en-US" # en-GB, de-DE, fr-FR, it-IT, zh-CN, ja-JP

def bing_spelling_check(record):
    '''Uses Microsoft's Bing to retrieve search results.'''

    text = record[YOUR_ATTRIBUTE].text
    search_url = "https://api.bing.microsoft.com/v7.0/SpellCheck"

    data = {
        'text': text
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Ocp-Apim-Subscription-Key': YOUR_API_KEY,
    }

    params = {
        'mkt': YOUR_LANGUAGE,
        'mode':'proof'
    }

    response = requests.post(search_url, headers=headers, params=params, data=data)
    response.raise_for_status()
    search_results = response.json()

    updated_string = text
    for i in range(len(search_results)):
        # retrieve the found token and the suggested token
        found_token = search_results["flaggedTokens"][i]["token"]
        suggested_token = search_results["flaggedTokens"][i]["suggestions"][0]["suggestion"]

        # updated the original string with each of the suggestions
        updated_string = updated_string.replace(found_token, suggested_token)

    return updated_string
```