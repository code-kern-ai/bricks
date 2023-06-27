```python
import requests

ATTRIBUTE: str = "text"
API_KEY: str = "<API_KEY_GOES_HERE>"

def pegasus_summarization(record):
      headers = {"Authorization": f"Bearer {API_KEY}"}
      data = {"inputs": record[ATTRIBUTE].text}
      try: 
            response = requests.post("https://api-inference.huggingface.co/models/google/pegasus-large", headers=headers, json=data)
            response_json = response.json()
            return response_json[0]["summary_text"]
      except Exception as e: 
            return f"That didn't work. Did you provide a valid API key? Go error: {e} and message: {response_json}"
```