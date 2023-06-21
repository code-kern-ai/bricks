import requests
from pydantic import BaseModel

INPUT_EXAMPLE = {
    "apiToken": "<API_KEY_GOES_HERE>",
    "text": "Diese Bratwurst schmeckt wirklich lecker!"
}

class BertSentimentGermanModel(BaseModel):
    apiToken: str
    text: str

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}

def bert_sentiment_german(req: BertSentimentGermanModel):
      """ Sentiment classification for german texts using a BERT model."""
      try:
            headers = {"Authorization": f"Bearer {req.apiToken}"}
            data = {"inputs": req.text, "options": {"wait_for_model": "true"}}
            response = requests.post("https://api-inference.huggingface.co/models/oliverguhr/german-sentiment-bert", headers=headers, json=data)
            response_json = response.json()
            return {"sentiment": response_json[0][0]["label"]}
      except Exception as e: 
           return f"That didn't work. Did you provide a valid API key? Got error: {e} and message {response_json}"