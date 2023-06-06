```python
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

ATTRIBUTE: str = "url"
LANGUAGE: str = "english"
SENTENCE_COUNT: int = 5

def sumy_website_summarizer(record):
    parser = HtmlParser.from_url(record[ATTRIBUTE], Tokenizer(LANGUAGE)) 
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    summary = summarizer(parser.document, SENTENCE_COUNT)
    return " ".join([str(sentence) for sentence in summary])
```