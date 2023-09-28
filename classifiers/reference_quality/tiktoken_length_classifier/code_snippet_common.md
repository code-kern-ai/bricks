```python
import tiktoken

def tiktoken_length_classifier(text: str, encoding_name: str = "cl100k_base") -> str:
    encoding = tiktoken.get_encoding(encoding_name)
    tokens = encoding.encode(text)
    num_tokens = len(tokens)
    print(num_tokens)

    if num_tokens < 64:
        return "short"
    elif num_tokens < 256:
        return "medium"
    else:
        return "long"

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["This is a short text with few tokens.", "This is a second short text"]
    for text in texts:
        print(f"\"{text}\" -> {tiktoken_length_classifier(text)}")

example_integration()
```