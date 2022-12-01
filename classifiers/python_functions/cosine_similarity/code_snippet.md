```python
import numpy as np 
from numpy import dot
from numpy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer

YOUR_ATTRIBUTE: str = "text"
YOUR_SUBJECT_TEXT: str = "Ten amazing facts about the sun" # Change this to whatever you want to find similarities to

def cosine_similarity(record):
    text = record[YOUR_ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string

    # Transform sentences to a vector
    tfidf = TfidfVectorizer()
    vects = tfidf.fit_transform([YOUR_SUBJECT_TEXT.lower(), text.lower()])
    vects = vects.todense()
    vect_one, vect_two = np.squeeze(np.asarray(vects[0])), np.squeeze(np.asarray(vects[1]))

    # Calculate the cosine similarity between the two vectors
    cos_sim = dot(vect_one, vect_two)/(norm(vect_one)*norm(vect_two))
    if cos_sim < 0.5:
        return "Not similar"
    elif cos_sim > 0.5 and cos_sim < 0.75:
        return "Somewhat similar"
    else:
        return "Very similar"
```