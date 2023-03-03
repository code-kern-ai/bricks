import re
from urllib.parse import urlparse
from nltk.corpus import words
from nltk.corpus import stopwords
from typing import List
from pydantic import BaseModel

INPUT_EXAMPLE = {
    "url": "His text contaisn some speling errors.",
    "includeDomain": True,
    "includeParameter": True,
    "checkValidUrl": True,
    "removeNoneEnglish": False,
    "removeStopwords": True,
    "removeHexLike": True,
    "textSeperator": ", ",
    "splitRegex": "\W",
    "wordWhiteList": ["heuristics"]
}

class UrlParserModel(BaseModel):
    url: str
    includeDomain: bool = True
    includeParameter: bool = True
    checkValidUrl: bool = True
    removeNoneEnglish: bool = False
    removeStopwords: bool = True
    removeHexLike: bool = True
    textSeperator: str = ", "
    splitRegex: str = "\W"
    

    class Config:
        schema_extra = {
            "example": INPUT_EXAMPLE,
        }

def url_parser(req: UrlParserModel):
    url = req.url
    if req.checkValidUrl and not valid_url(url):
        return ""
    url_obj = urlparse(url)
    keywords = extract_part(url_obj.path)
    if req.includeDomain:
        keywords = keywords | extract_part(url_obj.netloc)
    if req.includeParameter:
        keywords = keywords | extract_part(url_obj.params) | extract_part(url_obj.query) | extract_part(url_obj.fragment)
    if not req.textSeperator:
        return " ".join(keywords)
    return req.textSeperator.join(keywords)

def extract_part(part, req: UrlParserModel):
    if not part:
        return set()
    
    remaining = set([w.lower() for w in re.split(split_regex,part) if len(w) > 0])
    must_keep = remaining & white_list
    if req.removeStopwords:
        remaining = remaining - english_stopwords
    if req.removeNoneEnglish:
        remaining = remaining & english_words
    if req.removeHexLike:        
        remaining = {w for w in remaining if not is_hex(w)}
        
    return remaining | must_keep

def valid_url(url):
    if not url:
        return False
    return re.match(url_regex, url) is not None

def is_hex(part):
    try:
        int(part, 16)
        return True
    except ValueError:
        return False

# performance enhancement via prepreparation of regex & sets
def do_regex(req: UrlParserModel):
    url_regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    split_regex = re.compile(req.splitRegex) 
    english_words = set(words.words())
    english_stopwords = set(stopwords.words("english"))
    white_list = set(req.wordWhiteList)
    return white_list, english_stopwords, english_words, split_regex, url_regex

white_list, english_stopwords, english_words, split_regex, url_regex = do_regex(req)