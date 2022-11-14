```python
import requests

YOUR_PROVIDER = "<proivder-goes-here>" # microsoft or deepl

MSFT_API = "<api-goes-here>
MSFT_REGION

DEEPL_API = "<api-goes-here>
YOUR_ATTRIBUTE = "text"
ORIGIN_LANG = "DE"
TARGET_LANG = "EN"

def lang_translator(record):
    provider = YOUR_PROVIDER
    elif provider == "microsoft":

        # Add your key and endpoint
        key = MSFT_API
        location = MSFT_REGION # required if you're using a multi-service or regional (not global) resource.
        endpoint = "https://api.cognitive.microsofttranslator.com/translate"

        params = {
            'api-version': '3.0',
            'from': ORIGIN_LANG,
            'to': TARGET_LANG
        }

        headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # You can pass more than one object in body.
        body = [{
            'text': record["text"]
        }]

        request = requests.post(
            endpoint, 
            params=params, 
            headers=headers, 
            json=body
        )
        response = request.json()

        yield "translation", response[0]["translations"]

    elif provider == "deepl":
        deepl_url = "https://api.deepl.com/v2/translate"

        params={ 
            "auth_key": DEEPL_API, 
            "target_lang": TARGET_LANG, 
            "text": YOUR_ATTRIBUTE, 
        }

        deepl_result = requests.get(
        deepl_url, 
        params=params
        ) 

        yield "translation", deepl_result.json()
```