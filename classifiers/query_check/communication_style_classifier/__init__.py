from pydantic import BaseModel
import requests

INPUT_EXAMPLE = {
    "text": "Change the number in row 2 and 3.",
    "model_name": "KernAI/multilingual-e5-communication-style",
}


class CommunicationStyleClassifierModel(BaseModel):
    text: str
    model_name: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def communication_style_classifier(req: CommunicationStyleClassifierModel):
    """Uses custom E5 model to classify communication style of a text"""
    payload = {
        "name_model": req.model_name,
        "text": req.text
    }      
    response = requests.post("https://free.api.kern.ai/inference", json=payload)
    if response.ok:
        return {"communication_style": response.json()["label"]}
    return response.raise_for_status()