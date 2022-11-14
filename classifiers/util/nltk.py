import nltk


def download_corpora():
    corpora = [
        "words",
        "brown"
    ]

    for i in corpora:
        print(f"Downloading NLTK corpus {i}...")
        nltk.download(i)
