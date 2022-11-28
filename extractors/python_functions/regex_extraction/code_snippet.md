```python
import re

def regex_extraction(record):
    YOUR_REGEX = r"\$[0-9]+" # Choose any regex here
    YOUR_ATTRIBUTE = "details" # Choose any available attribute here
    YOUR_LABEL = "MONEY" # Choose any available label here

    def regex_search(pattern, string):
        prev_end = 0
        while True:
            match = re.search(pattern, string)
            if not match:
                break

            start, end = match.span()
            yield start + prev_end, end + prev_end

            prev_end += end
            string = string[end:]
            
    for start, end in regex_search(YOUR_REGEX, record[YOUR_ATTRIBUTE].text):
        span = record[YOUR_ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield YOUR_LABEL, span.start, span.end
```