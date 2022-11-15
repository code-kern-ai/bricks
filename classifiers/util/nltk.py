import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


def download_corpora():
    corpora = [
        "words",
        "brown",
        "punkt",
    ]

    for i in corpora:
        print(f"Downloading NLTK corpus {i}...")
        nltk.download(i)