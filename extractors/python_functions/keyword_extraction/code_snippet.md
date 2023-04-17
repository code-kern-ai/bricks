```python
import re
from flashtext import KeywordProcessor
from typing import List

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_KEYWORDS: List[str] = ["keyword1", "keyword2", "keyword3"]
YOUR_LABEL: str = "keyword"

def keyword_extraction(record):
    
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.
    keyword_processor = KeywordProcessor()
    keyword_processor.add_keywords_from_list(YOUR_KEYWORDS)
    keyword_found = keyword_processor.extract_keywords(text, span_info=True)
    
    for keyword in keyword_found:
        start, end = re.match(rf"({keyword})").span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end)
        yield YOUR_LABEL, span.start, span.end
```