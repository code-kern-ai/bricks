from pydantic import BaseModel
import requests

INPUT_EXAMPLE = {
    "text": "Sushi restaurants Barcelona",
    "api_key": "<API_KEY_GOES_HERE>"
}


class CommunicationStyleClassifierModel(BaseModel):
    text: str
    api_key: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def communication_style_classifier(req: CommunicationStyleClassifierModel):
    """Uses a custom E5 transformer model to classify a text by communication style"""
    url = ""

    data = {}
    headers = {}
    params = {}

    response = requests.post(url, headers=headers, params=params, data=data)
    response.raise_for_status()
    return response.json()