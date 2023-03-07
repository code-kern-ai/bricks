```python
import re
from urllib.parse import urlparse
from nltk.corpus import words
from nltk.corpus import stopwords
from typing import List

YOUR_ATTRIBUTE:str = "url"
YOUR_INCLUDE_DOMAIN:bool = True
YOUR_INCLUDE_PARAMETER:bool = True
YOUR_CHECK_VALID_URL:bool = True
YOUR_REMOVE_NONE_ENGLISH:bool = False # only uses words that are part of nltk.corpus words
YOUR_REMOVE_STOPWORDS:bool = True # only uses words that are not part of nltk.corpus stopwords
YOUR_REMOVE_HEX_LIKE:bool = True # remove things that look like hex or numbers
YOUR_TEXT_SEPERATOR:str = ", "
YOUR_SPLIT_REGEX:str = "\W" # possible regex, default is any none word char e.g. [^\w]|_ to include underscores
YOUR_WORD_WHITE_LIST:List[str] = ["heuristics"]

def url_keyword_parser(record):
    url = record[YOUR_ATTRIBUTE]
    if YOUR_CHECK_VALID_URL and not valid_url(url):
        return ""
    url_obj = urlparse(url)
    keywords = extract_part(url_obj.path)
    if YOUR_INCLUDE_DOMAIN:
        keywords = keywords | extract_part(url_obj.netloc)
    if YOUR_INCLUDE_PARAMETER:
        keywords = keywords | extract_part(url_obj.params) | extract_part(url_obj.query) | extract_part(url_obj.fragment)
    if not YOUR_TEXT_SEPERATOR:
        return " ".join(keywords)
    return YOUR_TEXT_SEPERATOR.join(keywords)

def extract_part(part):
    if not part:
        return set()
    
    remaining = set([w.lower() for w in re.split(split_regex,part) if len(w) > 0])
    must_keep = remaining & white_list
    if YOUR_REMOVE_STOPWORDS:
        remaining = remaining - english_stopwords
    if YOUR_REMOVE_NONE_ENGLISH:
        remaining = remaining & english_words
    if YOUR_REMOVE_HEX_LIKE:        
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
split_regex = re.compile(YOUR_SPLIT_REGEX) 
english_words = set(words.words())
english_stopwords = set(stopwords.words("english"))
white_list = set(YOUR_WORD_WHITE_LIST)
```
