```python
import requests

# replace this list with a list containing your data
text = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "your_text": text,
    "api_key": "insert your API key here", 
    "ibm_url": "https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/INSTANCE_ID" # change INSTANCE_ID
    "origin_language": "en", # change this to the language of your texts
    "target_language": "de" # change this to the language you want to translate to
}

def ibm_translator(record: dict) -> dict:
    translations = []
    for entry in record["your_text"]:
        headers = {'Content-Type': 'application/json'}
        data = '{"text":'+f'["{entry}"], '+'"model_id":'+f'"{record["origin_language"]}-'+f'{record["target_language"]}"'+'}'
        auth = ('apikey', record["api_key"])

        response = requests.post(
            record["ibm_url"], 
            headers=headers,
            data=data, 
            auth=auth
        )
        try:
            translation = [i["translation"] for i in response.json()["translations"]]
            translations.append(" ".join(translation))
        except:
            translations.append("Tanslation not possible.")
    return {"translations": translations}
```