import spacy

def download_all_models():
    print("Downloading spacy models...")
    models = [
        "en_core_web_sm",
        "de_core_news_sm",
        "fr_core_news_sm",
        "es_core_news_sm",
        "pt_core_news_sm",
        "it_core_news_sm",
        "nl_core_news_sm",
        "xx_ent_wiki_sm",
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