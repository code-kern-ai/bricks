```python
import requests
from typing import List

ATTRIBUTE: str = "text" # only text attributes
API_KEY: str = "<API_KEY_GOES_HERE>"
IBM_INSTANCE_ID: str = "<INSTANCE_ID_TO_USE>"
ORIGIN_LANG: str = "en"
TARGET_LANG: str = "de"


def ibm_translator(record):
    headers = {'Content-Type': 'application/json'}
    data = '{"text":'+f'["{record[ATTRIBUTE].text}"], '+'"model_id":'+f'"{ORIGIN_LANG}-'+f'{TARGET_LANG}"'+'}'
    auth = ('apikey', API_KEY)
    url = f"https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/{IBM_INSTANCE_ID}" 
    response = requests.post(
        url, 
        headers=headers,
        data=data, 
        auth=auth
    )
    try:
        translation = [i["translation"] for i in response.json()["translations"]]
        return " ".join(translation)
    except:
        return "Translation not possible."
```