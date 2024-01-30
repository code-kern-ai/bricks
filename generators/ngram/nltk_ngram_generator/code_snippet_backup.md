```python
import spacy
from nltk.util import ngrams

# replace this list with a list containing your data
text = ["Despite the unpredictable weather, the enthusiastic crowd gathered at the park for the annual summer festival, eagerly anticipating an evening filled with music, food, and vibrant celebrations."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "sentence": text,
    "ngram_size": 2
}

def nltk_ngram_generator(record):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(record.sentence)
    tokens  =[token.text for token in doc]
    n_grams = list(ngrams(tokens, record["ngram_size"]))

    return {"n_grams": n_grams}
```


