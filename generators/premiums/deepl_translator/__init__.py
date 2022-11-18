from pydantic import BaseModel
from typing import List
import requests, uuid

INPUT_EXAMPLE = {
    "text": "Hallo, guten Tag.",
    "toLang": "en",
    "apiKey": "<api-key-goes-here>",
    }

class DeeplTranslatorModel(BaseModel):
    text: str
    toLang: str
    apiKey: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def deepl_translator(req: DeeplTranslatorModel ):
    '''Uses DeepL API to translate texts.'''
    deepl_url = "https://api.deepl.com/v2/translate"
    params={ 
        "auth_key": req.apiKey, 
        "target_lang": req.toLang, 
        "text": req.text, 
    }

    deepl_result = requests.get(
    deepl_url, 
    params=params
    ) 

    return deepl_result.json()