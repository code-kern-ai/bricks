
from pydantic import BaseModel
import requests

INPUT_EXAMPLE = {
    "text": "Ths text contans speling errors.",
    "apiKey": "<api-key-goes-here>",
    }

class BingSpellingCorrectionModel(BaseModel):
    text: str
    apiKey: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def bing_spelling_correction(req: BingSpellingCorrectionModel):
    '''Uses Microsoft's Bing to correct the spelling of sentences.'''

    text = req.text

    if(len(text) == 0):
        return {"correctedText": ""}
    elif(len(text) >= 1500):
        raise ValueError("""The text is too long for the bing API to process. 
                         Please shorten it to less than 1500 characters.""")
    
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
    for i in range(len(search_results["flaggedTokens"])):
        # retrieve the found token and the suggested token
        found_token = search_results["flaggedTokens"][i]["token"]
        suggested_token = search_results["flaggedTokens"][i]["suggestions"][0]["suggestion"]

        # updated the original string with each of the suggestions
        updated_string = updated_string.replace(found_token, suggested_token)

    return {"correctedText": updated_string}