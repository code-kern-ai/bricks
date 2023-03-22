```python
import numpy as np 
from numpy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_SUBJECT_TEXT: str = "Insert the sentence you want to compare your records to here!"

def manhattan_distance(record):
    text = record[YOUR_ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string

    # Transform sentences to a vector
    tfidf = TfidfVectorizer()
    vects = tfidf.fit_transform([YOUR_SUBJECT_TEXT.lower(), text.lower()])
    vects = vects.todense()
    vect_one, vect_two = np.squeeze(np.asarray(vects[0])), np.squeeze(np.asarray(vects[1]))

    # Return the calculated euclidean distance
    return sum(abs(val1-val2) for val1, val2 in zip(vect_one, vect_two))
```