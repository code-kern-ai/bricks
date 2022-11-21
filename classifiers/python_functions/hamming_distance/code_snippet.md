```python
import numpy as np
from pydantic import BaseModel
from scipy.spatial.distance import hamming
from sklearn.feature_extraction.text import TfidfVectorizer

BASE_SENTENCE = "This is the base sentence you want to find the distances to." 
YOUR_ATTRIBUTE = "text"

def hamming_distance(record):

    text_one = BASE_SENTENCE
    text_two = record[YOUR_ATTRIBUTE].text

    tfidf = TfidfVectorizer().fit_transform([text_one, text_two])

    dense = tfidf.toarray()
    vect_one, vect_two = np.squeeze(dense[0]), np.squeeze(dense[1])

    hamming_distance = hamming(vect_one, vect_two)
    return hamming_distance
```