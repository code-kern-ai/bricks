from fastapi import APIRouter
from .python_functions import (
    language_detection,
    lookup_list,
    sentence_complexity,
    textblob_sentiment,
    textblob_subjectivity,
    emotionality_detection,
    spelling_check,
    cosine_similarity,
    profanity_detection,
    vader_sentiment,
)
from .premiums import (
    gpt3_classifier,
    toxicity_classifier
)

router = APIRouter()

for module in [
    language_detection,
    lookup_list,
    sentence_complexity,
    textblob_sentiment,
    textblob_subjectivity,
    emotionality_detection,
    spelling_check,
    cosine_similarity,
    profanity_detection,
    gpt3_classifier,
    vader_sentiment,
    toxicity_classifier
]:
    module_name = module.__name__.split(".")[-1]
    model_name = (
        "".join([term.capitalize() for term in module_name.split("_")]) + "Model"
    )
    exec(
        f"""
@router.post("/{module_name}")
async def api_{module_name}(request: {module_name}.{model_name}):
    return {module_name}.{module_name}(request)
    """
    )
