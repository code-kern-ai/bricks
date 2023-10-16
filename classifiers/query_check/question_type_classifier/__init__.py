from pydantic import BaseModel
import requests

INPUT_EXAMPLE = {
    "text": "Sushi restaurants Barcelona",
    "model_name": "KernAI/multilingual-e5-question-type",
}


class QuestionTypeClassifierModel(BaseModel):
    text: str
    model_name: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def question_type_classifier(req: QuestionTypeClassifierModel):
    """Uses custom E5 model to classify the question type of a text"""
    payload = {
        "name_model": req.model_name,
        "text": req.text
    }      
    response = requests.post("https://free.api.kern.ai/inference", json=payload)
    if response.ok:
        return {"question_type": response.json()["label"]}
    return response.raise_for_status()