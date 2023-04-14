```python
from typing import List

def lookup_list(text:str, lookup_values:List[str], return_label:str) -> str:    
    """
    @param text: text you want to look through
    @param lookup_values: values to check for in param text
    @param return_label: label to return
    @return: return_label if any of the lookup_values are in text, else None
    """
    for item in lookup_values:
        if item.lower() in text.lower():
            return return_label

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 
def example_integration():
    texts = ["Please contact john@kern.ai to get more info.", "This is a negative text."]
    lookup_values = ["john@kern.ai", "jane@kern.ai"]
    label = "in lookup"
    
    for text in texts:
        found = lookup_list(text, lookup_values, label)
        if found:
            print(f"text: \"{text}\" has label \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have the lookup values")

example_integration()
```
