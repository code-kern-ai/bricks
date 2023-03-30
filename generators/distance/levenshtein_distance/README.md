The Levenshtein distance is a string metric for measuring the difference between two sequences. It is calculated as the minimum number of single-character edits necessary to
transform one string into another.

The optional weights are for the three operations in the form of a tuple (insertion, deletion, substitution).

The difference between the code in `code_snippet_refinery.md` and `code_snippet_common.md` is, that the common code returns a matrix of all the similarities, while the refinery code returns only individual values based on a base sentence. This is because the refinery code cannot (yet) access all the data at the same time. Please also note that refinery also calculates the cosine similarity between all texts based on the transformer embeddings in the vector database by default. 