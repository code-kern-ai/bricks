
```python
import random

ATTRIBUTE: int 

def annotator_split(record):
    try:
        return random.randint(0, record[ATTRIBUTE]-1)
    except:
        print("Something went wrong. Please make sure, your desired maximal number is an Integer and bigger than 0.")


```
