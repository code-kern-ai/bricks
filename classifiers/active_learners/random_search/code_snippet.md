```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV

YOUR_EMBEDDING: str = "text-classification-distilbert-base-uncased" # pick this from the options above
YOUR_TRAIN_TEST_SPLIT: float = 0.5 # we currently have this fixed, but you'll soon be able to specify this individually!
YOUR_MIN_CONFIDENCE: float = 0.8
YOUR_ITERATIONS: int = 100 # this can be modified by the user

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
        self.model = RandomizedSearchCV(self.base_classifier, self.param_grid, n_iter=YOUR_ITERATIONS) # n_iter is the number of iterations and can be modified by the user

    @params_fit(
        embedding_name = YOUR_EMBEDDING, 
        train_test_split = YOUR_TRAIN_TEST_SPLIT # we currently have this fixed, but you'll soon be able to specify this individually!
    )

    def fit(self, embeddings, labels):
        self.model.fit(embeddings, labels)
        
    @params_inference(
        min_confidence = YOUR_MIN_CONFIDENCE,
        label_names = None # you can specify a list to filter the predictions (e.g. ["label-a", "label-b"])
    )

    def predict_proba(self, embeddings):
        return self.model.predict_proba(embeddings)
```