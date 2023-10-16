```python
import requests

ATTRIBUTE: str = "text" # only text attributes
API_KEY: str = "<API_KEY_GOES_HERE>"

def question_type_classifier(record):
    text = record[ATTRIBUTE].text
    url = ""

    data = {}
    headers = {}
    params = {}

    response = requests.post(search_url, headers=headers, params=params, data=data)
    response.raise_for_status()
    return response.json()
```