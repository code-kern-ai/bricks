```python
import requests, uuid

ATTRIBUTE: str = "text" # only text attributes
API_KEY: str = "<API_KEY_GOES_HERE>" # Microsoft API key
ORIGINAL_LANGUAGE: str = "en" # only iso format
TARGET_LANGUAGE: str = "de" # only iso format

def microsoft_translator(record):
    endpoint = "https://api.cognitive.microsofttranslator.com/translate"
    params = {
        'api-version': '3.0',
        'from': [ORIGINAL_LANGUAGE],
        'to': [TARGET_LANGUAGE] 
    }

    headers = {
        'Ocp-Apim-Subscription-Key': API_KEY,
        'Ocp-Apim-Subscription-Region': "northeurope", # Change this to the region of your resource
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': record[ATTRIBUTE].text
    }]

    request = requests.post(
        endpoint, 
        params=params, 
        headers=headers, 
        json=body
    )

    request_json = request.json()
    translation = request_json[0]["translations"][0]["text"]

    return translation
```