```python
import numpy as np 
from numpy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_SUBJECT_TEXT: str = "Ten amazing facts about the sun"

def euclidean_distance(record):
    text = record[YOUR_ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string

    # Transform sentences to a vector
    tfidf = TfidfVectorizer()
    vects = tfidf.fit_transform([YOUR_SUBJECT_TEXT.lower(), text.lower()])
    vects = vects.todense()
    vect_one, vect_two = np.squeeze(np.asarray(vects[0])), np.squeeze(np.asarray(vects[1]))

    # Return the calculated euclidean distance
    return str(np.linalg.norm(vect_one - vect_two))
```