from pydantic import BaseModel
from translate import Translator

INPUT_EXAMPLE = {
    "text": "Hallo, guten Tag.",
    "fromLang": "de",
    "toLang": "en",
    }

class LanguageTranslatorModel(BaseModel):
    text: str
    fromLang: str
    toLang: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def language_translator(req: LanguageTranslatorModel):
    """Function to translate text."""

    origin_lang = req.fromLang
    target_lang = req.toLang
    string_to_translate = req.text

    translator = Translator(from_lang=origin_lang, to_lang=target_lang)
    translation = translator.translate(string_to_translate)
    return {"translation": translation}

