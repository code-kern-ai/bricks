```python
import requests
from typing import List

ATTRIBUTE: str = "text" # only text attributes
API_KEY: str = "<API_KEY_GOES_HERE>"
IBM_URL: str = "<RESOURCE_URL_GOES_HERE"
ORIGIN_LANG: str = "en"
TARGET_LANG: str = "de"


def ibm_translator(record):
    headers = {'Content-Type': 'application/json'}
    data = '{"text":'+f'["{record[ATTRIBUTE].text}"], '+'"model_id":'+f'"{ORIGIN_LANG}-'+f'{TARGET_LANG}"'+'}'
    auth = ('apikey', API_KEY)

    response = requests.post(
        IBM_URL, 
        headers=headers,
        data=data, 
        auth=auth
    )
    try:
        translation = [i["translation"] for i in response.json()["translations"]]
        return " ".join(translation)
    except:
        return "Tanslation not possible."
```