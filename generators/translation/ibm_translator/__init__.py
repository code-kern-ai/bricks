import requests
from pydantic import BaseModel
from typing import List

# Find out more here: https://cloud.ibm.com/apidocs/language-translator

INPUT_EXAMPLE = {
    "text": ["Hello, world!"],
    "apiKey": "<API_KEY_GOES_HERE>",
    "ibmURL": "<RESOURCE_URL_GOES_HERE>",
    "origin": "en",
    "target": "de",
}


class IbmTranslatorModel(BaseModel):
    text: List[str]
    apiKey: str
    ibmURL: str
    origin: str
    target: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def ibm_translator(req: IbmTranslatorModel):
    """Translates texts using the IBM watson service."""
    headers = {"Content-Type": "application/json"}
    auth = ("apikey", req.apiKey)
    data = (
        '{"text":'
        + f'["{req.text}"], '
        + '"model_id":'
        + f'"{req.origin}-'
        + f'{req.target}"'
        + "}"
    )

    response = requests.post(req.ibmURL, headers=headers, data=data, auth=auth)

    return {"translations": [i["translation"] for i in response.json()["translations"]]}
