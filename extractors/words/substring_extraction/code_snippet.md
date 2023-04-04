```python
YOUR_SUBSTRING: str = "example"
YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LABEL: str = "substring"

def substring_extraction(record):
    """Extracts a common substring between two strings."""

    string1 = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.
    string2 = YOUR_SUBSTRING

    start_index = string1.find(string2)
    end_index = start_index + len(string2)

    if start_index != -1:
        span = record[YOUR_ATTRIBUTE].char_span(start_index, end_index, alignment_mode="expand")
        yield YOUR_LABEL, span.start, span.end
```