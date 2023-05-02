from fastapi import APIRouter

from .distance import (
    hamming_distance,
    levenshtein_distance,
    euclidean_distance,
    manhattan_distance,
)

from .lemmatizer import (
    spacy_lemmatizer,
)

from .paths import url_keyword_parser

from .search import (
    bing_news_search,
    bing_search,
    google_search,
    nyt_news_search,
)

from .speech_to_text import (
    azure_speech_to_text,
)

from .spelling import (
    textblob_spelling_correction,
    bing_spelling_correction,
)

from .summarization import (
    smalltalk_truncation,
    text_summarization,
    sumy_website_summarizer,
)

from .text_analytics import (
    most_frequent_words,
    phonetic_soundex,
    reading_time,
    syllable_count,
)

from .text_cleaning import html_cleanser, html_unescape

from .translation import (
    deepl_translator,
    ibm_translator,
    language_translator,
    microsoft_translator,
)

from .sentiment import vader_sentiment_scores

router = APIRouter()

for module in [
    language_translator,
    microsoft_translator,
    deepl_translator,
    hamming_distance,
    levenshtein_distance,
    ibm_translator,
    euclidean_distance,
    spacy_lemmatizer,
    url_keyword_parser,
    bing_news_search,
    bing_search,
    google_search,
    nyt_news_search,
    azure_speech_to_text,
    textblob_spelling_correction,
    smalltalk_truncation,
    text_summarization,
    most_frequent_words,
    phonetic_soundex,
    reading_time,
    syllable_count,
    html_cleanser,
    bing_spelling_correction,
    html_unescape,
    vader_sentiment_scores,
    manhattan_distance,
    sumy_website_summarizer,
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
