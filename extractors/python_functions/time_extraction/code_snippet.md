```python
def time_extraction(record):
    """Extracts times from a given text."""
    text = record["text"]
    regex = re.compile(
        r"(?:(?:[0-9]{1,2}(?::[0-9]{1,2}(?::[0-9]{1,2}:?)?)?)(?:(?: )?am|(?: )?pm|(?: )?AM|(?: )?PM)?)"
    )

    for match in regex.finditer(text.text):
        start, end = match.span()
        span = doc.char_span(start, end)
        yield "time", span.start, span.end
```