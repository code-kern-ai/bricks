```python
import requests, uuid

# replace this list with a list containing your data
text = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "your_text": text,
    "api_key": "2c5e376fb29f40eb8b6a98ee66995068", 
    "resource_location": "northeurope", # change this to the location where your resource is provisioned, like northeurope, uswest, etc
    "origin_language": "en", # only iso codes, change this to the language of your texts
    "target_language": "de" # only iso codes, change this to the language you want to translate to
}

def microsoft_translator(record: dict) -> dict:
    translations = []
    for entry in record["your_text"]:
        # prepare the API call
        endpoint = "https://api.cognitive.microsofttranslator.com/translate"
        params = {
            'api-version': '3.0',
            'from': [record["origin_language"]],
            'to': [record["target_language"]] 
        }

        headers = {
            "Ocp-Apim-Subscription-Key": record["api_key"],
            "Ocp-Apim-Subscription-Region": "northeurope", # Change this to the region of your resource
            "Content-type": "application/json",
            "X-ClientTraceId": str(uuid.uuid4())
        }

        # pass the text to the body
        body = [{
            "text": entry
        }]

        # make the API call
        request = requests.post(
            endpoint, 
            params=params, 
            headers=headers, 
            json=body
        )

        # parse the response
        request_json = request.json()
        translation = request_json[0]["translations"][0]["text"]
        translations.append(translation)

    return {"translations": translations}
```