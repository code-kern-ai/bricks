import requests
from extractors.util.spacy import SpacySingleton
from pydantic import BaseModel

INPUT_EXAMPLE = {
      "text": "I did not know that you were coming! I am very glad to see you. If you would tell me sooner, I would have baked some cookies, though.",
      "apiKey": "<API_KEY_GOES_HERE>"
}

class EmotionalityDetectionModel(BaseModel):
      apiKey: str
      text: str 

      class Config:
            schema_example = {"example": INPUT_EXAMPLE}

def emotionality_detection(req: EmotionalityDetectionModel):
      """huggingface model for emotion detection"""
      headers = {"Authorization": f"Bearer {req.apiKey}"}
      data = {"inputs": req.text}
      try: 
            response = requests.post("https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base", headers=headers, json=data)
            response_json = response.json()

            # flatten the list of lists
            flat_list = [item for sublist in response_json for item in sublist]

            # find the item with the highest score
            max_item = max(flat_list, key=lambda x: x["score"])

            # retrieve the label of the item with the highest score
            max_label = max_item["label"]

            return max_label
      except Exception as e: 
            return f"That didn't work. Did you provide a valid API key? Go error: {e} and message: {response_json}"