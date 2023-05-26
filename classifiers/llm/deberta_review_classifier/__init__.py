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
    """Uses the Hugging Face API to classify the sentiment of customer reviews."""
    def query(api_token, inputs):
        headers = {"Authorization": f"Bearer {api_token}"}
        response = requests.post("https://api-inference.huggingface.co/models/RashidNLP/Amazon-Deberta-Base-Sentiment", headers=headers, json={"inputs": inputs})
        json_response = response.json()
        result = [
            {item["label"]: item["score"] for item in entry}
            for entry in json_response
        ]
        return str(list(result[0].keys())[0])

    try:
        output = query(req.apiToken, req.text)
        return output
    except:
        return "That didn't work. Did you provide a valid Hugging Face API key?"