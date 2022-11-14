import nltk


def download_all_modules():
    modules = [
        "wordnet",
        "omw-1.4",
    ]

    for i in modules:
        print(f"Downloading NLTK corpus {i}...")
        nltk.download(i)
