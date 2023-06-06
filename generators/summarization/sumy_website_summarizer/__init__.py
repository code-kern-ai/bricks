from pydantic import BaseModel
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

INPUT_EXAMPLE = {
    "url": "https://en.wikipedia.org/wiki/capybara",
    "language": "english",
    "sentence_count": 5,
}

class SumyWebsiteSummarizerModel(BaseModel):
    url: str
    language: str = "english"
    sentence_count: int = 5

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}

def sumy_website_summarizer(request: SumyWebsiteSummarizerModel):  
    """Summarize a website using sumy"""
    parser = HtmlParser.from_url(request.url, Tokenizer(request.language))
    stemmer = Stemmer(request.language)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(request.language)
    summary = summarizer(parser.document, request.sentence_count)
    return " ".join([str(sentence) for sentence in summary])
