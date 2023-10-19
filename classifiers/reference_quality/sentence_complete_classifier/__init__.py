from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "text": "it would be sad if",
    "spacy_model": "en_core_web_sm"
}

class SentenceCompleteClassifierModel(BaseModel):
    text: str
    spacy_model: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def sentence_complete_classifier(req: SentenceCompleteClassifierModel):
    """Classify whether or not a text is complete"""
    nlp = SpacySingleton.get_nlp(req.spacy_model)
    doc = nlp(req.text)

    classifications = []
    for sent in doc.sents:
        if sent[0].is_title and sent[-1].is_punct:
            has_noun = 2
            has_verb = 1
            for token in sent:
                if token.pos_ in ["NOUN", "PROPN", "PRON"]:
                    has_noun -= 1
                elif token.pos_ == "VERB":
                    has_verb -= 1
            if has_noun < 1 and has_verb < 1:
                classifications.append("complete")
            else:
                classifications.append("incomplete")
        else:
            classifications.append("incomplete")

    # Aggregation logic
    if all(classification == "complete" for classification in classifications):
        return {"text_completeness": "complete"}
    elif all(classification == "incomplete" for classification in classifications):
        return {"text_completeness": "incomplete"}
    elif any(classification == "incomplete" for classification in classifications):
        return {"text_completeness": "partly complete"}