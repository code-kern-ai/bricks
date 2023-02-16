```python
import requests

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_API_KEY: str = "<API_KEY_GOES_HERE>"
YOUR_IBM_URL: str = "<RESOURCE_URL_GOES_HERE"
YOUR_ORIGIN_LANG: str = "en"
YOUR_TARGET_LANG: str = "de"


def attribute_4(record):
    if not record[YOUR_ATTRIBUTE] or not record[YOUR_ATTRIBUTE].text:
        return "No text string read!"
    headers = {'Content-Type': 'application/json'}
    data = '{"text":'+f'["{record[YOUR_ATTRIBUTE].text}"], '+'"model_id":'+f'"{YOUR_ORIGIN_LANG}-'+f'{YOUR_TARGET_LANG}"'+'}'
    auth = ('apikey', YOUR_API_KEY)

    response = requests.post(
        YOUR_IBM_URL, 
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