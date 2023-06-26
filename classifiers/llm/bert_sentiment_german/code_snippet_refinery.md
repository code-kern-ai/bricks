```python
import requests

ATTRIBUTE: str = "text" 
API_KEY: str = "<API_KEY_GOES_HERE>"

def bert_sentiment_german(record):
      try: 
            headers = {"Authorization": f"Bearer {API_KEY}"}
            data = {"inputs": record[ATTRIBUTE].text, "options": {"wait_for_model": "true"}}
            response = requests.post("https://api-inference.huggingface.co/models/oliverguhr/german-sentiment-bert", headers=headers, json=data)
            response_json = response.json()
            return response_json[0][0]["label"]
      except Exception as e: 
           return f"That didn't work. Did you provide a valid API key? Got error: {e} and message {response_json}"
```