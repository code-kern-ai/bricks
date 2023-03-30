```python
import numpy as np 
from numpy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer

# replace this list with a list containing your data
text = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "your_text": text,
}

# function for the euclidean distance, should return a n*n matrix. n being the number of texts
def euclidean_distance(record: dict) -> dict:
    all_distances = []
    all_entries = record["your_text"]

    # fit a tfidf vectorizer to all texts
    tfidf = TfidfVectorizer().fit(all_entries)
    for entry in all_entries:

        # calculate the euclidean distance for each entry
        row_of_distances = []
        for diff_entry in all_entries: 

            # transform sentences to a vector
            vects = tfidf.transform([entry.lower(), diff_entry.lower()])
            vects = vects.todense()
            vect_one, vect_two = np.squeeze(np.asarray(vects[0])), np.squeeze(np.asarray(vects[1]))

            # return the row of distances 
            row_of_distances.append(np.linalg.norm(vect_one - vect_two))

        # append a row of distances to the list of all distances
        all_distances.append(row_of_distances)
        
    # return distance matrix
    return all_distances
```