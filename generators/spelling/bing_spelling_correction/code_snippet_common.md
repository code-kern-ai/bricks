```python
import requests

def bing_spelling_correction(text: str, api_key: str, language: str) -> str:
    search_url = "https://api.bing.microsoft.com/v7.0/SpellCheck"
    data = {
        'text': text
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Ocp-Apim-Subscription-Key': api_key,
    }
    params = {
        'mkt': language,
        'mode':'proof'
    }
    response = requests.post(search_url, headers=headers, params=params, data=data)
    response.raise_for_status()
    search_results = response.json()
    updated_string = text

    for i in range(len(search_results["flaggedTokens"])):
        # retrieve the found token and the suggested token
        try:
            found_token = search_results["flaggedTokens"][i]["token"]
            suggested_token = search_results["flaggedTokens"][i]["suggestions"][0]["suggestion"]
            # updated the original string with each of the suggestions
            updated_string = updated_string.replace(found_token, suggested_token)
        except: 
            pass
    return updated_string

# ↑ necessary bricks stuff
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["Ths text contans speling errors.", "Apple pie is also very delicious."]
    api_key = "<YOUR_API_KEY_HERE>"
    language = "en-US"
    for text in texts:
        print(f"the text \"{text}\" when corrected is -> {bing_spelling_correction(text, api_key, language)}")
example_integration() 
```