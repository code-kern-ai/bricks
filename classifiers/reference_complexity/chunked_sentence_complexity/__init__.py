from pydantic import BaseModel
from typing import Optional
from extractors.util.spacy import SpacySingleton
from collections import Counter
import textstat

INPUT_EXAMPLE = {
    "text": "Wow, this is really cool!", 
    "language": "en",
}

MODELS = {
    "en": "en_core_web_sm",
    "de": "de_core_news_sm"
}


class ChunkedSentenceComplexityModel(BaseModel):
    text: str
    language: Optional[str] = None

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def get_mapping_complexity(score):
    if score < 30:
        return "very difficult"
    if score < 50:
        return "difficult"
    if score < 60:
        return "fairly difficult"
    if score < 70:
        return "standard"
    if score < 80:
        return "fairly easy"
    if score < 90:
        return "easy"        
    return "very easy"
    
def chunked_sentence_complexity(req: ChunkedSentenceComplexityModel):
    """Chunks a text and calculates complexity of it."""
    textstat.set_lang(req.language)

    nlp = SpacySingleton.get_nlp(MODELS.get(req.language, "en_core_web_sm")) # defaults to "en_core_web_sm"  
    doc = nlp(req.text)
    
    complexities = [textstat.flesch_reading_ease(sent.text) for sent in doc.sents]

    avg = int(round(sum(complexities) / len(complexities)))
    return {"overall_text_complexity": get_mapping_complexity(avg)}
