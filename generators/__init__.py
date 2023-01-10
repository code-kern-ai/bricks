from fastapi import APIRouter
from .python_functions import (
    language_translator,
    html_cleanser,
    soundex_generator,
    spelling_correction,
    smalltalk_truncation,
    hamming_distance,
    levenshtein_distance,
    reading_time,
    syllable_count,
    text_summarisation,
)
from .premiums import (
    microsoft_translator,
    deepl_translator,
    ibm_translator,
    gpt3_grammar_correction,
    gpt3_tldr_summarization,
    gpt3_restaurant_review,
)

router = APIRouter()

for module in [
    language_translator,
    html_cleanser,
    microsoft_translator,
    deepl_translator,
    soundex_generator,
    spelling_correction,
    smalltalk_truncation,
    hamming_distance,
    levenshtein_distance,
    reading_time,
    syllable_count,
    ibm_translator,
    text_summarisation,
    gpt3_grammar_correction,
    gpt3_tldr_summarization,
    gpt3_restaurant_review,
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