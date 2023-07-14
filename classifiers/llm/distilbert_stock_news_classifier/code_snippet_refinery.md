```python
import requests
import json

API_KEY: str = "<API_KEY_GOES_HERE>"
ATTRIBUTE: str = "text" # only text attributes

def distilbert_stock_news_classifier(record):
    api_token = API_KEY
    inputs = record[ATTRIBUTE].text
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.post("https://api-inference.huggingface.co/models/KernAI/stock-news-destilbert", headers=headers, json={"inputs": inputs})
    json_response = response.json()
    result = [{item["label"]: item["score"] for item in entry} for entry in json_response]
    return str(list(result[0].keys())[0])
```