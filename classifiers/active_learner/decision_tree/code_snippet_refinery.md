```python
from sklearn.tree import DecisionTreeClassifier
from typing import List
# you can find further models here: https://scikit-learn.org/stable/supervised_learning.html#supervised-learning

EMBEDDING: str = "text-classification-distilbert-base-uncased" 
MIN_CONFIDENCE: float = 0.8
LABELS: List[str] = None # you can specify a list to filter the predictions (e.g. ["label-a", "label-b"])

class MyDT(LearningClassifier):

    def __init__(self):
        self.model = DecisionTreeClassifier()

    @params_fit(
        embedding_name = EMBEDDING, 
        train_test_split = 0.5 # we have this fixed at the moment, but you'll soon be able to specify this individually! 
    )
    def fit(self, embeddings, labels):
        self.model.fit(embeddings, labels)

    @params_inference(
        min_confidence = MIN_CONFIDENCE,
        label_names = LABELS 
    )
    def predict_proba(self, embeddings):
        return self.model.predict_proba(embeddings)
```