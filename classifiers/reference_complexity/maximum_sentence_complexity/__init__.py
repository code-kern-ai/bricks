from pydantic import BaseModel
from typing import Optional
from extractors.util.spacy import SpacySingleton
from collections import Counter
import textstat

INPUT_EXAMPLE = {
    "text": "An easy sentence. Despite the rains persistence, the resilient team continued their expedition, undeterred by the relentless downpour.", 
    "language": "en",
}

MODELS = {
    "en": "en_core_web_sm",
    "de": "de_core_news_sm"
}


class MaximumSentenceComplexityModel(BaseModel):
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
    
def maximum_sentence_complexity(req: MaximumSentenceComplexityModel):
    """Chunks a text and calculates complexity of it."""
    textstat.set_lang(req.language)

    nlp = SpacySingleton.get_nlp(MODELS.get(req.language, "en_core_web_sm")) # defaults to "en_core_web_sm"  
    doc = nlp(req.text)
    
    complexities = [textstat.flesch_reading_ease(sent.text) for sent in doc.sents]
    return {"overall_text_complexity": get_mapping_complexity(min(complexities))}
