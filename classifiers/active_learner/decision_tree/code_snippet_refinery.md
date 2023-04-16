```python
from sklearn.tree import DecisionTreeClassifier
from typing import List
# you can find further models here: https://scikit-learn.org/stable/supervised_learning.html#supervised-learning

YOUR_EMBEDDING: str = "text-classification-distilbert-base-uncased" 
YOUR_MIN_CONFIDENCE: float = 0.8
YOUR_LABELS: List[str] = None # optional, you can specify a list to filter the predictions

class MyDT(LearningClassifier):

    def __init__(self):
        self.model = DecisionTreeClassifier()

    @params_fit(
        embedding_name = YOUR_EMBEDDING, 
        train_test_split = 0.5 # we have this fixed at the moment, but you'll soon be able to specify this individually! 
    )
    def fit(self, embeddings, labels):
        self.model.fit(embeddings, labels)

    @params_inference(
        min_confidence = YOUR_MIN_CONFIDENCE,
        label_names = YOUR_LABELS 
    )
    def predict_proba(self, embeddings):
        return self.model.predict_proba(embeddings)
```