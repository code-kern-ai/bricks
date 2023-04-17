```python
import numpy as np
from scipy.spatial.distance import hamming
from sklearn.feature_extraction.text import TfidfVectorizer

ATTRIBUTE: str = "text" # only text attributes
BASE_SENTENCE: str = "This is the base sentence you want to find the distances to." 

def hamming_distance(record):

    text_two = record[ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string

    tfidf = TfidfVectorizer().fit_transform([BASE_SENTENCE.lower(), text_two.lower()])

    dense = tfidf.toarray()
    vect_one, vect_two = np.squeeze(dense[0]), np.squeeze(dense[1])

    if vect_one.shape == () or vect_two.shape == ():
        pass

    else:
        return hamming(vect_one, vect_two)
```