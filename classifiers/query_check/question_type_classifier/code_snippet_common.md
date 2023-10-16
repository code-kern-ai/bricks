```python
import requests

def question_type_classifier(text: str, model_name: str, request_url: str = "https://free.api.kern.ai/inference") -> str:
    """
    @param text: text with a user query you want to classify
    @param model_name: Name of a model provided by Kern AI
    @param request_url: URL to the API endpoint of Kern AI
    @return: returns either 'keyword-question', 'interrogative-question' or 'statement-question' 
    """
    payload = {
        "name_model": model_name,
        "text": text
    }      
    response = requests.post(request_url, json=payload)
    if response.ok:
        return response.json()["label"]
    return response.raise_for_status()


# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 


model_name = "KernAI/multilingual-e5-question-type"

def example_integration():
    texts = ["Travel documents Germany", "Give me documents related to travel insurance.", "What is the content of these documents about?"]
    for text in texts:
        print(f"the sentiment of \"{text}\" is \"{question_type_classifier(text, model_name=model_name)}\"")

example_integration()
```