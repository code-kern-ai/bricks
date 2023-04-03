from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
from extractors.python_functions.regex_extraction import RegexExtractionModel, regex_extraction

INPUT_EXAMPLE = {
    # "text": "tricky percentage - .5  % with sloppy whitespaces is found between position 3 and 6",
    "text": "percentages 110% are found -.5% at 50,25% positions 1, 5 and 8",
    "spacyTokenizer": "en_core_web_sm",
}


# make sure the model name fits to the function name, as it is actually parsed
# i.e. my_tagger -> MyTaggerModel (capitalized and "Model" appended)
class PercentageExtractionModel(RegexExtractionModel):
    # regex: str = r'\s*(-?\d+(?:[.,]\d*)?|-?[.,]\d+)\s*%'
    regex: str = r'(-?\d+(?:[.,]\d*)?|-?[.,]\d+)%'
    yourLabel: str = "percentage"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def percentage_extraction(request: PercentageExtractionModel):
    """Extracts percentages from a given text."""
    ret = regex_extraction(request)
    return ret

    # text = request.text
    # nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    # doc = nlp(text)

    # # my function logic here
    # pattern = r'\s*(-?\d+(?:[.,]\d*)?|-?[.,]\d+)\s*%'
    # percentages = re.findall(pattern, text)
    # percentages =  [float(perc.replace(",", ".")) for perc in percentages]

    # # append to the results triplets in the form of [label, start, end]

    # # rename extractedEntities to whatever you want to call the output
    # return {"extractedEntities": results}
