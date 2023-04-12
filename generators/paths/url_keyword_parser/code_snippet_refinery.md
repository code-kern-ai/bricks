```python
import re
from urllib.parse import urlparse
from nltk.corpus import words
from nltk.corpus import stopwords
from typing import List

ATTRIBUTE:str = "text" # only text like attributes
INCLUDE_DOMAIN:bool = False # include URL domain in keyword scan
INCLUDE_PARAMETER:bool = True # inlude URL parameter in keyword scan
CHECK_VALID_URL:bool = False # ensure valid URL pattern
REMOVE_NONE_ENGLISH:bool = False # only use words that are part of nltk.corpus words
REMOVE_STOPWORDS:bool = True # only uses words that are not part of nltk.corpus stopwords
REMOVE_HEX_LIKE:bool = True # remove things that look like hex or numbers
TEXT_SEPERATOR:str = ", " # joins resulting keywords on
SPLIT_REGEX:str = "\W" # possible regex, default is any none word char e.g. \W|_ to include underscores
WORD_WHITE_LIST:List[str] = None # optional, specify words that are exempt form remove checks

def url_keyword_parser(record):
    url = record[ATTRIBUTE]
    if not isinstance(url,str):
        url = url.text
    if CHECK_VALID_URL and not valid_url(url):
        return ""
    url_obj = urlparse(url)
    keywords = extract_part(url_obj.path)
    if INCLUDE_DOMAIN:
        keywords = keywords | extract_part(url_obj.netloc)
    if INCLUDE_PARAMETER:
        keywords = keywords | extract_part(url_obj.params) | extract_part(url_obj.query) | extract_part(url_obj.fragment)
    if not TEXT_SEPERATOR:
        return " ".join(keywords)
    return TEXT_SEPERATOR.join(keywords)

def extract_part(part):
    if not part:
        return set()
    
    remaining = set([w.lower() for w in re.split(split_regex,part) if len(w) > 0])
    must_keep = remaining & white_list
    if REMOVE_STOPWORDS:
        remaining = remaining - english_stopwords
    if REMOVE_NONE_ENGLISH:
        remaining = remaining & english_words
    if REMOVE_HEX_LIKE:        
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
url_regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
split_regex = re.compile(SPLIT_REGEX) 
english_words = set(words.words()) if REMOVE_NONE_ENGLISH else None
english_stopwords = set(stopwords.words("english")) if REMOVE_STOPWORDS  else None
white_list = set(WORD_WHITE_LIST) if WORD_WHITE_LIST else set()
```
