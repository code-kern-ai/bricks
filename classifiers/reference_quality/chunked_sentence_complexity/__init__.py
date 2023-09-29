from pydantic import BaseModel
from typing import Optional
from extractors.util.spacy import SpacySingleton
from collections import Counter
import textstat

INPUT_EXAMPLE = {
    "text": "Wow, this is really cool!", 
    "language": "en",
    "spacy_model": "en_core_web_sm"
}

class SentenceComplexityModel(BaseModel):
    text: str
    language: Optional[str]
    spacy_model: Optional[str]

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def setall(d, keys, value):
    for k in keys:
        d[k] = value

OUTCOMES = {}
setall(OUTCOMES, range(90, 122), "very easy")
setall(OUTCOMES, range(80, 90), "easy")
setall(OUTCOMES, range(70, 80), "fairly easy")
setall(OUTCOMES, range(60, 70), "standard")
setall(OUTCOMES, range(50, 60), "fairly difficult")
setall(OUTCOMES, range(30, 50), "difficult")
setall(OUTCOMES, range(0, 30), "very difficult")


def get_mapping_complexity(score):
    if score < 0:
        return OUTCOMES[0]
    return OUTCOMES[int(score)]


def sentence_complexity(request: SentenceComplexityModel):
    text = request.text
    if len(text.strip()) == 0:
        return "Please provide a text input."
    else:
        language = request.language
        if language is not None:
            try:
                textstat.set_lang(language)
            except:
                print("Set language couldn't get identified. Setting to english as default.")
                textstat.set_lang("en")

        sentence_complexity_score = textstat.flesch_reading_ease(text)
        sentence_complexity = get_mapping_complexity(sentence_complexity_score)
        return {"sentenceComplexity": sentence_complexity}
    
    
def chunked_sentence_complexity(req: SentenceComplexityModel):
    """Calculate sentence complexity of a text."""
    textstat.set_lang(req.language)
    nlp = SpacySingleton.get_nlp(req.spacy_model)
    doc = nlp(req.text)
    
    complexities = []
    for sent in doc.sents:
        # Apply the complexity function to each sentence
        complexity = sentence_complexity(sent.text)
        complexities.append(complexity)

    counter = Counter(complexities)
    
    # aggregating the complexity
    complexity_scores = {"very easy": 1, "easy": 2, "fairly easy": 3, "standard": 4, "fairly difficult": 5, "difficult": 6, "very difficult": 7}

    total_score = 0
    total_count = 0
    for comp, count in counter.items():
        total_score += complexity_scores[comp] * count
        total_count += count

    # weighted average complexity
    average_complexity = total_score / total_count

    # create a reverse mapping from scores to complexity levels
    reverse_mapping = {v: k for k, v in complexity_scores.items()}

    # find the closest complexity level to the average complexity
    closest_complexity = min(reverse_mapping.keys(), key=lambda x: abs(x - average_complexity))
    return {"overall_text_complexity": reverse_mapping[closest_complexity]}