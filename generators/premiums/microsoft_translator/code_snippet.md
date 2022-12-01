```python
import requests, uuid

YOUR_ATTRIBUTE: str = "text" #only text attributes
YOUR_API_KEY: str = "<api-key-goes-here>" #Microsoft API key
YOUR_ORIGINAL_LANGUAGE: str = "en" #only iso format
YOUR_TARGET_LANGUAGE: str = "de" #only iso format

def microsoft_translator(record):
    endpoint = "https://api.cognitive.microsofttranslator.com/translate"
    params = {
        'api-version': '3.0',
        'from': [YOUR_ORIGINAL_LANGUAGE],
        'to': [YOUR_TARGET_LANGUAGE] 
    }

    headers = {
        'Ocp-Apim-Subscription-Key': API_KEY,
        'Ocp-Apim-Subscription-Region': "northeurope", # Change this to the region of your resource
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': record[YOUR_ATTRIBUTE].text
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