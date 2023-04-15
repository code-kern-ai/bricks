```python
import numpy as np 
from scipy.spatial.distance import hamming
from sklearn.feature_extraction.text import TfidfVectorizer

def hamming_distance(base_text: str, compare_text:str) -> float:
    """
    @param base_text: base text
    @param compare_text: text to compare to
    @return: the hamming distance between the two texts
    """
    tfidf = TfidfVectorizer().fit_transform([base_text.lower(), compare_text.lower()])

    dense = tfidf.toarray()
    vect_one, vect_two = np.squeeze(dense[0]), np.squeeze(dense[1])

    if vect_one.shape == () or vect_two.shape == ():
        pass

    else:
        return hamming(vect_one, vect_two)

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["Let's eat, Grandpa!", "Grandpa is eating!", "Apple pie is also very delicious."]
    for textA in texts:
        for textB in texts:
            print(f"hamming distance between \"{textA}\" and \"{textB}\" is {hamming_distance(textA, textB)}")

example_integration()
```