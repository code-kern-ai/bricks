```python
# import what is required from sequence-learn (see next line)
# you can find further models here: https://github.com/code-kern-ai/sequence-learn

class MyActiveLearner(LearningExtractor):

    def __init__(self):
        self.model = None # enter the model to be used by bricks here

    @params_fit(
        embedding_name = "your-embedding", # pick this from the options above
        train_test_split = 0.5 # we currently have this fixed, but you'll soon be able to specify this individually!
    )
    def fit(self, embeddings, labels):
        self.model.fit(embeddings, labels)

    @params_inference(
        min_confidence = 0.9,
        label_names = None # you can specify a list to filter the predictions (e.g. ["label-a", "label-b"])
    )
    def predict_proba(self, embeddings):
        return self.model.predict_proba(embeddings)

```