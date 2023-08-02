```python

import requests
import spacy

def emotion_detection(text, api_key):
      headers = {"Authorization": f"Bearer {api_key}"}
      data = {"inputs": text}
      try: 
            response = requests.post("https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base", headers=headers, json=data)
            response_json = response.json()
            ner_positions = []

            nlp = spacy.load("en_core_web_sm")
            doc = nlp(text)

            for item in response_json:
                  start = item["start"]
                  end = item["end"]
                  span = doc.char_span(start, end, alignment_mode="expand")
                  ner_positions.append((item["entity_group"], span.start, span.end))
            return ner_positions
      except Exception as e: 
            return f"That didn't work. Did you provide a valid API key? Go error: {e} and message: {response_json}"

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
      hf_api_key = "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"
      texts = ["What a great day to go to the beach.", "Sorry to hear that. CAn I help you?", "Why the hell would you do that?"]
      for text in texts:
            output = emotion_detection(text, api_key=hf_api_key)
            print(output)

example_integration()
```