```python
import requests

def deepl_translator(text: str,api_key:str,target_language:str) -> str:    
    """ 
    @param text: text we want to translate
    @param api_key: Deepl API Key
    @param target_language: only iso format
    @return: translated text
    """
    deepl_url = "https://api.deepl.com/v2/translate"
    params={ 
        "auth_key": api_key, 
        "target_lang": target_language, 
        "text": text, 
    }
    deepl_result = requests.get(
        deepl_url, 
        params=params
    ) 
    deepl_result_json= deepl_result.json()
    return deepl_result_json["translations"][0]["text"]

# ↑ necessary bricks stuff
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]
    api_key = "<API_KEY_TO_USE>"
    target_language = "de"
    for text in texts:
        print(f"the text \"{text}\" in {target_language} is {deepl_translator(text, api_key, target_language)}")
example_integration() 
```