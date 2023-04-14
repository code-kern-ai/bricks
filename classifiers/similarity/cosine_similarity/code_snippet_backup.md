```python
# expects labeling task to have labels ["Not similar", "Somewhat similar", "Very similar"]
import numpy as np 
from numpy import dot
from numpy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer

# replace this list with a list containing your data
text = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "your_text": text,
}

# function for the euclidean distance, should return a n*n matrix. n being the number of texts
def cosine_similarity(record: dict) -> dict:
    all_similarities = []
    all_entries = record["your_text"]

    # fit a tfidf vectorizer to all texts
    tfidf = TfidfVectorizer().fit(all_entries)
    for entry in all_entries:

        # calculate the euclidean distance for each entry
        row_of_similarities = []
        for diff_entry in all_entries: 

            # transform sentences to a vector
            vects = tfidf.transform([entry.lower(), diff_entry.lower()])
            vects = vects.todense()
            vect_one, vect_two = np.squeeze(np.asarray(vects[0])), np.squeeze(np.asarray(vects[1]))

            cos_sim = dot(vect_one, vect_two)/(norm(vect_one)*norm(vect_two))
            if cos_sim < 0.5:
                row_of_similarities.append("Not similar")
            elif cos_sim > 0.5 and cos_sim < 0.75:
                row_of_similarities.append("Somewhat similar")
            else:
                row_of_similarities.append("Very similar")

        # append a row of distances to the list of all distances
        all_similarities.append(row_of_similarities)
        
    # return distance matrix
    return {"distances": all_similarities}
```