from pydantic import BaseModel
from typing import Optional, List
import requests, uuid

from translate import Translator

INPUT_EXAMPLE = {
    "text": "Hallo, guten Tag.",
    "fromLang": ["de"],
    "toLang": ["en"],
    "provider": "free",
    "apiKey": "<api-key>",
    }

class LangTranslatorModel(BaseModel):
    text: str
    fromLang: List[str]
    toLang: List[str]
    provider: str
    apiKey: Optional[str] # Only for microsoft or deepl provider
    region: Optional[str] # Only needed if using microsoft service

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def lang_translator(req: LangTranslatorModel):
    '''Function to transalte text using DeepL or Microsoft.'''
    provider = req.provider

    if provider == "free":
        origin_lang = req.fromLang[0]
        target_lang = req.toLang[0]
        string_to_translate = req.text

        translator = Translator(from_lang=origin_lang, to_lang=target_lang)
        translation = translator.translate(string_to_translate)
        return {"translation": translation}

    elif provider == "microsoft":

        # Add your key and endpoint
        key = req.apiKey
        location = req.region # required if you're using a multi-service or regional (not global) resource.
        endpoint = "https://api.cognitive.microsofttranslator.com/translate"

        params = {
            'api-version': '3.0',
            'from': req.fromLang,
            'to': req.toLang
        }

        headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # You can pass more than one object in body.
        body = [{
            'text': req.text
        }]

        request = requests.post(
            endpoint, 
            params=params, 
            headers=headers, 
            json=body
        )

        return {"translation": request.json()}

    elif provider == "deepl":
        deepl_url = "https://api.deepl.com/v2/translate"
        params={ 
            "auth_key": req.apiKey, 
            "target_lang": req.toLang[0], 
            "text": req.text, 
        }

        deepl_result = requests.get(
        deepl_url, 
        params=params
        ) 

        return {"translation", deepl_result.json()}