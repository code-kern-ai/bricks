```python
import requests, uuid

def microsoft_translator(text: str, api_key:str, resource_location:str, original_language:str, target_language:str) -> str:
    """ 
    @param text: text we want to translate
    @param api_key: Microsoft API Key
    @param resource_location: location of the resource
    @param original_language: only iso format
    @param target_language: only iso format
    @return: translated text
    """
    endpoint = "https://api.cognitive.microsofttranslator.com/translate"
    params = {
        'api-version': '3.0',
        'from': [original_language],
        'to': [target_language] 
    }

    headers = {
        "Ocp-Apim-Subscription-Key": api_key,
        "Ocp-Apim-Subscription-Region": resource_location,
        "Content-type": "application/json",
        "X-ClientTraceId": str(uuid.uuid4())
    }
    body = [{
        "text": text
    }]
    request = requests.post(
        endpoint, 
        params=params, 
        headers=headers, 
        json=body
    )
    request_json = request.json()
    return request_json[0]["translations"][0]["text"]
       
# ↑ necessary bricks stuff
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]
    api_key = "<API_KEY_GOES_HERE>"
    resource_location = "northeurope" # change this to the location where your resource is provisioned, like northeurope, uswest, etc
    original_language = "en"
    target_language = "de"
    for text in texts:
        print(f"the text \"{text}\" in {target_language} is {microsoft_translator(text, api_key, resource_location, original_language, target_language)}")
example_integration() 
```