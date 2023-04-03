```python
from skopt import BayesSearchCV
from skopt.space import Real, Categorical, Integer
from sklearn.svm import SVC
from typing import List

# install with 'pip install embedders' or clone from: https://github.com/code-kern-ai/embedders
from embedders.classification.contextual import TransformerSentenceEmbedder
from embedders.classification.reduce import PCASentenceReducer

corpus = ["replace this with a list of your texts"] 

# instantiate sentence embedder and fit to corpus
embedder = TransformerSentenceEmbedder("bert-base-cased")
embeddings = embedder.fit_transform(corpus)

record = {
    "embedding_name":  embeddings
    "min_confidence": 0.8, 
    "iterations": 100, 
    "labels": None,
}

class MyBayesian(LearningClassifier):
    def __init__(self):
        self.base_classifier = SVC(probability=True)
        self.param_grid = {
            'C': Real(1e-6, 1e+6, prior='log-uniform'),
            'gamma': Real(1e-6, 1e+1, prior='log-uniform'),
            'degree': Integer(1,8),
            'kernel': Categorical(['linear', 'poly', 'rbf']),
        }   # the hyperparameters can be modified by the user
        self.model = BayesSearchCV(self.base_classifier, self.param_grid, n_iter=record["iterations"])
        
    @params_fit(
        embeddings = record["embedding_name"],
        train_test_split = 0.5
    )
    
    def fit(self, embeddings, labels):
        self.model.fit(embeddings, labels)
        
    @params_inference(
        min_confidence = record["min_confidence"],
        label_names = record["labels"]
    )
    
    def predict_proba(self, embeddings):
        return self.model.predict_proba(embeddings)


```