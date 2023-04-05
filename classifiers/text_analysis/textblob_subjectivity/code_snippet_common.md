```python
# expects labeling task to have labels ["subjective", "rather subjective" ,"neutral", "rather objective", "objective"]
from textblob import TextBlob

# replace this list with a list containing your data
text = ["These are the worst fries every.", "Trees are made of wood."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
}

def textblob_subjectivity(record): 
    subjectivity = []
    for entry in record["text"]:   
        blob = TextBlob(entry) 
        subjectivity.append(get_mapping_subjectivity(blob.sentiment.subjectivity * 100))
    return {"subjectivity": subjectivity}

def set_all(d, keys, value):
    for k in keys:
        d[k] = value

def get_mapping_subjectivity(score):
    if score < 0:
        return outcomes[0]
    if score > 100:
        return outcomes[100]
    return outcomes[int(score)]


outcomes = {}
set_all(outcomes, range(80, 100 + 1), "subjective")
set_all(outcomes, range(60, 80), "rather subjective")
set_all(outcomes, range(40, 60), "neutral")
set_all(outcomes, range(20, 40), "rather objective")
set_all(outcomes, range(0, 20), "objective")
```