```python
import requests

ATTRIBUTE: str = "text"
API_KEY: str = "<API_KEY_GOES_HERE>"

def emotionality_detection(record):
      headers = {"Authorization": f"Bearer {API_KEY}"}
      data = {"inputs": record[ATTRIBUTE].text}
      try:
            response = requests.post("https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base", headers=headers, json=data)
            response_json = response.json()
            ner_positions = []
            for item in response_json:
                  start = item["start"]
                  end = item["end"]
                  span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
                  yield item["entity_group"], span.start, span.end
      except Exception as e: 
            return f"That didn't work. Did you provide a valid API key? Go error: {e} and message: {response_json}"
```