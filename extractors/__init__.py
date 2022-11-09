from fastapi import APIRouter
from .python_functions import (
    aspect_matcher,
    book_extraction,
    date_extraction,
    email_extraction,
    gazetteer,
    hashtag_extraction,
    ip_extraction,
    name_extraction,
    org_extraction,
    phone_number_extraction,
    price_extraction,
    regex_extraction,
    time_extraction,
    url_extraction,
    window_search,
    metric_detector,
    path_extractor,
)

router = APIRouter()

for module in [
    aspect_matcher,
    book_extraction,
    date_extraction,
    email_extraction,
    gazetteer,
    hashtag_extraction,
    ip_extraction,
    name_extraction,
    org_extraction,
    phone_number_extraction,
    price_extraction,
    regex_extraction,
    time_extraction,
    url_extraction,
    window_search,
    metric_detector,
    path_extractor,
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
