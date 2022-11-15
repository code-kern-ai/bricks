from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

# CSS colors can be specified:
# By color names
# As RGB values
# As hexadecimal values
# As HSL values (CSS3)
# As HWB values (CSS4)

INPUT_EXAMPLE = {
    "text": "There are more than 42 #colors you could use in CSS, e.g. #ff00ff, hsl(0, 0%, 0%), or rgba(255, 0, 0, 0.3) if you want to use alpha values.",
    "spacyTokenizer": "en_core_web_sm"
}

class ColorCodeExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def color_code_extraction(request: ColorCodeExtractionModel):
    """Extracts CSS colors from a text."""

    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)

    # https://developer.mozilla.org/en-US/docs/Web/CSS/color_value
    hexcolor_regex = re.compile(r"#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{4}|[0-9a-fA-F]{3})(?![0-9a-fA-F])")
    rgb_regex = re.compile(r"(rgba|rgb)\([^\)]*\)")
    hsl_regex = re.compile(r"(hsla|hsl)\([^\)]*\)")
    hwb_regex = re.compile(r"hwb\([^\)]*\)")

    color_codes = []
    for regex in [hexcolor_regex, rgb_regex, hsl_regex, hwb_regex]:
        for match in regex.finditer(text):
            start, end = match.span()
            span = doc.char_span(start, end)
            color_codes.append(["color", span.start, span.end])

    return {"extractedColorCodes": color_codes}
