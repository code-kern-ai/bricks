```python
import textstat
from collections import Counter

ATTRIBUTE: str = "text" # only text attributes
TARGET_LANGUAGE: str = "en" # iso codes

def chunked_sentence_complexity(record):
    complexities = []
    for sent in record[ATTRIBUTE].sents:
        # Apply the complexity function to each sentence
        complexity = sentence_complexity(sent.text)
        complexities.append(complexity)

    counter = Counter(complexities)
    
    # aggregating the complexity
    complexity_scores = {"very easy": 1, "easy": 2, "fairly easy": 3, "standard": 4, "fairly difficult": 5, "difficult": 6, "very difficult": 7}

    total_score = 0
    total_count = 0
    for comp, count in counter.items():
        total_score += complexity_scores[comp] * count
        total_count += count

    # weighted average complexity
    average_complexity = total_score / total_count

    # create a reverse mapping from scores to complexity levels
    reverse_mapping = {v: k for k, v in complexity_scores.items()}

    # find the closest complexity level to the average complexity
    closest_complexity = min(reverse_mapping.keys(), key=lambda x: abs(x - average_complexity))
    return reverse_mapping[closest_complexity]

def sentence_complexity(text):
    score = textstat.flesch_reading_ease(text)
    if score < 30:
        return "very difficult"
    if score < 50:
        return "difficult"
    if score < 60:
        return "fairly difficult"
    if score < 70:
        return "standard"
    if score < 80:
        return "fairly easy"
    if score < 90:
        return "easy"        
    return "very easy"

if TARGET_LANGUAGE is not None:
    textstat.set_lang(TARGET_LANGUAGE)
```