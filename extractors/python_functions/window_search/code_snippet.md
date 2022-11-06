```python
def window_cue_search(doc):
    YOUR_WINDOW = 4 # choose any window size here
    YOUR_LABEL = "PERSON"
    YOUR_ATTRIBUTE = "details" # choose any available attribute here
    LOOKUP_VALUES = ["join"] # this could also be coming from a knowledge base via `import knowledge`
    for chunk in record[YOUR_ATTRIBUTE].noun_chunks:
        left_bound = max(chunk.sent.start, chunk.start - (YOUR_WINDOW // 2) +1)
        right_bound = min(chunk.sent.end, chunk.end + (YOUR_WINDOW // 2) + 1)
        window_doc = record[YOUR_ATTRIBUTE][left_bound: right_bound]
        if any([term in window_doc.text for term in LOOKUP_VALUES]):
            yield YOUR_LABEL, chunk.start, chunk.end
```