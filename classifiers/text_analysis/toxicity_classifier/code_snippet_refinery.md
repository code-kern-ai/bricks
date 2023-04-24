```python
import requests
import json

API_KEY: str = "<API_KEY_GOES_HERE>"
ATTRIBUTE: str = "headline" # only text attributes

def toxicity_classifier(record):
    """
    Uses toxic-bert via Hugging Face Inference API to classify toxicity in text.
    """
    api_token = API_KEY
    inputs = record[ATTRIBUTE].text
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.post("https://api-inference.huggingface.co/models/unitary/toxic-bert", headers=headers, json={"inputs": inputs})
    json_response = response.json()
    result = [
        {item["label"]: item["score"] for item in entry}
        for entry in json_response
    ]
    return json.dumps(result[0])
```