```python
import tiktoken 

ATTRIBUTE: str = "text" # only text attributes
ENCODING_NAME: str = "cl100k_base"


def tiktoken_length_classifier(record):
    encoding = tiktoken.get_encoding(ENCODING_NAME)
    tokens = encoding.encode(record[ATTRIBUTE].text)
    num_tokens = len(tokens)
    print(num_tokens)

    if num_tokens < 64:
        return "short"
    elif num_tokens < 256:
        return "medium"
    else:
        return "long"
```