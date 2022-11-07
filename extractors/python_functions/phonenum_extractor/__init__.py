import re
from typing import Optional
from pydantic import BaseModel
import requests
from extractors.util.spacy import SpacySingleton
import phonenumbers

class PhonenumExtractorModel(BaseModel):
    text: str
    spacyTokenizer: Optional[str] = "en_core_web_sm"

    class Config:
        schema_extra = {
            "example": {
                "text": "So here's my number +442083661177. Call me maybe!",
                "spacyModel": "en_core_web_sm"
            }
        }

def validate_phone_number(request: PhonenumExtractorModel):
    text = request.text

    if requests.spacyTokenizer is not None:
        nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    else:
        nlp = SpacySingleton.get_nlp("en_core_web_sm")
    doc = nlp(text)

    regex = re.compile(r"[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}")
    regex.findall(text)

    valid_numbers = []
    for match in regex.finditer(text):
        try:
            parsed_num = phonenumbers.parse(match.group(0), None)
            if phonenumbers.is_valid_number(parsed_num):
                start, end = match.span()
                span = doc.char_span(start, end)
                valid_numbers.append([span.start, span.end, span.text]) 
        except:
            pass
    
    return {"valid_numbers": valid_numbers}
