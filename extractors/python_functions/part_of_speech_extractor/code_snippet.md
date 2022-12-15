```python
from typing import List, Tuple

YOUR_ATTRIBUTE: str = "text" # only text attributes

def part_of_speech_extractor(record) -> List[Tuple[str, int, int]]:
    """Yields POS tags using spaCy."""

    doc = record[YOUR_ATTRIBUTE]

    for token in doc:
            pos = token.pos_
            if pos:
                yield pos, token.i, token.i+1
```