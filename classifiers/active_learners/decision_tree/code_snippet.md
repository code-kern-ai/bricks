```python
from sklearn.tree import DecisionTreeClassifier
# you can find further models here: https://scikit-learn.org/stable/supervised_learning.html#supervised-learning

class MyDT(LearningClassifier):

    def __init__(self):
        self.model = DecisionTreeClassifier()

    @params_fit(
        embedding_name = "your-embedding", # pick this from the options above
        train_test_split = 0.5 # we currently have this fixed, but you'll soon be able to specify this individually!
    )
    def fit(self, embeddings, labels):
        self.model.fit(embeddings, labels)

    @params_inference(
        min_confidence = 0.8,
        label_names = None # you can specify a list to filter the predictions (e.g. ["label-a", "label-b"])
    )
    def predict_proba(self, embeddings):
        return self.model.predict_proba(embeddings)
```