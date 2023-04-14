```python
from Levenshtein import distance as levenshtein_dist

def levenshtein_distance(base_text: str, compare_text:str, weight_insertion:int=1,weight_deletion:int=1,weight_substitution:int=1) -> float:
    """
    @param base_text: base text
    @param compare_text: text to compare to
    @param weight_insertion: weight for insertion
    @param weight_deletion: weight for deletion
    @param weight_substitution: weight for substitution
    @return: the levenshtein distance between the two texts
    """
    weights_tuple = (weight_insertion, weight_deletion, weight_substitution)
    return levenshtein_dist(base_text, compare_text, weights=weights_tuple)

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 
def example_integration():
    texts = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]
    for textA in texts:
        for textB in texts:
            print(f"levenshtein distance between \"{textA}\" and \"{textB}\" is {levenshtein_distance(textA, textB)}")

example_integration()
```