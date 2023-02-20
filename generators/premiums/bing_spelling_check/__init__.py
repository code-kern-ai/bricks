from pydantic import BaseModel
import requests

INPUT_EXAMPLE = {
    "text": "Ths text contans speling errors.",
    "apiKey": "<api-key-goes-here>",
    }

class BingSpellingCheckModel(BaseModel):
    text: str
    apiKey: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def bing_spelling_check(req: BingSpellingCheckModel):
    '''Uses Microsoft's Bing to correct the spelling of sentences.'''

    text = req.text
    search_url = "https://api.bing.microsoft.com/v7.0/SpellCheck"

    data = {
        'text': text
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Ocp-Apim-Subscription-Key': req.apiKey,
    }

    params = {
        'mkt':'en-us',
        'mode':'proof'
    }

    response = requests.post(search_url, headers=headers, params=params, data=data)
    response.raise_for_status()
    search_results = response.json()

    updated_string = text
    # check if results are empty, i.e. if no errors were found. Returns original text if true.
    if len(search_results["flaggedTokens"]) == 0:
        return text
    else:
        for i in range(len(search_results)):
            try:
                print(search_results)
                # retrieve the found token and the suggested token
                found_token = search_results["flaggedTokens"][i]["token"]
                suggested_token = search_results["flaggedTokens"][i]["suggestions"][0]["suggestion"]

                # updated the original string with each of the suggestions
                updated_string = updated_string.replace(found_token, suggested_token)
            except:
                pass

    return {"correctedText": updated_string}