from extractors.python_functions.regex_extraction import RegexExtractionModel, regex_extraction

INPUT_EXAMPLE = {
    "text": "percentages 110% are found -.5% at 42,13% positions 1, 5 and 8",
    "spacyTokenizer": "en_core_web_sm",
}


class PercentageExtractionModel(RegexExtractionModel):
    regex: str = r"(-?\d+(?:[.,]\d*)?|-?[.,]\d+)%"
    yourLabel: str = "percentage"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def percentage_extraction(request: PercentageExtractionModel):
    """Extracts percentages from a given text."""

    return regex_extraction(request)