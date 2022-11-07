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


@router.post(f"/{aspect_matcher.aspect_matcher.__name__.lower()}")
def api_language_detection(request: aspect_matcher.AspectMatcherModel):
    return aspect_matcher.aspect_matcher(request)


@router.post(f"/{date_extraction.date_extraction.__name__.lower()}")
def api_language_detection(request: date_extraction.DateExtractionModel):
    return date_extraction.date_extraction(request)


@router.post(f"/{email_extraction.email_extraction.__name__.lower()}")
def api_language_detection(request: email_extraction.EmailExtractionModel):
    return email_extraction.email_extraction(request)


@router.post(f"/{gazetteer.gazetteer.__name__.lower()}")
def api_language_detection(request: gazetteer.GazetteerModel):
    return gazetteer.gazetteer(request)


@router.post(f"/{hashtag_extraction.hashtag_extraction.__name__.lower()}")
def api_language_detection(request: hashtag_extraction.HashtagExtractionModel):
    return hashtag_extraction.hashtag_extraction(request)


@router.post(f"/{name_extraction.name_extraction.__name__.lower()}")
def api_language_detection(request: name_extraction.NameExtractionModel):
    return name_extraction.name_extraction(request)


@router.post(f"/{org_extraction.org_extraction.__name__.lower()}")
def api_language_detection(request: org_extraction.OrgExtractionModel):
    return org_extraction.org_extraction(request)


@router.post(f"/{price_extraction.price_extraction.__name__.lower()}")
def api_language_detection(request: price_extraction.PriceExtractionModel):
    return price_extraction.price_extraction(request)


@router.post(f"/{regex_extraction.regex_extraction.__name__.lower()}")
def api_language_detection(request: regex_extraction.RegexExtractionModel):
    return regex_extraction.regex_extraction(request)


@router.post(f"/{time_extraction.time_extraction.__name__.lower()}")
def api_language_detection(request: time_extraction.TimeExtractionModel):
    return time_extraction.time_extraction(request)


@router.post(f"/{url_extraction.url_extraction.__name__.lower()}")
def api_language_detection(request: url_extraction.UrlExtractionModel):
    return url_extraction.url_extraction(request)


@router.post(f"/{window_search.window_search.__name__.lower()}")
def api_language_detection(request: window_search.WindowSearchModel):
    return window_search.window_search(request)


@router.post('/ip_extractor')
def api_window_search(request: ip_extractor.IpExtractionModel):
    return ip_extractor.fn_ip_extractor(request)

