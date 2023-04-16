```python
from skopt import BayesSearchCV
from skopt.space import Real, Categorical, Integer
from sklearn.svm import SVC
from typing import List

EMBEDDING: str = "text-classification-distilbert-base-uncased" # pick this from the options above
MIN_CONFIDENCE: float = 0.8
ITERATIONS: int = 100 # this can be modified by the user
LABELS: List[str] = None # optional, you can specify a list to filter the predictions (e.g. ["label-a", "label-b"])

class MyBayesian(LearningClassifier):
    def __init__(self):
        self.base_classifier = SVC(probability=True)
        self.param_grid = {
            'C': Real(1e-6, 1e+6, prior='log-uniform'),
            'gamma': Real(1e-6, 1e+1, prior='log-uniform'),
            'degree': Integer(1,8),
            'kernel': Categorical(['linear', 'poly', 'rbf']),
        }   # the hyperparameters can be modified by the user
        self.model = BayesSearchCV(self.base_classifier, self.param_grid, n_iter=ITERATIONS)
        
    @params_fit(
        embedding_name = EMBEDDING,
        train_test_split = 0.5
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