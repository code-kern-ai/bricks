```python
import spacy

loaded_models = {}
def load_spacy(spacy_model):
    if spacy_model not in loaded_models:
        loaded_models[spacy_model] = spacy.load(spacy_model)
    return loaded_models[spacy_model]

def sentence_complete_classifier(text: str, spacy_model: str = "en_core_web_sm") -> str:
    """
    @param text: The text to classify
    @param spacy_model: A spaCy language model
    @returns: Classification for the text based on all sentences
    """
    nlp = load_spacy(spacy_model)
    doc = nlp(text)

    classifications = []
    for sent in doc.sents:
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


# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = [
        "This is a complete sentence written by me!",
        "The first sentence I have written is complete! However, the second one...",
        "and they rand over here and then"
    ]
    for text in texts: 
        print(f"The text '{text}' is -> {sentence_complete_classifier(text)}")

example_integration()
```