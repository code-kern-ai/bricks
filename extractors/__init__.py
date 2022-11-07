from fastapi import APIRouter
from .python_functions import (
    aspect_matcher,
    date_extraction,
    email_extraction,
    gazetteer,
    hashtag_extraction,
    name_extraction,
    org_extraction,
    price_extraction,
    regex_extraction,
    time_extraction,
    url_extraction,
    window_search,
    ip_extractor
)

router = APIRouter()

@router.post("/aspect_matcher")
async def api_aspect_matcher(request: aspect_matcher.AspectMatcherModel):
    return aspect_matcher.aspect_matcher(request)

@router.post('/date_extraction')
def api_date_extraction(request: date_extraction.DateExtractionModel):
    return date_extraction.date_extractor(request)

@router.post('/email_extraction')
def api_email_extraction(request: email_extraction.EmailExtractionModel):
    return email_extraction.email_extractor(request)

@router.post('/gazetteer')
def api_gazetteer(request: gazetteer.GazetteerModel):
    return gazetteer.gazetteer(request)

@router.post('/hashtag_extraction')
def api_hash_extraction(request: hashtag_extraction.HashExtractionModel):
    return hashtag_extraction.hash_extractor(request)

@router.post('/name_extraction')
def api_name_extraction(request: name_extraction.NameExtractionModel):
    return name_extraction.name_extractor(request)

@router.post('/org_extraction')
def api_org_extraction(request: org_extraction.OrganisationExtractionModel):
    return org_extraction.organisation_extraction(request)

@router.post('/price_extraction')
def api_price_extraction(request: price_extraction.PriceExtractionModel):
    return price_extraction.price_extractor(request)

@router.post('/regex_extraction')
def api_regex_extraction(request: regex_extraction.RegexExtractionModel):
    return regex_extraction.extract_by_regex(request)

@router.post('/time_extraction')
def api_time_extraction(request: time_extraction.TimeExtractionModel):
    return time_extraction.time_extractor(request)

@router.post('/url_extraction')
def api_url_extraction(request: url_extraction.UrlExtractionModel):
    return url_extraction.fn_url_extraction(request)

@router.post('/window_search')
def api_window_search(request: window_search.WindowSearchModel):
    return window_search.window_search(request)

@router.post('/ip_extractor')
def api_window_search(request: ip_extractor.IpExtractionModel):
    return ip_extractor.fn_ip_extractor(request)