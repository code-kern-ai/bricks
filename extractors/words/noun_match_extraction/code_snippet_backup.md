```python 
import re
import spacy

# replace this list with a list containing your data
text = ["Leo likes tasty pizza. Mary loves delicious cake. And Moritz loves tasty bread."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
}

def noun_match_extraction(record):
    nlp = spacy.load("en_core_web_sm")

    word_repo = []
    noun_positions = []
    text_id = 0
    for entry in record["text"]:
        doc = nlp(entry)
        # get noun chunks from spacy 
        nc = [i.text.lower() for i in doc.noun_chunks]
        
        # loop through all noun chunks
        for noun_chunk in nc:
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
                    for item in re.finditer(pattern, entry):
                        start, end = item.span()
                        span = doc.char_span(start, end, alignment_mode="expand")
                        noun_positions.append({f"text_{text_id}": ["Noun chunk", span.start, span.end]})
        text_id += 1
    return {"extractions": noun_positions}
```