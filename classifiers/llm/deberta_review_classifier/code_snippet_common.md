```python
import requests

def deberta_review_classifier(text: str, api_key: str) -> dict:
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post("https://api-inference.huggingface.co/models/RashidNLP/Amazon-Deberta-Base-Sentiment", headers=headers, json={"inputs": text})
    json_response = response.json()
    while not isinstance(json_response, dict):
        json_response = json_response[0]
    if "label" not in json_response:
        return f"This didn't work, got: {json_response}"
    else:
        json_response = json_response["label"]
    return json_response

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    api_key = "<API_KEY_GOES_HERE>"
    texts = ["This is a great product and I would buy it again, 10/10 would recommend!", "Product broke immediately. Don't like it. :/"]
    for text in texts:
        print(f"\"{text}\" is {deberta_review_classifier(text, api_key)}")

example_integration()
```