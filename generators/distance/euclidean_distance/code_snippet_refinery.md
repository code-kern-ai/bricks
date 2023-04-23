```python
import numpy as np 
from numpy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer

ATTRIBUTE: str = "text" # only text attributes
SUBJECT_TEXT: str = "Ten amazing facts about the sun"

def euclidean_distance(record):
    text = record[ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string

    # Transform sentences to a vector
    tfidf = TfidfVectorizer()
    vects = tfidf.fit_transform([SUBJECT_TEXT.lower(), text.lower()])
    vects = vects.todense()
    vect_one, vect_two = np.squeeze(np.asarray(vects[0])), np.squeeze(np.asarray(vects[1]))

    # Return the calculated euclidean distance
    return np.linalg.norm(vect_one - vect_two)
```