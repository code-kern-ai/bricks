import spacy

def download_all_models():
    print("Downloading spacy models...")
    models = [
        "en_core_web_sm",
        "en_core_web_lg"
    ]
    for model in models:
        print(f"Downloading {model}...")
        download_model(model)

def download_model(model):
    """Download a spacy model if it doesn't exist."""
    try:
        spacy.load(model)
    except OSError:
        spacy.cli.download(model)
        spacy.load(model)

class SpacySingleton:
    nlp = None

    @classmethod
    def get_nlp(cls, model="en_core_web_sm"):
        if cls.nlp is None:
            cls.nlp = spacy.load(model)
        return cls.nlp