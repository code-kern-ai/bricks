import requests
from extractors.util.spacy import SpacySingleton
from pydantic import BaseModel

INPUT_EXAMPLE = {
      "text": "Angela Merkel was the chancellor of Germany.",
      "apiKey": "<API_KEY_GOES_HERE>"
}

class BertNerExtractionModel(BaseModel):
      apiKey: str
      text: str 

      class Config:
            schema_example = {"example": INPUT_EXAMPLE}

def bert_ner_extraction(req: BertNerExtractionModel):
      """BERT model for entity recognition."""
      headers = {"Authorization": f"Bearer {req.apiKey}"}
      data = {"inputs": req.text}
      response = requests.post("https://api-inference.huggingface.co/models/dslim/bert-base-NER", headers=headers, json=data)
      response_json = response.json()
      ner_positions = []

      nlp = SpacySingleton.get_nlp("en_core_web_sm")
      doc = nlp(req.text)

      for item in response_json:
            start = item["start"]
            end = item["end"]
            span = doc.char_span(start, end, alignment_mode="expand")
            ner_positions.append((item["entity_group"], span.start, span.end))
      return ner_positions