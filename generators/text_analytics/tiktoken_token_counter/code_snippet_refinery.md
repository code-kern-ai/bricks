```python
import tiktoken 

ATTRIBUTE: str = "text" # only text attributes
ENCODING_NAME: str = "cl100k_base"

def tiktoken_token_counter(record):
    encoding = tiktoken.get_encoding(ENCODING_NAME)
    tokens = encoding.encode(record[ATTRIBUTE].text)
    return len(tokens)
```