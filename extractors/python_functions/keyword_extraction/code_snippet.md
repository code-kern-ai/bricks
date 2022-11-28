```python
from flashtext import KeywordProcessor

YOUR_ATTRIBUTE = "text"
YOUR_KEYWORDS = ["keyword1", "keyword2", "keyword3"]

def keyword_extraction(record):
    
    text = record[YOUR_ATTRIBUTE].text
    keyword_processor = KeywordProcessor()
    keyword_processor.add_keywords_from_list(YOUR_KEYWORDS)
    keywords_found = keyword_processor.extract_keywords(text, span_info=True)
    
    return keywords_found
```