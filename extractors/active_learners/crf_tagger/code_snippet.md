```python
from sequencelearn.sequence_tagger import CRFTagger
# you can find further models here: https://github.com/code-kern-ai/sequence-learn

YOUR_EMBEDDING: str = "text-extraction-distilbert-base-uncased" # pick this from the options above

class MyActiveLearner(LearningExtractor):

    def __init__(self):
        self.model = CRFTagger(
            num_epochs = 100, # Number of epochs to train the CRF tagger
            learning_rate = 0.001, # Factor to apply during backpropagation
            momentum = 0.9, # Factor to weigh previous iteration during training
            random_seed = None, # Random seed to use for reproducibility. If None, a random seed is chosen
            verbose = False, # set to True to see the training progress
        )

    @params_fit(
        embedding_name = YOUR_EMBEDDING, 
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