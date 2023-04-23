```python
import requests

# replace this list with a list containing your data
text = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "your_text": text,
    "api_key": "insert your API key here"
    "target_language": "de" # Change this to the language of your choice
}

def deepl_translator(record: dict) -> dict:
    translations = []
    for entry in record["your_texts"]:
        # set up everything for the API call
        deepl_url = "https://api.deepl.com/v2/translate"
        params={ 
            "auth_key": record["api_key"], 
            "target_lang": record["target_language"], 
            "text": entry, 
        }

        # send out API call
        deepl_result = requests.get(
        deepl_url, 
        params=params
        ) 

        # parse API response
        deepl_result_json= deepl_result.json()
        translation = deepl_result_json["translations"][0]["text"]

        # append to the list of translations
        translations.append(translation)
    return {"translations": translations}
```