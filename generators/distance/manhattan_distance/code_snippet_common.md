```python
import numpy as np 
from numpy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer

def manhattan_distance(base_text: str, compare_text:str) -> float:
    """
    @param base_text: base text
    @param compare_text: text to compare to
    @return: the hamming distance between the two texts
    """
    tfidf = TfidfVectorizer()
    vects = tfidf.fit_transform([base_text.lower(), compare_text.lower()])
    vects = vects.todense()
    vect_one, vect_two = np.squeeze(np.asarray(vects[0])), np.squeeze(np.asarray(vects[1]))

    return sum(abs(val1-val2) for val1, val2 in zip(vect_one, vect_two))

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 
def example_integration():
    texts = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]
    for textA in texts:
        for textB in texts:
            print(f"manhattan distance between \"{textA}\" and \"{textB}\" is {manhattan_distance(textA, textB)}")

example_integration()
```