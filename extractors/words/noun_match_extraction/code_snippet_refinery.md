```python
import re

ATTRIBUTE: str = "text" # only text attributes

def noun_match_extraction(record):
# instantiate empty lists to store already encountered words and for found matches 
    word_repo = []
    matches = []

    text = record[ATTRIBUTE].text

    # get noun chunks from spacy 
    nc = [i.text.lower() for i in record[ATTRIBUTE].noun_chunks]
    
    # loop through all noun chunks
    for noun_chunk in nc:
        print(noun_chunk)
        # if noun chunk has more than one word, take first word as a target word
        if len(noun_chunk.split()) >= 2:
            target_word = noun_chunk.split()[0]

            # if target word has been used before, stop process
            if target_word in word_repo:
                pass
            else:
                # pass word to repository to avoid duplicate use
                word_repo.append(target_word)

                # create regex_pattern with target word
                pattern = rf"\W*({target_word})\W*([^\s]+)"
            
                # extract the spans of all found matches
                for item in re.finditer(pattern, text):
                    start, end = item.span()
                    span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
                    yield "Noun chunk", span.start, span.end
        else:
            pass
```