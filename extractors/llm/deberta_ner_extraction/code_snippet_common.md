```python
import requests
import spacy

def deberta_ner_extraction(text, api_key):
      headers = {"Authorization": f"Bearer {api_key}"}
      data = {"inputs": text, "options": {"wait_for_model": "true"}}
      try:
            response = requests.post("https://api-inference.huggingface.co/models/RashidNLP/NER-Deberta", headers=headers, json=data)
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
      hf_api_key = "<API_KEY_GOES_HERE>"
      texts = ["Apple announces new iPhone.", "Angela Merkel was the chancellor of Germany."]
      for text in texts:
            output = deberta_ner_extraction(text, api_key=hf_api_key)
            print(f"text: '{text}' contains the following entities -> {output}")

example_integration()
```