```python
import requests

def deberta_review_classifier(text: str, api_key: str) -> dict:
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post("https://api-inference.huggingface.co/models/RashidNLP/Amazon-Deberta-Base-Sentiment", headers=headers, json={"inputs": text})
    json_response = response.json()
    result = [
        {item["label"]: item["score"] for item in entry}
        for entry in json_response
    ]
    return list(result[0].keys())[0]

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    api_key = "<API_KEY_GOES_HERE>"
    texts = ["This is a great product and I would by it again, 10/10 would recommend!", "Product broke immediately. Don't like it. :/"]
    for text in texts:
        print(f"\"{text}\" is {deberta_review_classifier(text, api_key)}")

example_integration()
```