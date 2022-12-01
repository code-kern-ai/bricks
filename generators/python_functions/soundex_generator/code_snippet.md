```python
import unicodedata

#currently only english language is supported here
#reach out to us if this should be extended for other languages

YOUR_ATTRIBUTE: str = "text" #only text attributes

def soundex_generator(record):
    """Converts an english word into a phonetic SoundEx representation, for example to store names."""

    word = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string. 
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
    yield "".join(result)
```