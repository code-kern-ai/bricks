```python
import requests, uuid

YOUR_ATTRIBUTE = "text"
API_KEY = "<api-key-goes-here>"

def microsoft_translator(record):
    endpoint = "https://api.cognitive.microsofttranslator.com/translate"
    params = {
        'api-version': '3.0',
        'from': ["de"],
        'to': ["en"] # You can translate to multiple languages by adding languages to the list
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