import nltk

def download_all_modules():
    modules = [
        "wordnet"
    ]

    for i in modules:
        print(f"Downloading NLTK corpus {i}...")
        nltk.download(i)