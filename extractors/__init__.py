from fastapi import APIRouter

from .codes import color_code_extraction, stock_ticker_extraction

from .dates_and_times import (
    date_extraction,
    time_extraction,
)

from .functions import (
    aspect_extraction,
    gazetteer_extraction,
    regex_extraction,
    window_search_extraction,
)

from .llm import (
    gpt_information_extraction,
    deberta_ner_extraction,
    bert_ner_extraction,
)

from .media import work_of_art_extraction

from .metrics import (
    metric_extraction,
)

from .numbers import (
    credit_card_extraction,
    digit_extraction,
    iban_extraction,
    ip_extraction,
    isbn_extraction,
    phone_number_extraction,
    price_extraction,
    percentage_extraction,
    bic_extraction,
)

from .paths import (
    filepath_extraction,
    url_extraction,
)

from .personal_identifiers import (
    address_extraction,
    email_extraction,
    person_extraction,
    zipcode_extraction,
)

from .symbols import hashtag_extraction

from .words import (
    goodbye_extraction,
    keyword_extraction,
    noun_match_extraction,
    org_extraction,
    part_of_speech_extraction,
    quote_extraction,
    smalltalk_extraction,
    substring_extraction,
    synonym_extraction,
    verb_phrase_extraction,
    difficult_words_extraction,
)

router = APIRouter()

for module in [
    address_extraction,
    email_extraction,
    person_extraction,
    zipcode_extraction,
    color_code_extraction,
    stock_ticker_extraction,
    date_extraction,
    time_extraction,
    aspect_extraction,
    gazetteer_extraction,
    regex_extraction,
    window_search_extraction,
    gpt_information_extraction,
    work_of_art_extraction,
    metric_extraction,
    credit_card_extraction,
    digit_extraction,
    iban_extraction,
    ip_extraction,
    isbn_extraction,
    phone_number_extraction,
    price_extraction,
    filepath_extraction,
    url_extraction,
    hashtag_extraction,
    goodbye_extraction,
    keyword_extraction,
    noun_match_extraction,
    org_extraction,
    part_of_speech_extraction,
    quote_extraction,
    smalltalk_extraction,
    substring_extraction,
    synonym_extraction,
    verb_phrase_extraction,
    percentage_extraction,
    difficult_words_extraction,
    bic_extraction,
    deberta_ner_extraction,
    bert_ner_extraction,
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
