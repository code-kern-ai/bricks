```python
from collections import Counter
import spacy

# replace this list with a list containing your data
text = ["APPL went down by 5% in the past two weeks. Shareholders are concerned over the continued recession since APPL and NASDAQ have been hit hard by this recession. Risks pertaining to short-selling are pouring in as APPL continues to depreciate. If the competitors come together and start short-selling, the stock can face calamity."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "n_words": 5,
}

def most_frequent_words(record):
    nlp = spacy.load("en_core_web_sm")
    frequent_words = []
    for entry in record["text"]:
        doc = nlp(entry)
        words = [token.text for token in doc if not token.is_stop and not token.is_punct]
        frequent_words.append(str(Counter(words).most_common(record["n_words"])).strip("[]"))
    return {"words": frequent_words}
```
