```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from typing import List

EMBEDDING: str = "text-classification-distilbert-base-uncased" # pick this from the options above
MIN_CONFIDENCE: float = 0.8
ITERATIONS: int = 100 # this can be modified by the user
LABELS: List[str] = None # optional, you can specify a list to filter the predictions (e.g. ["label-a", "label-b"])

class MyRandom(LearningClassifier):
    
    def __init__(self):
        self.base_classifier = RandomForestClassifier()
        self.param_grid = {
            'n_estimators': [10, 100, 1000],
            'max_depth': [1, 10, 100, None],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4],
            'bootstrap': [True, False]
        } # the hyperparameters can be tuned by the user
        self.model = RandomizedSearchCV(self.base_classifier, self.param_grid, n_iter=ITERATIONS) # n_iter is the number of iterations and can be modified by the user

    @params_fit(
        embedding_name = EMBEDDING, 
        train_test_split = 0.5 # we currently have this fixed, but you'll soon be able to specify this individually!
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