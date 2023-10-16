from pydantic import BaseModel
import requests

INPUT_EXAMPLE = {
    "text": "Sushi restaurants Barcelona",
    "api_key": "<API_KEY_GOES_HERE>"
}


class QuestionTypeClassifierModel(BaseModel):
    text: str
    api_key: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def question_type_classifier(req: QuestionTypeClassifierModel):
    """Uses a custom E5 transformer model to classify the """
    url = ""

    data = {}
    headers = {}
    params = {}

    response = requests.post(url, headers=headers, params=params, data=data)
    response.raise_for_status()
    return response.json()
