from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re
from nltk.corpus import stopwords

INPUT_EXAMPLE = {
    "text": '''"Hello, how are you?" he asked.
            "I am doing fine, and you?", she said.
            "I am doing good as well.".
            "Listen, I wanted to talk to you about the something. Actually your car broke down on the bridge and I 
            suspect that the engine is heated up.".
            "Don't worry about that, I'll buy a new car!"''',
    "spacyTokenizer": "en_core_web_sm",
    "stopWords": "english",
}


class SmalltalkExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"
    stopWords: str = "english"


    class Config:
        schema_example = {"example": INPUT_EXAMPLE}


def smalltalk_extraction(request: SmalltalkExtractionModel):
    """Detects smalltalk languages from chats"""

    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    sw = stopwords.words(request.stopWords)
    regex = re.compile(r"\".*?\"")

    smalltalk = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        text_list_original = span.text.replace('"', '').replace(',', '').split()
        new_text = []
        stop_words = []
        for token in text_list_original:
            if token not in sw:
                new_text.append(token)
            else:
                stop_words.append(token)
        if len(new_text) < 0.5 * len(text_list_original) or len(stop_words) < 8:
            smalltalk.append(["smalltalk", span.start, span.end])

    return {"smalltalk": smalltalk}
