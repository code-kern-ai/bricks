```python
import requests

ATTRIBUTE: str = "text" # only text attributes
MODEL_NAME: str = "KernAI/multilingual-e5-question-type"
REQUEST_URL: str = "https://free.api.kern.ai/inference"

def question_type_classifier(record):
    payload = {
        "name_model": MODEL_NAME,
        "text": record[ATTRIBUTE].text
    }      
    response = requests.post(REQUEST_URL, json=payload)
    if response.ok:
        return response.json()["label"]
```