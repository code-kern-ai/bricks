```python
# expects labeling task to have labels ["very easy", "easy" ,"fairly easy", "standard", "fairly difficult", "difficult", "very difficult"]
import textstat

# replace this list with a list containing your data
text = ["Doctors from Stockhold University invent cure for rare disease.", "Mary had a little lamb."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "traget_language": "en", # accepts ISO country codes
}

def sentence_complexity(record):
    complexity = []
    for entry in record["text"]:
        sentence_complexity_score = textstat.flesch_reading_ease(entry)
        sentence_complexity = get_mapping_complexity(sentence_complexity_score)
        complexity.append(sentence_complexity)
    return {"complexity": complexity}

def set_all(d, keys, value):
    for k in keys:
        d[k] = value
    
def get_mapping_complexity(score):
    if score < 0:
        return outcomes[0]
    if score > 100:
        return outcomes[100]
    return outcomes[int(score)]

if record["traget_language"] is not None:
    textstat.set_lang(record["traget_language"])

outcomes = {}
set_all(outcomes, range(90, 100 + 1), "very easy")
set_all(outcomes, range(80, 90), "easy")
set_all(outcomes, range(70, 80), "fairly easy")
set_all(outcomes, range(60, 70), "standard")
set_all(outcomes, range(50, 60), "fairly difficult")
set_all(outcomes, range(30, 50), "difficult")
set_all(outcomes, range(0, 30), "very difficult")
```