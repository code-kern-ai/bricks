```python
import numpy as np
from scipy.spatial.distance import hamming
from sklearn.feature_extraction.text import TfidfVectorizer

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_BASE_SENTENCE: str = "This is the base sentence you want to find the distances to." 

def hamming_distance(record):

    text_one = YOUR_BASE_SENTENCE
    text_two = record[YOUR_ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string

    tfidf = TfidfVectorizer().fit_transform([text_one, text_two])

    dense = tfidf.toarray()
    vect_one, vect_two = np.squeeze(dense[0]), np.squeeze(dense[1])

    if vect_one.shape == () or vect_two.shape == ():
        pass

    else:
        hamming_distance_value = hamming(vect_one, vect_two)
        return hamming_distance_value
```