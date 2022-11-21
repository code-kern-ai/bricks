```python
import requests

YOUR_ATTRIBUTE = "headline"
API_KEY = "<api-key-goes-here>" 

def deepl_translator(record):
    '''Uses DeepL API to translate texts.'''
    deepl_url = "https://api.deepl.com/v2/translate"
    params={ 
        "auth_key": API_KEY, 
        "target_lang": "de", # Change this to the language of your choice
        "text": record[YOUR_ATTRIBUTE].text, 
    }

    deepl_result = requests.get(
    deepl_url, 
    params=params
    ) 
    deepl_result_json= deepl_result.json()
    translation = deepl_result_json["translations"][0]["text"]

    return translation
```