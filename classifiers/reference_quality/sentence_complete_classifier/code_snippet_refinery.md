```python
ATTRIBUTE: str = "text"

def sentence_complete_classifier(record):
    classifications = []
    for sent in record[ATTRIBUTE].sents:
        if sent[0].is_title and sent[-1].is_punct:
            has_noun = 2
            has_verb = 1
            for token in sent:
                if token.pos_ in ["NOUN", "PROPN", "PRON"]:
                    has_noun -= 1
                elif token.pos_ == "VERB":
                    has_verb -= 1
            if has_noun < 1 and has_verb < 1:
                classifications.append("complete")
            else:
                classifications.append("incomplete")
        else:
            classifications.append("incomplete")

    # Aggregation logic
    if all(classification == "complete" for classification in classifications):
        return "complete"
    elif all(classification == "incomplete" for classification in classifications):
        return "incomplete"
    elif any(classification == "incomplete" for classification in classifications):
        return "partly complete"
```