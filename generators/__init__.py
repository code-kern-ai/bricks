from fastapi import APIRouter
from .python_functions import (
    language_translator,
    html_cleanser,
    phonetic_soundex,
    spelling_correction,
    smalltalk_truncation,
    hamming_distance,
    levenshtein_distance,
    reading_time,
    syllable_count,
    text_summarisation,
    spacy_lemmatizer,
)
from .premiums import (
    microsoft_translator,
    deepl_translator,
    ibm_translator,
    gpt3_grammar_correction,
    gpt3_tldr_summarization,
    gpt3_restaurant_review,
    nyt_news_search,
    bing_news_search,
    bing_search,
    google_search,
)

router = APIRouter()

for module in [
    language_translator,
    html_cleanser,
    microsoft_translator,
    deepl_translator,
    phonetic_soundex,
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
    nyt_news_search,
    bing_news_search,
    bing_search,
    google_search,
    spacy_lemmatizer,
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