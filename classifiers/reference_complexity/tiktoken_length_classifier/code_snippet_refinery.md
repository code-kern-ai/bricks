```python
import tiktoken 

ATTRIBUTE: str = "text" # only text attributes
ENCODING_MODEL: str = "cl100k_base"

encoding = tiktoken.get_encoding(ENCODING_MODEL)

def tiktoken_length_classifier(record):
    tokens = encoding.encode(record[ATTRIBUTE].text)
    num_tokens = len(tokens)

    if num_tokens < 128:
        return "short"
    elif num_tokens < 1024:
        return "medium"
    else:
        return "long"
```