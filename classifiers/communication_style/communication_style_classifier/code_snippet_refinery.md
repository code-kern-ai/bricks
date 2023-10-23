```python
import requests

ATTRIBUTE: str = "text" # only text attributes
MODEL_NAME: str = "KernAI/multilingual-e5-communication-style"
REQUEST_URL: str = "https://free.api.kern.ai/inference"

def communication_style_classifier(record):
    payload = {
        "model_name": MODEL_NAME,
        "text": record[ATTRIBUTE].text
    }      
    response = requests.post(REQUEST_URL, json=payload)
    if response.ok:
        return response.json()["label"]
```