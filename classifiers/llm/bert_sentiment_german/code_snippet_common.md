```python
import requests

def bert_sentiment_german(text, api_key):
      try:
            headers = {"Authorization": f"Bearer {api_key}"}
            data = {"inputs": text, "options": {"wait_for_model": "true"}}
            response = requests.post("https://api-inference.huggingface.co/models/oliverguhr/german-sentiment-bert", headers=headers, json=data)
            response_json = response.json()
            return response_json[0][0]["label"]
      except Exception as e: 
           return f"That didn't work. Did you provide a valid API key? Got error: {e} and message {response_json}"

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
      hf_api_key = "<API_KEY_GOES_HERE>"
      texts = ["Ich mag diese Bratwurst nicht! Sie schmeckt wirklich schlecht.", "Ein lecker Kaffee am Morgen vertreibt Kummer und Sorgen!"]
      for text in texts:
            output = bert_sentiment_german(text, api_key=hf_api_key)
            print(f"The text: '{text}' has the sentiment -> {output}")

example_integration()
```