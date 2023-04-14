```python
import re
from urllib.parse import urlparse
from nltk.corpus import words
from nltk.corpus import stopwords

# replace this list with a list containing your data
text = ["https://stackoverflow.com/questions/19560498/faster-way-to-remove-stop-words-in-python"]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "include_domain": False, # include URL domain in keyword scan
    "include_parameter": True, # inlude URL parameter in keyword scan
    "check_valid_url": False, # ensure valid URL pattern
    "remove_none_english": False, # only use words that are part of nltk.corpus words
    "remove_stopwords": True, # only uses words that are not part of nltk.corpus stopwords
    "remove_hex_like": True, # remove things that look like hex or numbers
    "text_seperator": ", ", # joins resulting keywords on
    "split_regex": "\W", # possible regex, default is any none word char e.g. \W|_ to include underscores
    "word_white_list": None # optional, specify words that are exempt form remove checks
}

def url_keyword_parser(record):
    parsed_urls = []
    for entry in record["text"]:
        if not isinstance(entry,str):
            url = url.text
        if record["check_valid_url"] and not valid_url(url):
            parsed_urls.append("No valid URL")
        url_obj = urlparse(entry)
        keywords = extract_part(url_obj.path)
        if record["include_domain"]:
            keywords = keywords | extract_part(url_obj.netloc)
        if record["include_parameter"]:
            keywords = keywords | extract_part(url_obj.params) | extract_part(url_obj.query) | extract_part(url_obj.fragment)
        if not record["text_seperator"]:
            parsed_urls.append(" ".join(keywords))
        parsed_urls.append(record["text_seperator"].join(keywords))
    return {"parsedUrl": parsed_urls}

def extract_part(part):
    if not part:
        return set()
    
    remaining = set([w.lower() for w in re.split(split_regex,part) if len(w) > 0])
    must_keep = remaining & white_list
    if record["remove_stopwords"]:
        remaining = remaining - english_stopwords
    if record["remove_none_english"]:
        remaining = remaining & english_words
    if record["remove_hex_like"]:        
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
split_regex = re.compile(record["split_regex"]) 
english_words = set(words.words()) if record["remove_none_english"] else None
english_stopwords = set(stopwords.words("english")) if record["remove_stopwords"]  else None
white_list = set(record["word_white_list"]) if record["word_white_list"] else set()
```