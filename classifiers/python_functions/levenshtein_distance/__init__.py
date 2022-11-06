from pydantic import BaseModel
from typing import Dict
from Levenshtein import distance as levenshtein_distance

class LevenshteinDistanceModel(BaseModel):
    textFirst: str
    textSecond: str
    weights: Dict[str, int] = {
        "insertion": 1,
        "deletion": 1,
        "substitution": 1,
    }

    class Config:
        schema_extra = {
            "example": {
                "textFirst": "John Doe",
                "textSecond": "Jon Doe",
                "weights": {
                    "insertion": 1,
                    "deletion": 1,
                    "substitution": 1
                }
            }
        }

def fn_levenshtein_distance(request: LevenshteinDistanceModel):
    """
    The Levenshtein distance is a string metric for measuring the difference
    between two sequences.
    It is calculated as the minimum number of single-character edits necessary to
    transform one string into another.

    The optional weights are for the three operations in the form of a tuple (insertion, deletion, substitution).

    Args:
        request (LevenshteinDistanceModel): schema of request body

    Returns:
        dict: Levenshtein distance of two words
    """

    text_first = request.textFirst 
    text_second = request.textSecond
    weights = request.weights

    if weights is not None:
        weights_tuple = (weights["insertion"], weights["deletion"], weights["substitution"])
        ls_distance = levenshtein_distance(text_first, text_second, weights=weights_tuple)
    else:
        ls_distance = levenshtein_distance(text_first, text_second)
    return {"levenshteinDistance": ls_distance}

