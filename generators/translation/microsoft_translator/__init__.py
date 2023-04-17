from pydantic import BaseModel
from typing import List
import requests, uuid

INPUT_EXAMPLE = {
    "text": "Hallo, guten Tag.",
    "fromLang": ["de"],
    "toLang": ["en"],
    "apiKey": "<API_KEY_GOES_HERE>",
    "region": "northeurope",
}


class MicrosoftTranslatorModel(BaseModel):
    text: str
    fromLang: List[str]
    toLang: List[str]
    apiKey: str
    region: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def microsoft_translator(req: MicrosoftTranslatorModel):
    """Uses Microsofts cognitive services to translate texts."""

    endpoint = "https://api.cognitive.microsofttranslator.com/translate"
    params = {"api-version": "3.0", "from": req.fromLang, "to": req.toLang}

    headers = {
        "Ocp-Apim-Subscription-Key": req.apiKey,
        "Ocp-Apim-Subscription-Region": req.region,
        "Content-type": "application/json",
        "X-ClientTraceId": str(uuid.uuid4()),
    }

    # You can pass more than one object in body.
    body = [{"text": req.text}]

    request = requests.post(endpoint, params=params, headers=headers, json=body)

    try:
        return request.json()
    except:
        return "That didn't work. Maybe the API key is wrong?"
