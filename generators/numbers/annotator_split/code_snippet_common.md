```python
import random

def annotator_split(record) -> int:
    return random.randint(0, record-1)

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    max_number = [3,5,1000,43694,1,14,0,13.5]
    for number in max_number:
        print(f"the random number in the maximal number-range of {number} is {annotator_split(number)}")

example_integration()
```