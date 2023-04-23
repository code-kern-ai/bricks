```python
SUBSTRING: str = "example"
ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "substring"

def substring_extraction(record):
    """Extracts a common substring between two strings."""

    string1 = record[ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.
    string2 = SUBSTRING

    start_index = string1.find(string2)
    end_index = start_index + len(string2)

    if start_index != -1:
        span = record[ATTRIBUTE].char_span(start_index, end_index, alignment_mode="expand")
        yield LABEL, span.start, span.end
```