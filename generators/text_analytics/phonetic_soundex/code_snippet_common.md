```python
from typing import List
import unicodedata

def phonetic_soundex(text:str)->List[str]:
    soundex_list = []
    for word in text.split():
        word = unicodedata.normalize("NFKD", word)
        word = word.upper()

        replacements = (
            ("BFPV", "1"),
            ("CGJKQSXZ", "2"),
            ("DT", "3"),
            ("L", "4"),
            ("MN", "5"),
            ("R", "6"),
        )
        result = [word[0]]
        count = 1

        # find would-be replacement for first character
        for lset, sub in replacements:
            if word[0] in lset:
                last = sub
                break
        else:
            last = None

        for letter in word[1:]:
            for lset, sub in replacements:
                if letter in lset:
                    if sub != last:
                        result.append(sub)
                        count += 1
                    last = sub
                    break
            else:
                if letter != "H" and letter != "W":
                    # leave last alone if middle letter is H or W
                    last = None
            if count == 4:
                break

        result += "0" * (4 - count)
        soundex_list.append("".join(result))
    return soundex_list

# ↑ necessary bricks stuff
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]

    for text in texts:
        print(f"Soundex of \"{text}\" is:{phonetic_soundex(text)}")
example_integration() 
```