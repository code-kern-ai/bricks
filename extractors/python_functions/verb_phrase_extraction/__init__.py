from pydantic import BaseModel
import textacy

INPUT_EXAMPLE = {
    "text": "In the next section, we will build a new model which is more accurate than the previous one.",
    "spacyTokenizer": "en_core_web_sm",
}


class VerbPhraseExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def verb_phrase_extraction(request: VerbPhraseExtractionModel):
    """Extracts the verb phrases from a record"""

    text = request.text
    patterns = [{"POS": "AUX"}, {"POS": "VERB"}]
    doc = textacy.make_spacy_doc(text, lang=request.spacyTokenizer)
    verb_phrase = textacy.extract.token_matches(doc, patterns=patterns)
    verb_chunk = []
    for chunk in verb_phrase:
        verb_chunk.append(["match", chunk.start, chunk.end])

    return {"action": verb_chunk}
