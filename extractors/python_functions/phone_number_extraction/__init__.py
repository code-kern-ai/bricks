import re
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import phonenumbers

INPUT_EXAMPLE = {
    "text": "So here's my number +442083661177. Call me maybe!",
    "spacyTokenizer": "en_core_web_sm",
}


class PhonenumExtractorModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def phone_number_extraction(request: PhonenumExtractorModel):
    """Detects phone numbers in a given text."""
    text = request.text

    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
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
                valid_numbers.append(["phoneNumber", span.start, span.end])
        except phonenumbers.phonenumberutil.NumberParseException:
            pass

    return {"phoneNumbers": valid_numbers}
