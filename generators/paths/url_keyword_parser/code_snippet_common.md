```python
from typing import Optional, List, Set
import re
from urllib.parse import urlparse
from nltk.corpus import words
from nltk.corpus import stopwords

def url_keyword_parser(url:str, include_domain:bool=False, include_parameter:bool=True, check_valid_url:bool=False,remove_hex_like:bool=True)->List[str]:
    """
    Extracts keywords from a given URL.
    Keep in mind to prepare the global variables before calling this function.

    @param url: url to analyze
    @param include_domain: include URL domain in keyword scan
    @param include_parameter: include URL parameter in keyword scan
    @param check_valid_url: ensure valid URL pattern
    @param remove_hex_like: remove things that look like hex or numbers
    @return: list of keywords
    """
    if check_valid_url and not valid_url(url):
        return ["No valid URL"]
    url_obj = urlparse(url)
    keywords = extract_part(url_obj.path,remove_hex_like)
    if include_domain:
        keywords = keywords | extract_part(url_obj.netloc,remove_hex_like)
    if include_parameter:
        keywords = keywords | extract_part(url_obj.params,remove_hex_like) | extract_part(url_obj.query,remove_hex_like) | extract_part(url_obj.fragment,remove_hex_like)
    return list(keywords)

def extract_part(part:str,remove_hex_like:bool)->Set[str]:
    if not part:
        return set()
    
    remaining = set([w.lower() for w in re.split(split_regex,part) if len(w) > 0])
    must_keep = remaining & white_list
    remaining = remaining - english_stopwords
    if english_words:
        remaining = remaining & english_words
    if remove_hex_like:        
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

# performance enhancement via global preprepared values
url_regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
split_regex = None 
english_words = None
english_stopwords =None
white_list =None

def prepare_globals(word_white_list:Optional[List[str]]=None, regex:str="\W",remove_stopwords:bool=True, remove_none_english:bool=False):
    global white_list, split_regex, english_words, english_stopwords
    split_regex = re.compile(regex)
    if word_white_list:
        white_list = set(word_white_list)
    else:
        white_list = set()
    if remove_stopwords:
        english_stopwords = set(stopwords.words("english"))
    else:
        english_stopwords = set()
    if remove_none_english:
        english_stopwords =set(words.words())
    else:
        english_words = None
      
# ↑ necessary bricks stuff
# -----------------------------------------------------------------------------------------
# ↓ example implementation 
def example_integration():
    word_white_list = None # optional, specify words that are exempt form remove checks
    split_regex = "\W" # regex, default is any none word char e.g. \W|_ to include underscores
    remove_stopwords = True # only uses words that are NOT part of nltk.corpus stopwords
    remove_none_english = False # only use words that are part of nltk.corpus words

    prepare_globals(word_white_list, split_regex, remove_stopwords, remove_none_english)
    
    urls = ["https://stackoverflow.com/questions/19560498/faster-way-to-remove-stop-words-in-python","https://docs.kern.ai/refinery/evaluating-heuristics#best-practices"]

    for url in urls:
        print(f"url \"{url}\" contains:{url_keyword_parser(url)}")
example_integration() 


```