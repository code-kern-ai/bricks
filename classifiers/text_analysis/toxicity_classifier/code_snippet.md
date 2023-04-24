```python
import requests

YOUR_API_KEY: str = "<API_KEY_GOES_HERE>"
YOUR_API_URL = "https://api-inference.huggingface.co/models/unitary/toxic-bert"
YOUR_ATTRIBUTE: str = "text" # only text attributes

def toxicity_classifier(record):
    """
    Uses toxic-bert via Hugging Face Inference API to classify toxicity in text. Visit https://huggingface.co/unitary/toxic-bert for full documentation 
    """
    api_token = YOUR_API_KEY
    inputs = record[YOUR_ATTRIBUTE].text

    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.post(API_URL, headers=headers, json={"inputs": inputs})
    json_response = response.json()
    result = [
        {item["label"]: item["score"] for item in entry}
        for entry in json_response
    ]
    return json.dumps(result)
```