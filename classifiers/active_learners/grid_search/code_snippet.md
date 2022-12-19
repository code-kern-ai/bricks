```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

class MyGrid(LearningClassifier):
    
    def __init__(self):
        self.base_classifier = RandomForestClassifier()
        self.model = GridSearchCV(self.base_classifier)

    @params_fit(
        embedding_name = "your-embedding",
        train_test_split = 0.5
    )

    def fit(self, embeddings, labels):
        self.model.fit(embeddings, labels)

    @params_inference(
        min_confidence = 0.8,
        label_names = None
    )

    def predict_prob(self, embeddings):
        return self.model.predict(embeddings)
```