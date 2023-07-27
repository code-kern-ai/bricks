```python
import re
from typing import List
from flashtext import KeywordProcessor

ATTRIBUTE: str = "text" # only text attributes
KEYWORDS: List[str] = ["keyword1", "keyword2", "keyword3"]
LABEL: str = "keyword"

def keyword_extraction(record):
    
    text = record[ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.
    keyword_processor = KeywordProcessor()
    keyword_processor.add_keywords_from_list(KEYWORDS)
    keyword_found = keyword_processor.extract_keywords(text, span_info=True)
    
    if len(keyword_found) > 0:
        for keyword in keyword_found:
            start, end = re.match(rf"({keyword})", text).span()
            span = record[ATTRIBUTE].char_span(start, end)
            yield LABEL, span.start, span.end
```