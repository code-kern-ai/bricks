import requests
import json
from pydantic import BaseModel

INPUT_EXAMPLE = {
    "apiToken": "<API_KEY_GOES_HERE>",
    "text": "Shut your mouth, you idiot!"
}

class BertToxicityClassifierModel(BaseModel):
    apiToken: str
    text: str

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}


def bert_toxicity_classifier(req: BertToxicityClassifierModel):
    """Uses the Hugging Face API to classify text as toxic or not toxic."""
    def query(api_token, inputs):
        headers = {"Authorization": f"Bearer {api_token}"}
        response = requests.post("https://api-inference.huggingface.co/models/unitary/toxic-bert", headers=headers, json={"inputs": inputs})
        json_response = response.json()
        result = [
            {item["label"]: item["score"] for item in entry}
            for entry in json_response
        ]
        return json.dumps(result)

    try:
        output = query(req.apiToken, req.text)
        return output
    except:
        return "That didn't work. Did you provide a valid Hugging Face API key?"