import requests
from extractors.util.spacy import SpacySingleton
from pydantic import BaseModel

INPUT_EXAMPLE = {
      "text": "Angela Merkel was the chancellor of Germany.",
      "apiKey": "<API_KEY_GOES_HERE>"
}

class PegasusSummarizationModel(BaseModel):
      apiKey: str
      text: str 

      class Config:
            schema_example = {"example": INPUT_EXAMPLE}

def pegasus_summarization(req: PegasusSummarizationModel):
      """Pegasus model for text summarization."""
      headers = {"Authorization": f"Bearer {req.apiKey}"}
      data = {"inputs": req.text}
      try:
            response = requests.post("https://api-inference.huggingface.co/models/google/pegasus-large", headers=headers, json=data)
            response_json = response.json()
            return response_json[0]["summary_text"]
      except Exception as e: 
            return f"That didn't work. Did you provide a valid API key? Go error: {e} and message: {response_json}"