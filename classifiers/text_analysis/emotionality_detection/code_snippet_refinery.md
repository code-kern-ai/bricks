```python
import requests

ATTRIBUTE: str = "text"
API_KEY: str = "<API_KEY_GOES_HERE>"

def emotionality_detection(text, api_key):
      headers = {"Authorization": f"Bearer {API_KEY}"}
      data = {"inputs": record[ATTRIBUTE].text}
      try: 
            response = requests.post("https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base", headers=headers, json=data)
            response_json = response.json()
            flat_list = [item for sublist in response_json for item in sublist]
            max_item = max(flat_list, key=lambda x: x["score"])
            max_label = max_item["label"]
            return max_label
      except Exception as e: 
            return f"That didn't work. Did you provide a valid API key? Go error: {e} and message: {response_json}"        
```