```python
import requests

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_API_KEY: str = "<api-key-goes-here>" # Deepl API Key
YOUR_TARGET_LANGUAGE: str = "de" # only iso format

def deepl_translator(record):
    """Uses DeepL API to translate texts."""
    if not record[YOUR_ATTRIBUTE] or not record[YOUR_ATTRIBUTE].text:
        return "No text string read!"
    deepl_url = "https://api.deepl.com/v2/translate"
    params={ 
        "auth_key": YOUR_API_KEY, 
        "target_lang": YOUR_TARGET_LANGUAGE, # Change this to the language of your choice
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