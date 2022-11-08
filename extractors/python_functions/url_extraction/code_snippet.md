```python
def url_extraction(record):
    text = record["your-text"]
    regex_pattern = re.compile(r"(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+")

    for match in regex_pattern.finditer(text.text):
        start, end = match.span()
        span = text.char_span(start, end)
        yield "url", span.start, span.end
```