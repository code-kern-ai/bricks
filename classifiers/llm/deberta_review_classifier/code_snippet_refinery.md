```python
import requests

API_KEY: str = "<API_KEY_GOES_HERE>"
ATTRIBUTE: str = "text" # only text attributes

def deberta_review_classifier(record):
    inputs = record[ATTRIBUTE].text
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post("https://api-inference.huggingface.co/models/RashidNLP/Amazon-Deberta-Base-Sentiment", headers=headers, json={"inputs": inputs})
    json_response = response.json()
    while not isinstance(json_response, dict):
        json_response = json_response[0]
    if "label" not in json_response:
        return f"This didn't work, got: {json_response}"
    else:
        json_response = json_response["label"]
    return json_response
```