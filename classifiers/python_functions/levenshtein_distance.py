from pydantic import BaseModel
from typing import Optional
from Levenshtein import distance as levenshtein_distance

class LevenshteinDistanceModel(BaseModel):
    string1: str
    string2: str
    weights: Optional[tuple]

    class Config:
        schema_extra = {
            "example": {
                "text_01": "Example.",
                "text_02": "Examples",
                "weights": (1, 1, 1)
            }
        }

def fn_levenshtein_distance(requests: LevenshteinDistanceModel):
    """
    The Levenshtein distance is a string metric for measuring the difference
    between two sequences.
    It is calculated as the minimum number of single-character edits necessary to
    transform one string into another.

    Args:
        request (LevenshteinDistanceModel): schema of request body

    Returns:
        dict: Levenshtein distance of two words
    """
    str_01 = requests.text_01
    str_02 = requests.text_02
    weights = requests.weights

    if weights is not None:
        ls_distance = levenshtein_distance(str_01, str_02, weights=weights)
    else:
        ls_distance = levenshtein_distance(str_01, str_02)
    return {"Levenshtein distance": ls_distance}

