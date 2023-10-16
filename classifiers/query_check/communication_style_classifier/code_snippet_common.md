```python
import requests

def communication_style_classifier(text: str, api_key: str) -> str:
    """
    @param text: text with a user query you want to classify
    @return: returns either 'keyword-question', 'interrogative-question' or 'statement-question' 
    """
    url = ""

    data = {}
    headers = {}
    params = {}

    response = requests.post(search_url, headers=headers, params=params, data=data)
    response.raise_for_status()
    return response.json()


# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 


def example_integration():
    texts = ["Travel documents Germany", "What is the content of these documents about?", "Tell me the summary of the provided references."]
    for text in texts:
        print(f"the sentiment of \"{text}\" is \"{communication_style_classifier(text)}\"")

example_integration()

```