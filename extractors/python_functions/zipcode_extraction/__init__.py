import re 
import json 

from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "text": "10 Downing Street London SW1A 2AA",
    "countryId": "GB",
}

class ZipcodeExtractionModel(BaseModel):
    text: str
    countryId: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

# Load JSON file with all zip code regex patterns
with open('extractors/python_functions/zipcode_extraction/zip_codes.json') as f:
    zip_codes_json = json.load(f)

def zipcode_extraction(req: ZipcodeExtractionModel):
    """Extracts a zipcode from a string using regex."""
    country_id = req.countryId
    text = req.text

    nlp = SpacySingleton.get_nlp("en_core_web_sm")
    doc = nlp(text)

    match = re.search(zip_codes_json[country_id], text)

    start, end = match.span()
    span = doc.char_span(start, end, alignment_mode="expand")

    return {country_id : ["zip code", span.start, span.end]}
