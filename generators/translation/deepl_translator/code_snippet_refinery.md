```python
import requests

ATTRIBUTE: str = "text" # only text attributes
API_KEY: str = "<API_KEY_GOES_HERE>" # Deepl API Key
TARGET_LANGUAGE: str = "de" # only iso format

def deepl_translator(record):
    '''Uses DeepL API to translate texts.'''
    deepl_url = "https://api.deepl.com/v2/translate"
    params={ 
        "auth_key": API_KEY, 
        "target_lang": TARGET_LANGUAGE, # Change this to the language of your choice
        "text": record[ATTRIBUTE].text, 
    }

    deepl_result = requests.get(
    deepl_url, 
    params=params
    ) 
    deepl_result_json= deepl_result.json()
    translation = deepl_result_json["translations"][0]["text"]

    return translation
```