```python
import requests

YOUR_ATTRIBUTE = "text"
API_KEY = "<key-goes-here>"

def deepl_translator(record):
    '''Uses DeepL API to translate texts.'''
    deepl_url = "https://api.deepl.com/v2/translate"
    params={ 
        "auth_key": API_KEY, 
        "target_lang": "en", # Change this to the language of your choice
        "text": record[YOUR_ATTRIBUTE].text, 
    }

    deepl_result = requests.get(
    deepl_url, 
    params=params
    ) 

    yield deepl_result.json()
```