# Welcome to the contributions guideline for bricks
This is the official repository to add further modules/heuristics to bricks maintained mostly by Kern AI. Please refer to this document if you want to add your own modules/heuristics to the library.

## Table of contents
- [Structure of this repository](#structure-of-this-repository)
- [How to contribute ideas](#how-to-contribute-ideas)
- [How to contribute modules](#how-to-contribute-modules)
- [Quality assurance](#quality-assurance)
- [What happens next?](#what-happens-next)


## Structure of this repository
We have structured this repository into two main folders:
- `classifiers`: this is where modules will go into that are used to classify a given text into a specific category. For example, a module that classifies a text into the category `news` or `blog` would go into this folder. It can also be about enrichments, e.g. to detect languages and such.
- `extractors`: this is where modules will go into that are used to extract information from a given text. For example, a module that extracts the author of a text would go into this folder.

In each folder, you will find further directories, typically in this structure:
- `python_functions`: functions you would write as labeling functions in refinery. Think of very simplistic Python snippets. Each python function is implemented as a directory, containing an `__init__.py` file with the endpoint function and a `code_snippet.md` file with a description of the function.
- `active_learning`: this will contain configuration files for active learning. You can use these to train your models in refinery.
- `zero_shot`: this is where we'll add configurations for zero-shot models as soon as refinery has a programmable zero-shot interface (atm it is no-code, but we'll change that in the near future).
- `premium`: those are modules that require some sort of API key. We will add them here, but only the request code, not the API key itself. We will add a `README.md` file in this folder that explains how to get the API key and how to use it.

## How to contribute ideas
If you have an idea for a new module/heuristic, please open an issue in the repository. We will discuss the idea and if it is a good fit for the library, we will add it to the library. This means you don't _have to write_ the code yourself, but you can still contribute to the library.

## How to contribute modules
1. As stated above, please first add the idea as an issue. We'll use this to document the origin of the module, and will use it to help you during the contribution.
2. Create a new branch with the name of the module you want to add. Please do **not** add multiple modules in one branch.
3. Add a directory to the file system fitting your request, e.g. `classifiers/python_functions/your_module_name`. Inside it, add an `__init__.py` file with the endpoint function and a `code_snippet.md` file with a description of the function. Also add a `README.md` file with a description of the module. You can use the other modules as a template, or reach out to us on [Discord](https://discord.gg/qf4rGCEphW).
4. For further details on _how_ to implement the module, see the section below.
5. Create a pull request to the `main` branch of the repository. We will review your code and merge it into the repository, and add a `config.py` file which will be used to push your module to the library.

### How to implement a module
All modules follow a similar structure. The following is a template for a module, which you can add as a directory with an `__init__.py` file and a `code_snippet.md` file. The `__init__.py` for the `language_detection` module looks like this:

```python
# These are the import statements. Please make sure to add them here.
from pydantic import BaseModel
from langdetect import detect, DetectorFactory 
DetectorFactory.seed = 0

# This is how the endpoint will understand request data. Simply think of this as a function signature. The below code would look as follows in "pure Python":
# def module_name(text: str):
#    pass
class LanguageDetectionModel(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": {
                "text": "This is an english sentence."
            }
        }

# This is the actual module. It takes the request data as input and returns the output.
def language_detection(request: LanguageDetectionModel):
    # If you want to, you can add a docstring. We'll be loving you for that :D
    """Detect language of text."""

    # This is where the logic goes. Please note: the endpoint logic can look slightly different to the code that is displayed in the module itself, as requests work different than plain Python.
    text = request.text
    language = detect(text)
    return {"language": language}
```

And the `code_snippet.md` file looks like this:

```python
# This is how the actual module will be displayed in the library.

from typing import Dict, Any
from langdetect import detect

def fn_language_detection(record: Dict[str, Any]) -> str:
    """Detect language of text
        
    Args:
        record (Dict): one single record you want to process

    Returns:
        str: Language of your text
    """

    text = record["your-text"]
    language = detect(text)
    return language
```

Afterwards, you can add your module to the `__init__.py` file in the respective folder (`classifiers` or `extractors`). This is how the `__init__.py` file looks like:

```python
from fastapi import APIRouter
from .python_functions import language_detection

router = APIRouter()

@router.post(f"/{language_detection.language_detection.__name__.lower()}")
def api_language_detection(request: language_detection.LanguageDetectionModel):
    return language_detection.language_detection(request)
```

Lastly, we'd be really thankful if you update the `requirements.txt` of the repository to include the libraries needed for your module. For the above code, this would be:
```
langdetect
```

If you're not sure, no worries, we're already incredibly thankful for your contribution! We'll add this to the requirements file ourselves.

### spaCy for extractor modules
We use spaCy for extractor modules, as it helps to put texts into correct tokens. Please use spaCy for extractor modules, and match character returns with token-level returns. For instance:
```python
def date_extraction(request: DateExtraction):
    text = request.text
    
    # load the spaCy module as a singleton
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)

    # process e.g. via a regular expression
    regex = re.compile(r"(?:[0-9]{1,2}|Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[\/\. -]{1}(?:[0-9]{1,2}|Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[,\/\. -]{1}(?:[0-9]{2,4})")
 # added whitespace instead of \s since \s can also read newline
    regex.findall(text)

    # match the found character indices to spaCy
    spans = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        spans.append([span.start, span.end, span.text])

    return {"spans": spans}
```

## Quality assurance
We want to make sure that things work nicely and that the modules are of high quality. Therefore, when we will review your submission, we'll do blackbox tests and will check the above criteria. Again, this is about collaboration, so please don't worry about this too much. We'll help you with this!

## What happens next?
We have a content management system up and running, in which we enter newly registered endpoints. As soon as your endpoint is merged into the `main` branch, we'll add it to the CMS. This triggers a task for our dev rel team, so it usually doesn't take too long. You can then find it in our online library :)