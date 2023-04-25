```python
import requests

def bert_toxicity_classifier(text: str, api_key: str) -> dict:
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post("https://api-inference.huggingface.co/models/unitary/toxic-bert", headers=headers, json={"inputs": text})
    json_response = response.json()
    result = [
        {item["label"]: item["score"] for item in entry}
        for entry in json_response
    ]
    return result[0]

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    api = "<API_KEY_GOES_HERE>"
    texts = ["Damn you are a stupid moron!", "The flowers look beautiful today.", "I hate all german people!", "I love you!"]
    for text in texts:
        print(f"\"{text}\" is {toxicity_classifier(text, api)}")

example_integration()
```