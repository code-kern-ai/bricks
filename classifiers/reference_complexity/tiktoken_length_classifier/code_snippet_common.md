```python
import tiktoken

def tiktoken_length_classifier(text: str, encoding_model: str = "cl100k_base") -> str:
    """
    @param text: text you want to classify
    @param encoding_model: Name of the OpenAI encoding model. Is cl100k_base by default for GPT-4 and GPT-3.5 encodings. 
    @return: either 'short', 'medium' or 'long' depending on the amount of tokens in a text
    """
    encoding = tiktoken.get_encoding(encoding_model)
    tokens = encoding.encode(text)
    num_tokens = len(tokens)

    if num_tokens < 128:
        return "short"
    elif num_tokens < 1024:
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