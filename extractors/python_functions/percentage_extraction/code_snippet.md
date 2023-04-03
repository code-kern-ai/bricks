```python
import re

YOUR_REGEX: str = r"(-?\d+(?:[.,]\d*)?|-?[.,]\d+)%" # this will caputre all percentages
YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LABEL: str = "percentage" # Choose any available label here

def percentage_extraction(record):

    def regex_search(pattern, string):
        prev_end = 0
        while True:
            match = re.search(pattern, string)
            if not match:
                break

            start_, end_ = match.span()
            yield start_ + prev_end, end_ + prev_end

            prev_end += end_
            string = string[end_:]
            
    for start, end in regex_search(YOUR_REGEX, record[YOUR_ATTRIBUTE].text):
        span = record[YOUR_ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield YOUR_LABEL, span.start, span.end
```