```python
from flashtext import KeywordProcessor

# replace this list with a list containing your data
text = ["I had such an amazing time in the movies. The popcorn was delicious as well."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "keywords": ["movies", "popcorn"],
    "label": "goodbye",
}

def keyword_extraction(record: dict) -> dict:
    keyword_processor = KeywordProcessor()
    keyword_processor.add_keywords_from_list(record["keywords"])

    keyword_positions = []
    text_id = 0
    for entry in record["text"]:
        keyword_found = keyword_processor.extract_keywords(entry, span_info=True)
        for keyword in keyword_found:
            keyword_positions.append({f"text_{text_id}" :[keyword[0], keyword[1], keyword[2]]})
        text_id += 1
    return {"extraction": keyword_positions}
```