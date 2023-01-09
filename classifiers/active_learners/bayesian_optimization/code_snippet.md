```python
from sklearn.ensemble import RandomForestClassifier
from bayes_opt import BayesianOptimization
from sklearn.model_selection import cross_val_score

class MyBayesian(LearningClassifier):
    
    def __init__(self, n_iter=10, cv=5, random_state=42):
        self.n_iter = n_iter
        self.cv = cv
        self.random_state = random_state
        self.base_classifier = RandomForestClassifier(random_state=self.random_state, n_jobs=-1,
                                                      n_estimators=100, max_depth=3)
        
    @params(
        embedding_name = "your_embedding",
        train_test_split = 0.5
    )
    
    def fit(self, embeddings, labels):
        self.model.fit(embeddings, labels)
        self.y_pred = self.model.predict(embeddings)
        for i in range(self.n_iter):
            self.optimizer = BayesianOptimization(
                f=self.cross_validation_score,
                pbounds={
                    "max_depth": (3,10),
                    "n_estimators": (10, 100),
                    "min_sample_split": (2, 10),
                    "min_sample_leaf": (1, 10),
                    "max_features": (0.1, 0.9)
                },
                random_state = self.random_state
            )
            self.optimizer.maximize(init_points=5, n_iter=10)
            self.best_params = self.optimizer.max["params"]
            self.model.set_params(**self.best_params)
            self.model.fit(embeddings, labels)
    
        
    def cross_validation_score(self, max_depth, n_estimators, min_samples_split, min_samples_leaf,
                               max_features, embeddings, labels):
        self.model.set_params(
            max_depth=int(max_depth),
            n_estimators=int(n_estimators),
            min_samples_split=int(min_samples_split),
            min_samples_leaf = int(min_samples_leaf),
            max_features = max_features
        )
        
        return cross_val_score(self.model, embeddings, labels, cv=self.cv).mean()
    
    @params_inference(
        min_confidence = 0.8,
        label_names = None
    )
    
    def predict_prob(self, embeddings):
        self.model.predict(embeddings)
```