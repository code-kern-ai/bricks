```python
import requests
import spacy

def bert_ner_extraction(text, api_key):
      headers = {"Authorization": f"Bearer {api_key}"}
      data = {"inputs": text}
      response = requests.post("https://api-inference.huggingface.co/models/dslim/bert-base-NER", headers=headers, json=data)
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

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
      hf_api_key = "<API_KEY_HERE>"
      texts = ["Apple announces new iPhone.", "Angela Merkel was the chancellor of Germany."]
      for text in texts:
            output = bert_ner_extraction(text, api_key=hf_api_key)
            print(output)

example_integration()
```