```python
import requests

API_KEY: str = "<API_KEY_GOES_HERE>"
ATTRIBUTE: str = "text" # only text attributes

def deberta_review_classifier(record):
    inputs = record[ATTRIBUTE].text
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post("https://api-inference.huggingface.co/models/RashidNLP/Amazon-Deberta-Base-Sentiment", headers=headers, json={"inputs": inputs})
    json_response = response.json()
    result = [{item["label"]: item["score"] for item in entry} for entry in json_response]
    return str(list(result[0].keys())[0])
```