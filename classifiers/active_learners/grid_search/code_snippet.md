```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

YOUR_EMBEDDING: str = "headline-classification-distilbert-base-uncased" # pick this from the options above
YOUR_TRAIN_TEST_SPLIT: float = 0.5 # we currently have this fixed, but you'll soon be able to specify this individually!
YOUR_MIN_CONFIDENCE: float = 0.8

class MyGrid(LearningClassifier):
    
    def __init__(self):
        self.base_classifier = RandomForestClassifier()
        self.param_grid = {
            "n_estimators": [10, 100, 1000],
            "max_depth": [1, 10, 100, None],
            "min_samples_split": [2, 5, 10],
            "min_samples_leaf": [1, 2, 4],
            "bootstrap": [True, False]
        } # the hyperparameters can be tuned by the user
        self.model = GridSearchCV(self.base_classifier, self.param_grid)

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