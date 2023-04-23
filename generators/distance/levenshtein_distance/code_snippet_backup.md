```python
from Levenshtein import distance as levenshtein_dist

# replace this list with a list containing your data
text = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "your_text": text,
    "weight_insertion": 1,
    "weight_deletion": 1,
    "weight_substitution": 1,
}

# function for the hamming distance, should return a n*n matrix. n being the number of texts
def levenshtein_distance(record: dict) -> dict:
    # check if weights are provided
    if record["weight_insertion"] is not None and record["weight_deletion"] is not None and record["weight_substitution"] is not None:
        weights_tuple = (
            record["weight_insertion"],
            record["weight_deletion"],
            record["weight_substitution"],
        )
    # otherwise use default weights
    else: 
        weights_tuple = (1, 1, 1)

    # list to store matrix of distances
    all_distances = []

    # retrieve all texts
    all_entries = record["your_text"]

    # calculate distance for each pair of texts
    for entry in all_entries:
        row_of_distances = []
        for diff_entry in all_entries:
            string_one = entry
            string_two = diff_entry
            ls_distance = levenshtein_dist(string_one, string_two, weights=weights_tuple)
    
            # append one distance to the row
            row_of_distances.append(ls_distance)
        # append whole row of distances to the matrix
        all_distances.append(row_of_distances)
    return {"distances": all_distances}
```