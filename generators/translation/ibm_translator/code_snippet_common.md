```python
import requests

def ibm_translator(text: str, api_key:str, instance_id:str, original_language:str, target_language:str) -> str:
    """ 
    @param text: text we want to translate
    @param api_key: IBM API Key
    @param instance_id: IBM instance id
    @param original_language: only iso format
    @param target_language: only iso format
    @return: translated text
    """
    headers = {'Content-Type': 'application/json'}
    data = '{"text":'+f'["{text}"], '+'"model_id":'+f'"{original_language}-'+f'{target_language}"'+'}'
    auth = ('apikey', api_key)
    url = f"https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/{instance_id}" 
    response = requests.post(
        url, 
        headers=headers,
        data=data, 
        auth=auth
    )
    try:
        translation = [i["translation"] for i in response.json()["translations"]]
        return " ".join(translation)
    except:
        return "Translation not possible."

# ↑ necessary bricks stuff
# -----------------------------------------------------------------------------------------
# ↓ example implementation
 
def example_integration():
    texts = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]
    api_key = "<API_KEY_TO_USE>"
    instance_id = "<INSTANCE_ID_TO_USE>"
    original_language = "en"
    target_language = "de"
    for text in texts:
        print(f"the text \"{text}\" in {target_language} is {ibm_translator(text, api_key, instance_id, original_language, target_language)}")
example_integration() 
```