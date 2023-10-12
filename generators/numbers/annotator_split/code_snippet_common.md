```python
import random

def annotator_split(record) -> int:
    return random.randint(0, record-1)

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    max_number = [2, 4, 6, 8, 10]
    for number in max_number:
        print(f"the random number in the maximal number-range of {number} is {annotator_split(number)}")

example_integration()
```