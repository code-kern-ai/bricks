```python

import numpy as np 
from numpy import dot
from numpy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer

def cosine_similarity(base_text: str, compare_text:str) -> str:
    """
    @param base_text: base text
    @param compare_text: text to compare to
    @return: either 'Not similar', 'Somewhat similar' or 'Very similar' depending on the score
    """
    tfidf = TfidfVectorizer()
    vects = tfidf.fit_transform([base_text.lower(), compare_text.lower()])
    vects = vects.todense()
    vect_one, vect_two = np.squeeze(np.asarray(vects[0])), np.squeeze(np.asarray(vects[1]))

    cos_sim = dot(vect_one, vect_two)/(norm(vect_one)*norm(vect_two))
    return lookup_label(cos_sim)

def lookup_label(score:float)->str:
    if score < .5:
        return "Not similar"
    if score < .75:
        return "Somewhat similar"
    return "Very similar"


# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 
def example_integration():
    texts = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]
    for textA in texts:
        for textB in texts:
            print(f"\"{textA}\" and \"{textB}\" are {cosine_similarity(textA, textB)}")

example_integration()
```