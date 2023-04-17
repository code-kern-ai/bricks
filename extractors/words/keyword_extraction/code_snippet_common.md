```python
from typing import List, Tuple
from flashtext import KeywordProcessor

def keyword_extraction(text: str, keywords: list, extraction_keyword: str) -> List[Tuple[str,int]]:
    """
    @param text: the input text
    @param extraction_keyword: the label that is assigned to extracted words
    @param keywords: a list of keywords you want to extract  
    @return: similar keywords
    """
    keyword_processor = KeywordProcessor()
    keyword_processor.add_keywords_from_list(keywords)

    keyword_positions = []
    keyword_found = keyword_processor.extract_keywords(text, span_info=True)
    for keyword in keyword_found:
        keyword_positions.append((extraction_keyword, keyword[1], keyword[2]))
    return keyword_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["I had such an amazing time in the movies. The popcorn was delicious as well.", "I love books!"]
    extraction_keyword = "movie related"
    keywords = ["movies", "popcorn"]
    for text in texts:
        found = keyword_extraction(text, keywords, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```