```python
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

def sumy__website_summarizer(url: str, language: str, sentence_count: int) -> str:
    """
    @param url: the url of the website to summarize
    @param language: the language of the website to summarize
    @param sentence_count: the number of sentences to return
    @return: the summarized text
    """  
    parser = HtmlParser.from_url(url, Tokenizer(language)) 
    stemmer = Stemmer(language)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(language)
    summary = summarizer(parser.document, sentence_count)
    return " ".join([str(sentence) for sentence in summary])

# ↑ necessary bricks stuff
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    url = "https://en.wikipedia.org/wiki/capybara"
    language = "english"
    print(f"the text from \"{url}\" was summarized into -> \n {sumy__website_summarizer(url, language, 5)}")
example_integration()
```