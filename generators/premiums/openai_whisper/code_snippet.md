```python
import requests
import json

YOUR_ATTRIBUTE: str =  "url"
YOUR_API_KEY: str = "<YOUR_API_KEY_HERE" 

def openai_whisper(record):
    headers = {
        "Authorization": f"Api-Key {YOUR_API_KEY}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {
        "url": str(record[YOUR_ATTRIBUTE].text),
    }

    response = requests.post("https://app.baseten.co/model_versions/qjdelgq/predict", headers=headers, data=json.dumps(data))

    return str(response.json()["model_output"]["text"])
```