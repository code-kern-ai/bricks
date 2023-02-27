```python
from skopt import BayesSearchCV
from skopt.space import Real, Categorical, Integer
from sklearn.ensemble import RandomForestClassifier
from typing import List

YOUR_EMBEDDING: str = "text-classification-distilbert-base-uncased" # pick this from the options above
YOUR_MIN_CONFIDENCE: float = 0.8
YOUR_ITERATIONS: int = 100 # this can be modified by the user
YOUR_LABELS: List[str] = None # optional, you can specify a list to filter the predictions (e.g. ["label-a", "label-b"])

class MyBayesian(LearningClassifier):
    def __init__(self):
        self.base_classifier = RandomForestClassifier()
        self.param_grid = {
            'C': Real(1e-6, 1e+6, prior='log-uniform'),
            'gamma': Real(1e-6, 1e+1, prior='log-uniform'),
            'degree': Integer(1,8),
            'kernel': Categorical(['linear', 'poly', 'rbf']),
        }   # the hyperparameters can be modified by the user
        self.model = BayesSearchCV(self.base_classifier, self.param_grid, n_iter=YOUR_ITERATIONS)
        
    @params_fit(
        embedding_name = YOUR_EMBEDDING,
        train_test_split = 0.5
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