from fastapi import APIRouter
from .python_functions import (
    address_extraction,
    aspect_extractor,
    work_of_art_extraction,
    credit_card_extraction,
    date_extraction,
    email_extraction,
    gazetteer_extraction,
    hashtag_extraction,
    ip_extraction,
    person_extraction,
    org_extraction,
    phone_number_extraction,
    price_extraction,
    regex_extraction,
    time_extraction,
    url_extraction,
    window_search_extraction,
    isbn_extraction,
    metric_extraction,
    filepath_extraction,
    synonym_extraction,
    substring_extraction,
    zipcode_extraction,
    color_code_extraction,
    part_of_speech_extraction,
    goodbye_extraction,
    quote_extraction,
    smalltalk_extraction,
    digit_extraction,
    keyword_extraction,
    iban_extraction,
    noun_match_extraction,
    stock_ticker_extraction,
    verb_phrase_extraction,
)

from .premiums import (
    gpt3_information_extraction
)

router = APIRouter()

for module in [
    address_extraction,
    aspect_extractor,
    work_of_art_extraction,
    credit_card_extraction,
    date_extraction,
    email_extraction,
    gazetteer_extraction,
    hashtag_extraction,
    ip_extraction,
    person_extraction,
    org_extraction,
    phone_number_extraction,
    price_extraction,
    regex_extraction,
    time_extraction,
    url_extraction,
    window_search_extraction,
    isbn_extraction,
    metric_extraction,
    filepath_extraction,
    synonym_extraction,
    substring_extraction,
    zipcode_extraction,
    color_code_extraction,
    part_of_speech_extraction,
    goodbye_extraction,
    quote_extraction,
    smalltalk_extraction,
    digit_extraction,
    keyword_extraction,
    iban_extraction,
    gpt3_information_extraction,
    noun_match_extraction,
    stock_ticker_extraction,
    verb_phrase_extraction,
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
