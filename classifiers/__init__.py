from fastapi import APIRouter

from .llm import gpt_classifier

from .lookup_lists import lookup_list

from .sentiment import (
    textblob_sentiment,
    vader_sentiment_classifier,
)

from .similarity import (
    cosine_similarity,
)

from .spelling import (
    spelling_check,
)

from .text_analysis import (
    emotionality_detection,
    language_detection,
    profanity_detection,
    sentence_complexity,
    textblob_subjectivity,
    toxicity_classifier,
)

from .spelling import (
    spelling_check,
)

router = APIRouter()

for module in [
    textblob_sentiment,
    spelling_check,
    vader_sentiment_classifier,
    gpt_classifier,
    lookup_list,
    cosine_similarity,
    emotionality_detection,
    language_detection,
    profanity_detection,
    sentence_complexity,
    textblob_subjectivity,
    toxicity_classifier,
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
