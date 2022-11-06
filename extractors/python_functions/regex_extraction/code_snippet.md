```python
import re

def detect_money_regex(record):
    YOUR_REGEX = "\$[0-9]+" # choose any regex here
    YOUR_ATTRIBUTE = "details" # choose any available attribute here
    YOUR_LABEL = "MONEY"

    def regex_search(pattern, string):
        """
        some helper function to easily iterate over regex matches
        """
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