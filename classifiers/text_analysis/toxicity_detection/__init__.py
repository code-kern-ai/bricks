import requests
import json
from pydantic import BaseModel

INPUT_EXAMPLE = {
    "apiToken": "<API_KEY_GOES_HERE>",
    "text": "Shut your mouth, you idiot!"
}

API_URL = "https://api-inference.huggingface.co/models/unitary/toxic-bert"

class ToxicityClassifierModel(BaseModel):
    apiToken: str
    text: str

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}


def toxicity_classifier(req: ToxicityClassifierModel):
    def query(api_token, inputs):
        headers = {"Authorization": f"Bearer {api_token}"}
        response = requests.post(API_URL, headers=headers, json={"inputs": inputs})
        json_response = response.json()
        result = [
            {item["label"]: item["score"] for item in entry}
            for entry in json_response
        ]
        breakpoint()
        res = json.dumps(result)
        return json.dumps(json_response)

    try:
        output = query(req.apiToken, req.text)
        return output
    except:
        return "That didn't work. Did you provide a valid Hugging Face API key?"