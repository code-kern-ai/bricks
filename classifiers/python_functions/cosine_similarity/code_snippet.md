```python
import numpy as np 
from numpy import dot
from numpy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer

YOUR_ATTRIBUTE = "your-text"

def cosine_similarity(record):
    text_one = "10 amazing pasta recipes." # Change this to whatever you want to find similarities to
    text_two = record[YOUR_ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string

    # Transform sentences to a vector
    tfidf = TfidfVectorizer()
    vects = tfidf.fit_transform([text_one.lower(), text_two.lower()])
    vects = vects.todense()
    vect_one, vect_two = np.squeeze(np.asarray(vects[0])), np.squeeze(np.asarray(vects[1]))

    # Calculate the cosine similarity between the two vectors
    cos_sim = dot(vect_one, vect_two)/(norm(vect_one)*norm(vect_two))
    return cos_sim
```