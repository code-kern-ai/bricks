from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

INPUT_EXAMPLE = {
    "text": '''"Hello, Nick," said Harry.
            "Hello, hello," said Nearly Headless Nick, starting and looking round. He wore a dashing, plumed hat on his long curly hair, and a tunic with a ruff, which concealed the fact that his neck was almost completely severed. He was pale as smoke, and Harry could see right through him to the dark sky and torrential rain outside.
            "You look troubled, young Potter," said Nick, folding a transparent letter as he spoke and tucking it inside his doublet.
            "So do you," said Harry.''',
    "spacyTokenizer": "en_core_web_sm",
}


class QuoteExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"


    class Config:
        schema_example = {"example": INPUT_EXAMPLE}


def quote_extraction(request: QuoteExtractionModel):
    """Extracts all the quotes from a text"""

    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    regex = re.compile(r'"(.+?)"')

    quotes = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        quotes.append(["quote", span.start, span.end])

    return {"quote": quotes}
