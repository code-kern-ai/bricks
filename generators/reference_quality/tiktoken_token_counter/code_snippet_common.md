```python
import tiktoken

def tiktoken_token_counter(text: str, encoding_name: str = "cl100k_base") -> int:
    """
    @param text: Text you want to count the number of tokens in
    @return: Integer with the token count
    """
    encoding = tiktoken.get_encoding(encoding_name)
    tokens = encoding.encode(text)
    return len(tokens)

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["This is a short text with few tokens.", "This is a second short text"]
    for text in texts:
        print(f"\"{text}\" -> {tiktoken_token_counter(text)}")

example_integration()
```