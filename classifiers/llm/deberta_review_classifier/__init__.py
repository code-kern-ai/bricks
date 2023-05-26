import requests
import json
from pydantic import BaseModel

INPUT_EXAMPLE = {
    "apiToken": "<API_KEY_GOES_HERE>",
    "text": "This is a great product and I would buy it again, 10/10 would recommend!"
}

class DebertaReviewClassifierModel(BaseModel):
    apiToken: str
    text: str

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}


def deberta_review_classifier(req: DebertaReviewClassifierModel):
    """Uses a DeBERTa model to classify the sentiment of customer reviews."""
    def query(api_token, inputs):
        headers = {"Authorization": f"Bearer {api_token}"}
        response = requests.post("https://api-inference.huggingface.co/models/RashidNLP/Amazon-Deberta-Base-Sentiment", headers=headers, json={"inputs": inputs})
        json_response = response.json()
        while not isinstance(json_response, dict):
            json_response = json_response[0]
        if "label" not in json_response:
            json_response = "Unkown"
        else:
            json_response = json_response["label"]
        return json_response

    try:
        output = query(req.apiToken, req.text)
        return {"Sentiment": output}
    except:
        return {"Error": "That didn't work. Did you provide a valid Hugging Face API key?"}