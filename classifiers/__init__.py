from fastapi import APIRouter
from .python_functions import (
    levenshtein_distance,
    language_detection,
    lookup_list,
    reading_time,
    sentence_complexity,
    syllable_count,
    textblob_sentiment,
    textblob_subjectivity,
    emotionality_detection,
    spelling_check,
    cosine_similarity
)

router = APIRouter()

for module in [
    levenshtein_distance,
    language_detection,
    lookup_list,
    reading_time,
    sentence_complexity,
    syllable_count,
    textblob_sentiment,
    textblob_subjectivity,
    emotionality_detection,
    spelling_check,
    cosine_similarity
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
